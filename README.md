# 🤖 Suastawa Consulting Flow
## CrewAI Agentic Automation untuk Website KJA & KKP

---

## Apa yang dilakukan Flow ini?

Saat kamu jalankan `crewai run`, 6 AI agent akan bekerja otomatis:

| Agent | Tugas |
|---|---|
| 🔍 Researcher | Riset industri KJA & KKP Indonesia |
| ✍️ Copywriter | Tulis semua konten website |
| 🔎 SEO Specialist | Buat meta tags, schema markup, sitemap |
| 🔐 Backend Dev | Generate kode Flask API + PostgreSQL |
| 🎨 Frontend Dev | Generate panel admin HTML/CSS/JS |

---

## Struktur Output

Setelah selesai, cek folder `output/`:

```
output/
├── content.md          ← Konten website (hero, layanan, tentang kami, dll)
├── seo.md              ← Meta tags, JSON-LD, sitemap, keywords
└── admin/
    ├── backend/
    │   └── app.py      ← Flask API siap deploy ke Railway
    └── frontend/
        └── admin.html  ← Panel admin siap upload ke Netlify
```

---

## Cara Jalankan

### 1. Setup environment

```bash
cp .env.example .env
# Edit .env — isi API keys kamu
```

### 2. Install dependencies

```bash
crewai install
```

### 3. Jalankan flow

```bash
crewai run
```

Perkiraan waktu: **5-15 menit** tergantung koneksi internet.

---

## Deploy Output

### Backend → Railway

```bash
# Copy output/admin/backend/app.py ke repo backend
# Set environment variables di Railway dashboard:
#   DATABASE_URL, JWT_SECRET_KEY, FLASK_ENV, FRONTEND_URL
railway up
```

### Frontend Admin → Netlify

```bash
# Copy output/admin/frontend/admin.html ke repo
# Update BACKEND_URL di dalam admin.html sesuai URL Railway
# Push ke GitHub → Netlify auto-deploy
```

### Konten Website

```bash
# Copy konten dari output/content.md ke halaman website yang sudah ada
# Pasang meta tags dari output/seo.md di <head> setiap halaman
```

---

## API Keys yang Dibutuhkan

| Key | Untuk | Daftar di |
|---|---|---|
| `ANTHROPIC_API_KEY` | AI agent (Claude) | console.anthropic.com |
| `SERPER_API_KEY` | Web search | serper.dev |

---

## Stack Teknologi

- **Frontend**: HTML/CSS/JS → Netlify
- **Backend**: Python Flask → Railway  
- **Database**: PostgreSQL → Railway
- **Domain**: suastawa-consulting.com → Namecheap
- **AI**: Claude (Anthropic) via CrewAI

---

*Dibuat dengan CrewAI — biar AI yang kerja, kamu istirahat! 🎉*
