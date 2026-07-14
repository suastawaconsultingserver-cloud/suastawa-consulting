# Suastawa Consulting — suastawa-consulting.com

## Struktur
- `frontend/` → website (Cloudflare Worker `small-pine-fd8b`)
  - `index.html`, `robots.txt`, `sitemap.xml`, `adminsc/admin.html`
- `backend/`  → API Flask (Railway) — MongoDB Atlas + JWT + Cloudinary
- `wrangler.toml` → config Cloudflare (directory = ./frontend)

## Deploy FRONTEND (Cloudflare)
Otomatis via GitHub:
    git add . && git commit -m "update" && git push
Cloudflare auto-publish ~1-2 menit. (Manual: `npx wrangler deploy`)

## Deploy BACKEND (Railway)
Railway → Settings → Root Directory = `backend`
Push ke GitHub → Railway auto-deploy. Env dari `.env` (isi manual di Railway Variables).

## Setelah live: daftarkan SEO
1. Google Search Console → tambah properti suastawa-consulting.com
2. Submit sitemap: https://suastawa-consulting.com/sitemap.xml
3. Request indexing halaman utama
