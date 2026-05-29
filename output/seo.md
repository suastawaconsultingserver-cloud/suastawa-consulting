# Paket SEO Lengkap - Suastawa Consulting

## 📋 Daftar Isi
1. Meta Tags HTML
2. Open Graph & Twitter Cards
3. JSON-LD Schema Markup
4. 20 Keyword Target
5. Sitemap XML
6. Robots.txt
7. Bonus: SEO Checklist

---

## 1. 🏷️ META TAGS HTML - Halaman Utama (Homepage)

```html
<!DOCTYPE html>
<html lang="id" prefix="og: https://ogp.me/ns#">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">

  <!-- ============================================
       PRIMARY META TAGS
  ============================================ -->
  <title>Suastawa Consulting | KJA & KKP Terpercaya - Konsultan Pajak & Akuntan Profesional Bali</title>

  <meta name="title"
        content="Suastawa Consulting | KJA & KKP Terpercaya - Konsultan Pajak & Akuntan Profesional Bali">

  <meta name="description"
        content="Suastawa Consulting adalah KJA (Kantor Jasa Akuntan) dan KKP (Kantor Konsultan Pajak) terdaftar dan berizin resmi. Layanan: laporan keuangan, audit, perencanaan pajak, SPT tahunan, konsultasi bisnis. Hubungi kami sekarang!">

  <meta name="keywords"
        content="KJA Bali, KKP Bali, kantor jasa akuntan, kantor konsultan pajak, konsultan pajak terdaftar, jasa akuntan profesional, laporan keuangan, audit keuangan, SPT tahunan, perencanaan pajak, Suastawa Consulting, konsultan bisnis Bali, jasa pembukuan, tax planning, akuntan publik Bali">

  <meta name="author" content="Suastawa Consulting">
  <meta name="publisher" content="Suastawa Consulting">
  <meta name="copyright" content="© 2024 Suastawa Consulting. All Rights Reserved.">
  <meta name="language" content="Indonesian">
  <meta name="revisit-after" content="7 days">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <meta name="googlebot" content="index, follow">
  <meta name="bingbot" content="index, follow">

  <!-- Geo Tags (Lokasi Bisnis) -->
  <meta name="geo.region" content="ID-BA">
  <meta name="geo.placename" content="Bali, Indonesia">
  <meta name="geo.position" content="-8.4095;115.1889">
  <meta name="ICBM" content="-8.4095, 115.1889">

  <!-- ============================================
       OPEN GRAPH TAGS (Facebook, WhatsApp, LinkedIn)
  ============================================ -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://suastawa-consulting.com/">
  <meta property="og:site_name" content="Suastawa Consulting">
  <meta property="og:locale" content="id_ID">
  <meta property="og:title"
        content="Suastawa Consulting | KJA & KKP Terpercaya - Konsultan Pajak & Akuntan Bali">
  <meta property="og:description"
        content="KJA dan KKP berizin resmi. Layanan konsultasi pajak, laporan keuangan, audit, SPT tahunan, pembukuan, dan perencanaan pajak untuk UMKM hingga perusahaan besar di Bali dan seluruh Indonesia.">
  <meta property="og:image"
        content="https://suastawa-consulting.com/assets/images/og-image-suastawa-consulting.jpg">
  <meta property="og:image:secure_url"
        content="https://suastawa-consulting.com/assets/images/og-image-suastawa-consulting.jpg">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt"
        content="Suastawa Consulting - KJA dan KKP Profesional di Bali">

  <!-- ============================================
       TWITTER CARD TAGS
  ============================================ -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@suastawaconsult">
  <meta name="twitter:creator" content="@suastawaconsult">
  <meta name="twitter:url" content="https://suastawa-consulting.com/">
  <meta name="twitter:title"
        content="Suastawa Consulting | KJA & KKP - Konsultan Pajak & Akuntan Bali">
  <meta name="twitter:description"
        content="KJA & KKP berizin resmi. Konsultasi pajak, laporan keuangan, audit, SPT tahunan untuk UMKM & perusahaan di Bali dan Indonesia.">
  <meta name="twitter:image"
        content="https://suastawa-consulting.com/assets/images/og-image-suastawa-consulting.jpg">
  <meta name="twitter:image:alt"
        content="Suastawa Consulting - Konsultan Pajak dan Akuntan Profesional">

  <!-- ============================================
       CANONICAL & ALTERNATE
  ============================================ -->
  <link rel="canonical" href="https://suastawa-consulting.com/">
  <link rel="alternate" hreflang="id" href="https://suastawa-consulting.com/">
  <link rel="alternate" hreflang="x-default" href="https://suastawa-consulting.com/">

  <!-- ============================================
       FAVICON & APP ICONS
  ============================================ -->
  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/icons/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/icons/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#1a3c6e">
  <meta name="msapplication-TileColor" content="#1a3c6e">

  <!-- ============================================
       PRECONNECT & PERFORMANCE
  ============================================ -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="dns-prefetch" href="//www.google-analytics.com">
  <link rel="dns-prefetch" href="//www.googletagmanager.com">

  <!-- ============================================
       JSON-LD SCHEMA (lihat Seksi 3)
  ============================================ -->
  <!-- Schema scripts diletakkan di sini -->

</head>
```

