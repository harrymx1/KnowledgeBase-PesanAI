# DOKUMEN PERTANGGUNGJAWABAN QA & TATA KELOLA KNOWLEDGE BASE (KNOWLEDGE BASE GOVERNANCE)
## AI WhatsApp Chatbot Universitas Negeri Malang (UM)
**Dutamedia Malang — Divisi Quality Assurance (QA)**  
*Penanggung Jawab / QA Lead: Divisi QA Internal Dutamedia Malang*  
*Tanggal: 19 September 2026*  
*Status: Final & Approved for Production Ingestion*

---

## 📌 1. Pernyataan Tanggung Jawab & Latar Belakang

Dokumen ini disusun sebagai **bentuk pertanggungjawaban profesional divisi Quality Assurance (QA)** kepada pimpinan proyek, manajemen Dutamedia, dan mitra Universitas Negeri Malang (UM) dalam memastikan kesiapan data Knowledge Base sebelum diunggah ke sistem AI Chatbot WhatsApp (Mekari Qontak AI).

### Prinsip Utama Penataan Data:
1. **Zero Data Loss (Tidak Boleh Ada Informasi yang Hilang):** Seluruh informasi penting—kuota daya tampung puluhan program studi, rincian biaya UKT & IPI, nomor kontak resmi, dan alur administrasi—dipertahankan 100% secara utuh tanpa ada teks yang terpotong.
2. **Single Source of Truth (Satu Sumber Kebenaran):** AI tidak boleh diberikan dua versi dokumen yang memiliki jadwal atau ketentuan saling bertentangan (*Knowledge Conflict*).
3. **Efisiensi Token & Anti-Duplikasi:** Sistem RAG tidak boleh dibebani file kembar identik yang memboroskan kuota token dan memicu respon berulang (*looping*).

---

## 🗂️ 2. Penjelasan Rinci Struktur Subfolder Aktif (Folder 01 s.d. 06)

Seluruh bahan yang siap diunggah ke sistem dialokasikan ke dalam **6 Subfolder Fungsional**:

### 📁 `01_PMB_Penerimaan_Mahasiswa_Baru/` (46 File | 992 KB)
* **Deskripsi:** Basis pengetahuan komprehensif seluruh jalur penerimaan mahasiswa baru di lingkungan UM untuk jenjang Diploma, Sarjana, dan Pascasarjana.
* **Cakupan Dokumen:**
  - Kuota daya tampung resmi seluruh program studi UM tahun akademik 2026.
  - Jalur Seleksi Nasional: SNBP dan SNBT (reguler & beasiswa KIP-K).
  - Seleksi Mandiri S1/D4: Prestasi (raport & kejuaraan), Skor UTBK (Gelombang 1–4 final), TMBK (ujian komputer), Leadership (ketua OSIS/organisasi), Kemitraan (institusi & mitra asuh), dan Kelas Internasional / Double Degree.
  - Program Pascasarjana: Magister S2 Reguler, S2 PJJ, Doktor S3 Reguler, dan S3 By Research.
  - Program Khusus: Fast-Track (Akselerasi Internal Triase) dan RPL (Rekognisi Pembelajaran Lampau).
  - Alur Registrasi Administrasi Mahasiswa Baru lolos seleksi dan penetapan batas waktu.
  - Template baku pola jawaban status buka/tutup jalur yang sopan.

### 📁 `02_Keuangan_dan_Biaya_Pendidikan/` (9 File | 105.1 KB)
* **Deskripsi:** Pusat data resmi seluruh skema pembiayaan studi, tarif, bank pembayaran, dan bantuan finansial.
* **Cakupan Dokumen:**
  - Rincian tarif UKT (Uang Kuliah Tunggal) Kelompok 1 s.d. 7 per program studi dan fakultas.
  - Ketentuan Sumbangan IPI (Iuran Pengembangan Institusi) jalur mandiri.
  - Panduan e-payment pembayaran menggunakan **Kode Bayar 48 Jam** melalui bank mitra resmi (BNI, BRI, BTN, Bank Mandiri, Bank Jatim, CIMB Niaga, BSI).
  - Prosedur permohonan sanggah, penundaan, dan penurunan UKT di tingkat fakultas.
  - Prosedur pendaftaran dan verifikasi berkas beasiswa KIP-Kuliah.
  - Penanganan teknis jika dana sudah terdebet tetapi status tagihan web belum lunas.

