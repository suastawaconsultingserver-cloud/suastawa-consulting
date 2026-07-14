# Update SEO Dinamis — cara pasang

File yang berubah/baru (timpa ke repo, pertahankan struktur):
- backend/app.py          (UPDATE — endpoint /api/seo)
- frontend/adminsc/admin.html  (UPDATE — menu SEO + noindex)
- worker.js               (BARU — di root repo)
- wrangler.toml           (UPDATE — mode Worker)

## Langkah
1. Salin ke-4 file di atas ke folder repo (timpa yang lama).
2. Push:
       git add .
       git commit -m "SEO dinamis: worker + admin menu + /api/seo"
       git push
3. Cloudflare auto-deploy Worker (~1-2 mnt). Railway auto-deploy backend.

## Verifikasi
- Login admin -> menu "SEO & Google" muncul -> ubah judul -> Simpan.
- Buka homepage (Incognito) -> View Source -> <title> = judul baru.
- Kalau Worker/API bermasalah, homepage tetap tampil (SEO statis bawaan) -> aman.

## Catatan
- Data SEO tersimpan di MongoDB (collection `seo`).
- JSON-LD (structured data) tetap statis di index.html (jarang berubah).