---

## 2. 🏷️ META TAGS PER HALAMAN

```html
<!-- ============================================
     HALAMAN: Layanan KJA (Kantor Jasa Akuntan)
     URL: /layanan/kja
============================================ -->
<title>Layanan KJA - Kantor Jasa Akuntan | Suastawa Consulting Bali</title>
<meta name="description"
      content="Layanan KJA (Kantor Jasa Akuntan) Suastawa Consulting: laporan keuangan PSAK, audit internal, pembukuan akuntansi, review laporan keuangan, dan kompilasi laporan untuk UMKM dan korporasi di Bali.">
<link rel="canonical" href="https://suastawa-consulting.com/layanan/kja">

<!-- ============================================
     HALAMAN: Layanan KKP (Kantor Konsultan Pajak)
     URL: /layanan/kkp
============================================ -->
<title>Layanan KKP - Kantor Konsultan Pajak | Suastawa Consulting Bali</title>
<meta name="description"
      content="Layanan KKP (Kantor Konsultan Pajak) berizin resmi Suastawa Consulting: konsultasi pajak, perencanaan pajak, pengisian SPT tahunan badan & pribadi, restitusi pajak, keberatan & banding pajak di Bali.">
<link rel="canonical" href="https://suastawa-consulting.com/layanan/kkp">

<!-- ============================================
     HALAMAN: Tentang Kami
     URL: /tentang-kami
============================================ -->
<title>Tentang Kami - Profil KJA & KKP Suastawa Consulting Bali</title>
<meta name="description"
      content="Suastawa Consulting adalah KJA dan KKP berizin resmi yang berpengalaman lebih dari 10 tahun di Bali. Tim profesional bersertifikat BKP dan akuntan terdaftar siap membantu bisnis Anda.">
<link rel="canonical" href="https://suastawa-consulting.com/tentang-kami">

<!-- ============================================
     HALAMAN: Kontak
     URL: /kontak
============================================ -->
<title>Hubungi Suastawa Consulting - KJA KKP Bali | Konsultasi Gratis</title>
<meta name="description"
      content="Hubungi Suastawa Consulting untuk konsultasi pajak dan akuntansi. Alamat: [Alamat Lengkap], Bali. Telepon: [No. Telepon]. Email: info@suastawa-consulting.com. Konsultasi awal GRATIS!">
<link rel="canonical" href="https://suastawa-consulting.com/kontak">

<!-- ============================================
     HALAMAN: Blog/Artikel
     URL: /blog
============================================ -->
<title>Blog Pajak & Akuntansi Terkini | Suastawa Consulting</title>
<meta name="description"
      content="Artikel, tips, dan panduan terbaru seputar pajak, akuntansi, laporan keuangan, dan regulasi perpajakan Indonesia. Update informasi dari tim konsultan Suastawa Consulting.">
<link rel="canonical" href="https://suastawa-consulting.com/blog">
```

