from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
from datetime import timedelta
import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv
from bson import ObjectId
import json
import traceback
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

app = Flask(__name__)
CORS(app, origins=["https://suastawa-consulting.com", "https://www.suastawa-consulting.com", "http://localhost:3000"])

# Config
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
if not app.config["JWT_SECRET_KEY"]:
    raise RuntimeError("JWT_SECRET_KEY environment variable tidak ditemukan")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)

jwt = JWTManager(app)

# MongoDB
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["suastawa_consulting"]

# Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

# Helper
def serialize(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError(f"Type {type(obj)} not serializable")

def doc_to_dict(doc):
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc

# ==================== AUTH ====================

@app.route("/api/auth/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = db.users.find_one({"username": username})
    if not user:
        return jsonify({"error": "Username atau password salah"}), 401
    stored = user["password"]
    # Support plaintext lama (migrasi) + hash baru
    valid = check_password_hash(stored, password) if stored.startswith("pbkdf2:") or stored.startswith("scrypt:") else stored == password
    if not valid:
        return jsonify({"error": "Username atau password salah"}), 401
    # Auto-upgrade ke hash kalau masih plaintext
    if not (stored.startswith("pbkdf2:") or stored.startswith("scrypt:")):
        db.users.update_one({"_id": user["_id"]}, {"$set": {"password": generate_password_hash(password)}})

    token = create_access_token(identity=str(user["_id"]))
    return jsonify({
        "token": token,
        "user": {"id": str(user["_id"]), "username": user["username"], "role": user["role"]}
    })

@app.route("/api/auth/ganti-password", methods=["POST"])
@jwt_required()
def ganti_password():
    data = request.json or {}
    password_lama = data.get("password_lama")
    password_baru = data.get("password_baru")

    if not password_lama or not password_baru:
        return jsonify({"error": "Password lama dan password baru wajib diisi"}), 400
    if len(password_baru) < 6:
        return jsonify({"error": "Password baru minimal 6 karakter"}), 400

    user_id = get_jwt_identity()
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return jsonify({"error": "Pengguna tidak ditemukan"}), 404
    stored = user["password"]
    valid = check_password_hash(stored, password_lama) if stored.startswith("pbkdf2:") or stored.startswith("scrypt:") else stored == password_lama
    if not valid:
        return jsonify({"error": "Password lama salah"}), 401

    db.users.update_one({"_id": ObjectId(user_id)}, {"$set": {"password": generate_password_hash(password_baru)}})
    return jsonify({"message": "Password berhasil diganti"})

# ==================== LAYANAN ====================

@app.route("/api/layanan", methods=["GET"])
def get_layanan():
    layanan = list(db.layanan.find())
    return jsonify([doc_to_dict(l) for l in layanan])

@app.route("/api/layanan", methods=["POST"])
@jwt_required()
def create_layanan():
    data = request.json
    result = db.layanan.insert_one(data)
    return jsonify({"id": str(result.inserted_id), "message": "Layanan berhasil ditambahkan"}), 201

@app.route("/api/layanan/<id>", methods=["PUT"])
@jwt_required()
def update_layanan(id):
    data = request.json
    db.layanan.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "Layanan berhasil diupdate"})

@app.route("/api/layanan/<id>", methods=["DELETE"])
@jwt_required()
def delete_layanan(id):
    db.layanan.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Layanan berhasil dihapus"})

# ==================== KONTAK / PESAN ====================

@app.route("/api/kontak", methods=["POST"])
def kirim_pesan():
    data = request.json
    required = ["nama", "email", "pesan"]
    for field in required:
        if not data.get(field):
            return jsonify({"error": f"Field '{field}' wajib diisi"}), 400

    from datetime import datetime
    data["created_at"] = datetime.utcnow().isoformat()
    data["status"] = "belum_dibaca"
    result = db.pesan.insert_one(data)
    return jsonify({"message": "Pesan berhasil dikirim", "id": str(result.inserted_id)}), 201