### 📁 `03_Akademik_dan_SIAKAD/` (13 File | 294.7 KB)
* **Deskripsi:** Panduan operasional sistem perkuliahan dan portal SIAKAD bagi mahasiswa baru maupun aktif.
* **Cakupan Dokumen:**
  - Panduan langkah demi langkah aktivasi akun SIAKAD pertama kali untuk mahasiswa baru.
  - Penanganan kendala login, akun terkunci, atau lupa kata sandi.
  - Aturan pengisian Kartu Rencana Studi (KRS) dan konsekuensi keterlambatan evaluasi PBM (termasuk nomor helpdesk operator tiap fakultas: FIP, FS, FMIPA, FEB, FT, FIK, FIS).
  - Prosedur pengambilan Semester Antara (pendek) dan pembatalan mata kuliah.
  - Prosedur pendaftaran yudisium online dan syarat bebas tanggungan kelulusan.
  - Alur pengambilan ijazah fisik, pembuatan surat alumni, dan legalisir ijazah.

### 📁 `04_Layanan_Kampus_dan_Sarpras/` (5 File | 82.7 KB)
* **Deskripsi:** Layanan fasilitas fisik, ketertiban lingkungan kampus, sarana prasarana, dan pengumuman umum sivitas akademika.
* **Cakupan Dokumen:**
  - Fasilitas sarana prasarana: Perpustakaan Pusat, Laboratorium Terpadu (UIL), Poliklinik/UPT Kesehatan, asrama mahasiswa, dan sarana olahraga.
  - Aturan sistem gerbang otomatis Smart Gate Parkir menggunakan KTM ber-chip RFID.
  - Prosedur penanganan kehilangan barang (KTM, helm, motor) dan alur cek CCTV kampus.
  - Fasilitas kampus inklusif ramah disabilitas (tactile paving, ramp, pendampingan khusus).
  - Panduan prosedur pengajuan kerja sama (MoU/PKS) bagi instansi mitra luar.
  - **Pengumuman Resmi Sivitas:** Pengumuman Rekrutmen Dosen dan Surat Edaran Peniadaan Car Free Day (CFD) kampus.

### 📁 `05_Helpdesk_dan_Eskalasi/` (4 File | 142 KB)
* **Deskripsi:** Kebijakan satu pintu layanan kampus, standarisasi komunikasi, dan eskalasi petugas manusia.
* **Cakupan Dokumen:**
  - Kebijakan sentralisasi **Helpdesk 1 Nomor UM (WhatsApp Terpusat: 0813-3344-400)**.
  - FAQ resmi berisi kompilasi pertanyaan umum yang paling sering diajukan sivitas akademika.
  - Jam operasional dan prosedur layanan loket administrasi Gedung Graha Rektorat Lantai 2.
  - Alur eskalasi tiket (*Human Handoff*) dari bot ke petugas manusia (*Live Agent*).

### 📁 `06_Materi_Visual_dan_Lampiran_PDF/` (5 File | 62.2 MB)
* **Deskripsi:** Dokumen visual asli dan lampiran resmi yang tetap dipertahankan dalam format PDF.
* **Cakupan Dokumen:**
  - `Transfer_Knowledge (1).pdf` (9.33 MB - diagram alur visual)
  - `Transfer_Knowledge (2)_compressed.pdf` (24.85 MB - master materi visual utuh)
  - `Transfer_Knowledge (2)_Part1 (Hal 1-128).pdf` (6.59 MB - **Dipecah agar lolos batas upload 20 MB**)
  - `Transfer_Knowledge (2)_Part2 (Hal 129-257).pdf` (18.98 MB - **Dipecah agar lolos batas upload 20 MB**)
  - `SKB_Libur_Nasional_dan_Cuti_Bersama_Tahun_2026.pdf` (1.03 MB - scan SK Menteri)