---

## 3. 🔷 JSON-LD SCHEMA MARKUP

```html
<!-- ============================================
     SCHEMA 1: LocalBusiness + Organization
     Untuk Homepage
============================================ -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["LocalBusiness", "AccountingService", "ProfessionalService"],
      "@id": "https://suastawa-consulting.com/#organization",
      "name": "Suastawa Consulting",
      "alternateName": ["KJA Suastawa Consulting", "KKP Suastawa Consulting"],
      "legalName": "Suastawa Consulting",
      "description": "KJA (Kantor Jasa Akuntan) dan KKP (Kantor Konsultan Pajak) berizin resmi yang menyediakan layanan konsultasi pajak, akuntansi, laporan keuangan, audit, dan perencanaan pajak untuk UMKM hingga perusahaan besar di Bali dan seluruh Indonesia.",
      "url": "https://suastawa-consulting.com",
      "logo": {
        "@type": "ImageObject",
        "url": "https://suastawa-consulting.com/assets/images/logo-suastawa-consulting.png",
        "width": 400,
        "height": 120,
        "caption": "Logo Suastawa Consulting"
      },
      "image": [
        "https://suastawa-consulting.com/assets/images/office-suastawa-consulting.jpg",
        "https://suastawa-consulting.com/assets/images/team-suastawa-consulting.jpg",
        "https://suastawa-consulting.com/assets/images/og-image-suastawa-consulting.jpg"
      ],
      "telephone": "+62-xxx-xxxx-xxxx",
      "faxNumber": "+62-xxx-xxxx-xxxx",
      "email": "info@suastawa-consulting.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "[Alamat Jalan Lengkap]",
        "addressLocality": "Denpasar",
        "addressRegion": "Bali",
        "postalCode": "80361",
        "addressCountry": "ID"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": -8.4095,
        "longitude": 115.1889
      },
      "hasMap": "https://maps.google.com/?q=Suastawa+Consulting+Bali",
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          "opens": "08:00",
          "closes": "17:00"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": "Saturday",
          "opens": "08:00",
          "closes": "13:00"
        }
      ],
      "priceRange": "Rp Rp",
      "currenciesAccepted": "IDR",
      "paymentAccepted": "Cash, Transfer Bank",
      "areaServed": [
        {
          "@type": "State",
          "name": "Bali"
        },
        {
          "@type": "Country",
          "name": "Indonesia"
        }
      ],
      "serviceArea": {
        "@type": "GeoCircle",
        "geoMidpoint": {
          "@type": "GeoCoordinates",
          "latitude": -8.4095,
          "longitude": 115.1889
        },
        "geoRadius": "100000"
      },
      "sameAs": [
        "https://www.facebook.com/suastawaconsulting",
        "https://www.instagram.com/suastawaconsulting",
        "https://www.linkedin.com/company/suastawa-consulting",
        "https://twitter.com/suastawaconsult",
        "https://www.youtube.com/@suastawaconsulting"
      ],
      "foundingDate": "2014",
      "numberOfEmployees": {
        "@type": "QuantitativeValue",
        "value": 15
      },
      "knowsAbout": [
        "Perpajakan Indonesia",
        "Akuntansi PSAK",
        "Laporan Keuangan",
        "Audit Keuangan",
        "Perencanaan Pajak",
        "SPT Tahunan",
        "Konsultasi Bisnis"
      ],
      "hasCredential": [
        {
          "@type": "EducationalOccupationalCredential",
          "credentialCategory": "Izin KJA - Kantor Jasa Akun