@app.route("/api/kontak", methods=["GET"])
@jwt_required()
def get_pesan():
    pesan = list(db.pesan.find().sort("created_at", -1))
    return jsonify([doc_to_dict(p) for p in pesan])

@app.route("/api/kontak/<id>/baca", methods=["PUT"])
@jwt_required()
def tandai_dibaca(id):
    db.pesan.update_one({"_id": ObjectId(id)}, {"$set": {"status": "sudah_dibaca"}})
    return jsonify({"message": "Pesan ditandai sudah dibaca"})

# ==================== DOKUMEN / SERTIFIKAT ====================

@app.route("/api/dokumen", methods=["GET"])
def get_dokumen():
    dokumen = list(db.dokumen.find())
    return jsonify([doc_to_dict(d) for d in dokumen])

@app.route("/api/dokumen/upload", methods=["POST"])
@jwt_required()
def upload_dokumen():
    if "file" not in request.files:
        return jsonify({"error": "File tidak ditemukan"}), 400

    file = request.files["file"]
    nama = request.form.get("nama", file.filename)
    kategori = request.form.get("kategori", "umum")

    # Cek konfigurasi Cloudinary sebelum upload
    cfg = cloudinary.config()
    if not cfg.cloud_name or not cfg.api_key or not cfg.api_secret:
        return jsonify({
            "error": "Konfigurasi Cloudinary belum lengkap. Periksa CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET di Railway Variables."
        }), 500

    try:
        result = cloudinary.uploader.upload(
            file,
            folder="suastawa_consulting",
            resource_type="auto"
        )
    except Exception as e:
        # Tampilkan pesan error asli dari Cloudinary
        print("CLOUDINARY UPLOAD ERROR:", traceback.format_exc())
        return jsonify({"error": f"Upload ke Cloudinary gagal: {str(e)}"}), 500

    from datetime import datetime
    doc = {
        "nama": nama,
        "kategori": kategori,
        "url": result["secure_url"],
        "public_id": result["public_id"],
        "format": result.get("format", ""),
        "created_at": datetime.utcnow().isoformat()
    }
    inserted = db.dokumen.insert_one(doc)
    doc["_id"] = str(inserted.inserted_id)
    return jsonify({"message": "Dokumen berhasil diupload", "dokumen": doc}), 201

@app.route("/api/dokumen/<id>", methods=["PUT"])
@jwt_required()
def update_dokumen(id):
    data = request.json
    # Hanya izinkan update metadata (nama, kategori) - bukan file
    allowed = {}
    if "nama" in data: allowed["nama"] = data["nama"]
    if "kategori" in data: allowed["kategori"] = data["kategori"]
    if allowed:
        db.dokumen.update_one({"_id": ObjectId(id)}, {"$set": allowed})
    return jsonify({"message": "Dokumen berhasil diupdate"})

@app.route("/api/dokumen/<id>", methods=["DELETE"])
@jwt_required()
def delete_dokumen(id):
    doc = db.dokumen.find_one({"_id": ObjectId(id)})
    if doc and doc.get("public_id"):
        cloudinary.uploader.destroy(doc["public_id"])
    db.dokumen.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Dokumen berhasil dihapus"})


# ==================== GALERI ====================

@app.route("/api/galeri", methods=["GET"])
def get_galeri():
    galeri = list(db.galeri.find().sort("urutan", 1))
    return jsonify([doc_to_dict(g) for g in galeri])