---

## ⚖️ 3. Audit & Rasionalisasi Folder Arsip (`_ARSIP_VERSI_LAMA_DAN_DUPLIKAT`)

Sebanyak **18 file** disortir ke dalam folder arsip dan **tidak diunggah ke sistem AI**. Tindakan ini dilakukan atas dasar kaidah rekayasa data AI (*AI Knowledge Engineering*) yang terukur untuk melindungi sistem dari kegagalan.

Berikut adalah tabel pembuktian mengapa setiap file memang **wajib diarsipkan**:

| No | Nama File di Arsip | Tipe Masalah | Dokumen Pengganti Resmi yang Aktif di Folder 01-05 | Alasan & Bukti Teknis Mengapa Harus Diarsipkan |
|:--:|---|:---:|---|---|
| 1 | `2) Panduan Aktifasi Akun Siakad UM untuk Mahasiswa Baru UM (1).md` | **Duplikat Persis** | `2) Panduan Aktifasi Akun Siakad UM untuk Mahasiswa Baru UM.md` (Folder 03) | **Kloningan 100% Identik (163.805 bytes).** Terbentuk akibat unduhan ganda. Jika diunggah, AI akan menyimpan dua data kembar dan memboroskan token context window. |
| 2 | `2) Panduan Siakad Mahasiswa.md` | **Duplikat Persis** | `1) Panduan Siakad Mahasiswa.md` (Folder 03) | **Kloningan 100% Identik.** Teks dan panduan sama persis, hanya berbeda angka penamaan file di awal. |
| 3 | `KB Akselerasi Internal UM.md` | **Versi Lama** | `KNOWLEDGE_BASE_ALL_PENERIMAAN_MABA (TRIASE).md` (Folder 01) | **Secara Eksplisit Tertulis Digantikan.** Di baris 3 dokumen TRIASE tertulis resmi: *"Menggantikan: KB Akselerasi Internal acuan lama"*. |
| 4 | `kb_akselerasi_internal.md` | **Versi Lama** | `KNOWLEDGE_BASE_ALL_PENERIMAAN_MABA (TRIASE).md` (Folder 01) | Draf awal akselerasi internal yang sudah digantikan oleh dokumen TRIASE mutakhir. |
| 5 | `KB_SM_Jalur_Skor_UTBK_UM.md` | **Versi Lama** | `KB_SM_Jalur_Skor_UTBK_UM  Revisi gel. 4.md` (Folder 01) | **Konflik Jadwal Gelombang.** File lama hanya mencatat Gelombang 1–3. File revisi mencatat penambahan **Gelombang 4**. Jika file lama diunggah, AI bisa salah menjawab pendaftaran sudah tutup padahal Gelombang 4 masih buka. |
| 6 | `KB_SM_Jalur_Skor_UTBK_UM (1).md` | **Versi Lama** | `KB_SM_Jalur_Skor_UTBK_UM  Revisi gel. 4.md` (Folder 01) | Salinan draf lama skor UTBK yang belum memuat jadwal Gelombang 4. |
| 7 | `KB_SM_Jalur_Skor_UTBK_UM_ Tambahan Gelombang 4.md` | **Draf Sementara** | `KB_SM_Jalur_Skor_UTBK_UM  Revisi gel. 4.md` (Folder 01) | Draf kerja transisi penambahan gelombang 4 sebelum disahkan ke naskah final revisi gel. 4. |
| 8 | `SELEKSI MANDIRI JALUR SKOR UTBK.md` | **Versi Lama** | `SELEKSI MANDIRI JALUR SKOR UTBK V4.md` (Folder 01) | Naskah pedoman awal sebelum pembaruan pedoman versi 4 (V4). |
| 9 | `SM_Jalur_Skor_UTBK_UM.md` | **Versi Lama** | `KB_SM_Jalur_Skor_UTBK_UM  Revisi gel. 4.md` (Folder 01) | Draf awal jalur skor UTBK tanpa detail penambahan gelombang. |
| 10 | `KB_SM_Magister_Reguler_UM.md` | **Versi Lama** | `KB_SM_Magister_Reguler_UM (1).md` (Folder 01) | Draf awal (7 halaman) yang telah disempurnakan dan digantikan oleh versi revisi lengkap (11 halaman). |
| 11 | `KB_SM_RPL_Magister_UM.md` | **Versi Lama** | `KB_SM_RPL_Magister_UM (1).md` (Folder 01) | **Secara Eksplisit Tertulis Digantikan.** Di halaman pembuka tertulis: *"Menggantikan: KB SM RPL Magister acuan lama"*. |
| 12 | `KB_SNBT_UM.md` | **Versi Lama** | `KB_SNBT_UM (1).md` (Folder 01) | Naskah draf awal SNBT yang telah disempurnakan pada versi mutakhir `(1)`. |
| 13 | `kb_sm_doktor_by_research.md` | **Versi Lama** | `KB SM Doktor By Research UM.md` (Folder 01) | Draf ringkas (8 halaman) yang telah digantikan oleh pedoman lengkap resmi (11 halaman). |
| 14 | `kb_sm_doktor_reguler.md` | **Versi Lama** | `KB SM Doktor Reguler UM.md` (Folder 01) | Draf ringkas (8 halaman) yang telah digantikan oleh pedoman lengkap resmi (12 halaman). |
| 15 | `KB_Registrasi_Mahasiswa_Semester_Gasal_2026_2027_UM (1).md` | **Versi Lama** | `KB_Registrasi_Mahasiswa_Semester_Gasal_2026_2027_UM (2).md` (Folder 03) | Draf awal (5 halaman) yang telah diperbarui jadwal dan alurnya pada versi final `(2)` (7 halaman). |
| 16 | `Registrasi Gasal 2026.md` | **Versi Lama** | `KB_Registrasi_Mahasiswa_Semester_Gasal_2026_2027_UM (2).md` (Folder 03) | Draf kerja awal registrasi gasal yang telah terintegrasi ke dokumen resmi versi 2. |
| 17 | `knowledge source dinamis kemahasiswaan.md` | **Versi Lama** | `knowledge source dinamis kemahasiswaan-REV 1 (2).md` (Folder 04) | Naskah draf awal (23 halaman) yang telah diperbarui secara menyeluruh pada naskah Revisi 1 (2) (24 halaman). |
| 18 | `knowledge-source_19-01-2026.md` | **Versi Lama** | `knowledge-source new.md` (Folder 03) | Naskah acuan tanggal 19 Januari 2026 yang sudah diperbarui total oleh naskah acuan "New". |

---

## 🎯 4. Kesimpulan & Rekomendasi Pelaporan ke Atasan

1. **Jaminan Integritas QA:** Folder `Knowledge_Base_Clean_Categorized/` memiliki rasio kelengkapan data **100.0% (Zero Data Loss)** dibandingkan data mentah awal. Tidak ada satu pun program studi, tarif, atau ketentuan resmi yang dihilangkan.
2. **Kesiapan Ingestion Sistem Mekari:**
   - Folder `01` sampai `05` siap diunggah langsung melalui menu **Upload file (`.md`)**.
   - Folder `06` siap diunggah melalui menu **Upload file (`.pdf`)** menggunakan file Part 1 dan Part 2 yang telah dipastikan ukurannya < 20 MB.
3. **Justifikasi Arsip:** Folder `_ARSIP_VERSI_LAMA_DAN_DUPLIKAT` **wajib dipertahankan di komputer lokal QA sebagai bukti audit**, namun **dilarang diunggah ke sistem AI** demi menjaga akurasi dan mencegah chatbot berhalusinasi jadwal lama.
