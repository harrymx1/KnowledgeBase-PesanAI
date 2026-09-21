# STRUKTUR DIREKTORI KNOWLEDGE BASE (UM x DUTAMEDIA)

Dokumen ini menjelaskan pemisahan antara **file asli/murni bawaan awal (Pure Knowledge Base UM)** dengan **file/folder hasil olahan & tools internal QA Dutamedia**.

---

## 🗂️ 1. File Asli Bawaan (Pure Original UM)
*File-file berikut adalah dokumen asli 100% dari Universitas Negeri Malang (UM) dalam format PDF:*
- **12 Dokumen PDF di Root**: Pengumuman penerimaan dosen, sarana prasarana, helpdesk 1 nomor, SKB libur, peniadaan CFD, dan Transfer Knowledge (1 & 2).
- 📁 **`Informasi Penerimaan Maba/`** (68 File PDF): Jalur SNBP, SNBT, dan Seleksi Mandiri berbagai jenjang/jalur.
- 📁 **`Panduan Siakad/`** (6 File PDF): Panduan aktivasi dan penggunaan SIAKAD.
- 📁 **`Registrasi UKT dan KRS/`** (12 File PDF): Biaya pendidikan, panduan pembayaran, sanggah UKT, dan registrasi administrasi.

---

## 📝 2. Hasil Konversi Markdown: `Knowledge_Base_MD/`
*Folder ini menjiplak struktur direktori asli, namun seluruh file PDF teks diubah menjadi file `.md` agar mudah dibaca, diedit, dan diunggah ke sistem Mekari Qontak:*
- Berisi **95 file `.md`** (hasil ekstraksi teks berstruktur rapi).
- Berisi **3 file `.pdf`** yang tetap dipertahankan sesuai instruksi (yaitu `Transfer_Knowledge (1).pdf`, `Transfer_Knowledge (2)_compressed.pdf`, dan `SKB_Libur_Nasional_dan_Cuti_Bersama_Tahun_2026.pdf` karena berbasis diagram/gambar visual).

---

## 🛠️ 3. Tools & Dokumentasi Internal QA: `_QA_Tools_dan_Dokumentasi/`
*Folder khusus ini memuat seluruh aset analisis, skrip otomatisasi, dan dokumen pengujian yang kita buat untuk mendukung proses QA (SIT/UAT):*
1. 📄 **`PANDUAN_QA_DAN_BEDAH_KNOWLEDGE_BASE_UM.md`**: Panduan lengkap bedah 98 dokumen, temuan red flags/konflik versi, checklist untuk meeting Tim Dev, dan Test Matrix UAT/SIT.
2. 🐍 **`analyze_kb.py`**: Skrip pemindai dan analisis metadata 98 dokumen PDF.
3. 🐍 **`detect_visual_pdfs.py`**: Skrip pendeteksi otomatis file PDF yang memuat diagram/gambar visual.
4. 🐍 **`convert_kb_to_md.py`**: Skrip engine replikasi dan konversi PDF ke format Markdown bersih.
5. 🐍 **`sortir_rekomendasi.py`**: Skrip rekomendasi pemisahan file-file usang/konflik dari unggahan Mekari.
6. 📊 **`catalog_summary.json`**: Database katalog ringkasan seluruh file (jumlah halaman, ukuran, intent, dan snippet).