@app.route("/api/galeri/upload", methods=["POST"])
@jwt_required()
def upload_galeri():
    if "file" not in request.files:
        return jsonify({"error": "File tidak ditemukan"}), 400
    file = request.files["file"]
    caption = request.form.get("caption", "")
    judul = request.form.get("judul", "")
    try:
        urutan = int(request.form.get("urutan", 0))
    except (TypeError, ValueError):
        urutan = 0
    cfg = cloudinary.config()
    if not cfg.cloud_name or not cfg.api_key or not cfg.api_secret:
        return jsonify({"error": "Konfigurasi Cloudinary belum lengkap."}), 500
    try:
        result = cloudinary.uploader.upload(
            file,
            folder="suastawa_consulting/galeri",
            resource_type="auto"
        )
    except Exception as e:
        print("CLOUDINARY GALERI UPLOAD ERROR:", traceback.format_exc())
        return jsonify({"error": f"Upload ke Cloudinary gagal: {str(e)}"}), 500
    from datetime import datetime
    doc = {
        "judul": judul,
        "caption": caption,
        "url": result["secure_url"],
        "public_id": result["public_id"],
        "tipe": result.get("resource_type", "image"),
        "format": result.get("format", ""),
        "urutan": urutan,
        "created_at": datetime.utcnow().isoformat()
    }
    inserted = db.galeri.insert_one(doc)
    doc["_id"] = str(inserted.inserted_id)
    return jsonify({"message": "Galeri berhasil diupload", "galeri": doc}), 201

@app.route("/api/galeri/import", methods=["POST"])
@jwt_required()
def import_galeri():
    data = request.json or {}
    url = data.get("url")
    if not url:
        return jsonify({"error": "url wajib diisi"}), 400
    public_id = data.get("public_id", "")
    if not public_id and "/upload/" in url:
        tail = url.split("/upload/", 1)[1]
        parts = tail.split("/")
        if parts and parts[0].startswith("v") and parts[0][1:].isdigit():
            parts = parts[1:]
        public_id = "/".join(parts).rsplit(".", 1)[0]
    try:
        urutan = int(data.get("urutan", 0))
    except (TypeError, ValueError):
        urutan = 0
    from datetime import datetime
    doc = {
        "judul": data.get("judul", ""),
        "caption": data.get("caption", ""),
        "url": url,
        "public_id": public_id,
        "tipe": data.get("tipe", "image"),
        "format": url.rsplit(".", 1)[-1] if "." in url else "",
        "urutan": urutan,
        "created_at": datetime.utcnow().isoformat()
    }
    inserted = db.galeri.insert_one(doc)
    doc["_id"] = str(inserted.inserted_id)
    return jsonify({"message": "Galeri berhasil diimport", "galeri": doc}), 201

@app.route("/api/galeri/<id>", methods=["PUT"])
@jwt_required()
def update_galeri(id):
    data = request.json or {}
    allowed = {}
    if "judul" in data: allowed["judul"] = data["judul"]
    if "caption" in data: allowed["caption"] = data["caption"]
    if "urutan" in data:
        try: allowed["urutan"] = int(data["urutan"])
        except (TypeError, ValueError): pass
    if allowed:
        db.galeri.update_one({"_id": ObjectId(id)}, {"$set": allowed})
    return jsonify({"message": "Galeri berhasil diupdate"})

@app.route("/api/galeri/<id>", methods=["DELETE"])
@jwt_required()
def delete_galeri(id):
    doc = db.galeri.find_one({"_id": ObjectId(id)})
    if doc and doc.get("public_id"):
        resource_type = doc.get("tipe", "image")
        try:
            cloudinary.uploader.destroy(doc["public_id"], resource_type=resource_type)
        except Exception:
            print("CLOUDINARY GALERI DESTROY ERROR:", traceback.format_exc())
    db.galeri.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Galeri berhasil dihapus"})

# ==================== HEALTH CHECK ====================

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "Suastawa Consulting API"})

# ==================== CLOUDINARY CHECK ====================

@app.route("/api/cloudinary-check", methods=["GET"])
def cloudinary_check():
    cfg = cloudinary.config()
    return jsonify({
        "cloud_name_set": bool(cfg.cloud_name),
        "api_key_set": bool(cfg.api_key),
        "api_secret_set": bool(cfg.api_secret),
        "cloud_name": cfg.cloud_name or "(kosong)"
    })

# ==================== SEED ADMIN ====================

@app.route("/api/seed", methods=["POST"])
def seed():
    if db.users.count_documents({}) > 0:
        return jsonify({"message": "Data sudah ada"}), 400
    db.users.insert_one({
        "username": "admin",
        "password": generate_password_hash("suastawa2025"),
        "role": "admin"
    })
    return jsonify({"message": "Admin berhasil dibuat"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
