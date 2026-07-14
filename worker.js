// Suastawa Consulting — Cloudflare Worker
// Menyajikan aset statis dari ./frontend dan menyuntikkan SEO dinamis
// (title, meta description, keywords, Open Graph, Twitter) ke homepage
// dengan mengambil data dari API. Jika API gagal, halaman tetap tampil
// dengan SEO statis bawaan index.html (fallback aman).

const API_SEO = "https://suastawa-api.up.railway.app/api/seo";

class AttrSetter {
  constructor(value) { this.value = value; }
  element(el) { if (this.value) el.setAttribute("content", this.value); }
}

class TitleSetter {
  constructor(value) { this.value = value; }
  element(el) { if (this.value) el.setInnerContent(this.value); }
}

async function fetchSeo() {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 2500);
  try {
    const r = await fetch(API_SEO, {
      signal: controller.signal,
      cf: { cacheTtl: 60, cacheEverything: true },
    });
    if (!r.ok) return null;
    return await r.json();
  } catch (e) {
    return null; // fallback: jangan ubah apa pun
  } finally {
    clearTimeout(timer);
  }
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    // Hanya homepage yang disuntik SEO dinamis
    const isHome = path === "/" || path === "/index.html";

    // Ambil aset asli dari folder frontend
    const assetResponse = await env.ASSETS.fetch(request);

    if (!isHome) return assetResponse;

    const seo = await fetchSeo();
    if (!seo) return assetResponse; // API mati -> pakai SEO statis

    const rewriter = new HTMLRewriter()
      .on("title", new TitleSetter(seo.title))
      .on('meta[name="description"]', new AttrSetter(seo.description))
      .on('meta[name="keywords"]', new AttrSetter(seo.keywords))
      .on('meta[property="og:title"]', new AttrSetter(seo.title))
      .on('meta[property="og:description"]', new AttrSetter(seo.description))
      .on('meta[property="og:image"]', new AttrSetter(seo.og_image))
      .on('meta[name="twitter:title"]', new AttrSetter(seo.title))
      .on('meta[name="twitter:description"]', new AttrSetter(seo.description))
      .on('meta[name="twitter:image"]', new AttrSetter(seo.og_image));

    return rewriter.transform(assetResponse);
  },
};
