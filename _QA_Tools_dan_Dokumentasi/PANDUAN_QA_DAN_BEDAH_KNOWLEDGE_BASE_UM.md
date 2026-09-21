# PANDUAN AUDIT KNOWLEDGE BASE & STRATEGI QA
## AI WhatsApp Chatbot Universitas Negeri Malang (UM)
**Dutamedia Malang — Divisi Quality Assurance (QA)**

---

## 1. Ringkasan Eksekutif & Hasil Audit File
Dari ekstraksi data di direktori proyek, terdapat total **98 file PDF** dengan rincian persebaran folder:
- **Root**: 12 file (Pengumuman umum, sarpras, SKB libur, helpdesk, dan file transfer knowledge gabungan).
- **Folder `Informasi Penerimaan Maba`**: 68 file (Jalur SNBP, SNBT, Seleksi Mandiri berbagai jalur, regulasi, template aksi).
- **Folder `Registrasi UKT dan KRS`**: 12 file (Biaya UKT, IPI, panduan bayar, loket layanan, semester antara).
- **Folder `Panduan Siakad`**: 6 file (Aktivasi akun Siakad, panduan mahasiswa).

---

## 2. Temuan Kritis (Critical Findings) untuk QA & Tim Dev

### ⚠️ Temuan 1: Tumpang Tindih Dokumen & Konflik Versi (Version Conflict)
Banyak file memiliki beberapa versi revisi dan gelombang pendaftaran yang tersimpan bersamaan di folder. Jika seluruh file ini diunggah mentah-mentah ke Mekari AI, mesin RAG (Retrieval-Augmented Generation) akan membaca dua informasi yang kontradiktif dan berpotensi memicu **halusinasi** atau memberikan informasi lama.

**Contoh Kasus Nyata di Folder:**
1. **Seleksi Mandiri Jalur Skor UTBK (Ada 5 file bertumpuk):**
   - `KB_SM_Jalur_Skor_UTBK_UM.pdf` (versi awal)
   - `KB_SM_Jalur_Skor_UTBK_UM+(1).pdf`
   - `KB_SM_Jalur_Skor_UTBK_UM++Revisi+gel.+4.pdf`
   - `KB_SM_Jalur_Skor_UTBK_UM_+Tambahan+Gelombang+4.pdf`
   - `SELEKSI+MANDIRI+JALUR+SKOR+UTBK+V4.pdf`
   *-> Rekomendasi QA:* **Hanya pakai file revisi paling mutakhir (Gelombang 4)**. File lama wajib diarsipkan/dikeluarkan dari dataset upload!
2. **Akselerasi Internal (Fast Track):**
   - `KB+Akselerasi+Internal+UM.pdf` vs `kb_akselerasi_internal.pdf` vs `KNOWLEDGE_BASE_ALL_PENERIMAAN_MABA (TRIASE).pdf` (di halaman 1 tertulis jelas: *Menggantikan KB Akselerasi Internal acuan lama*).
3. **Magister RPL:**
   - `KB_SM_RPL_Magister_UM.pdf` vs `KB_SM_RPL_Magister_UM+(1).pdf` (tertulis eksplisit: *Menggantikan versi acuan lama*).
4. **Panduan SIAKAD:**
   - Terdapat duplikat identik: `2) Panduan Aktifasi Akun Siakad UM untuk Mahasiswa Baru UM (1).pdf` dan `2) Panduan Aktifasi Akun Siakad UM untuk Mahasiswa Baru UM.pdf`.

---

### ⚠️ Temuan 2: Dokumen Berbahaya / Noise (Out of Scope / Kadaluwarsa)
Terdapat file-file yang bukan merupakan pengetahuan inti calon mahasiswa baru atau sudah kedaluwarsa. Mengunggahnya akan mengotori knowledge base (*Knowledge Pollution*):
1. `Pengumuman+Penerimaan+Dosen+20+Februari+-++7+April+2026..pdf`: Ini rekrutmen dosen, tanggalnya sudah lewat, dan sasarannya pelamar kerja, bukan mahasiswa.
2. `Peniadaan+Car+Free+Day.pdf`: Pengumuman insidental/lokal non-akademik.
3. `SKB_Libur_Nasional_dan_Cuti_Bersama_Tahun_2026.pdf`: Scanned image (tidak terbaca teks OCR) dan tidak relevan dimasukkan sebagai KB utama chatbot.

---

### ⚠️ Temuan 3: Jebakan "Tanggal Acuan Statis" (Time-Sensitivity Risk)
Pada dokumen `KB_Status_Aksi_Template_6Juli2026.pdf`, knowledge disusun dengan konteks:
> *"PER TANGGAL ACUAN: 6 JULI 2026"*
- Dokumen ini menyatakan: *Jalur Prestasi tutup sejak 11 Juni, Jalur UTBK sedang buka, Pengumuman Periode Tiga akan datang 7 Juli*, dll.
- **Risiko QA:** Chatbot LLM tidak tahu hari ini tanggal berapa jika sistem Mekari Qontak tidak menyuntikkan *system time/date context*. Jika bot menganggap hari ini selalu 6 Juli 2026, maka saat mahasiswa bertanya di bulan Agustus atau September, bot akan tetap menjawab dengan status per 6 Juli!

---

## 3. Pemetaan 4 Klaster Knowledge Base

| Klaster | Cakupan Topik Utama | Dokumen Acuan Terbaik (Prioritas Upload) |
|---|---|---|
| **Klaster 1: Penerimaan Mahasiswa Baru (PMB)** | - SNBP & SNBT<br>- Seleksi Mandiri S1/D4: Prestasi, Skor UTBK (Gel. 1-4), TMBK, Kemitraan, Leadership, Kelas Internasional.<br>- Pascasarjana: S2 Reguler, S2 PJJ, Fast-Track/Akselerasi, RPL, S3 By Research/Reguler. | - `KNOWLEDGE_BASE_ALL_PENERIMAAN_MABA (TRIASE).pdf`<br>- `KB_Jalur_Pendaftaran_SM_2026+(revisi).pdf`<br>- `KB_Status_Aksi_Template_6Juli2026.pdf`<br>- `DAYA+TAMPUNG+PROGRAM+STUDI+&+JADWAL+SELEKSI+MABA+UM+2026.pdf` |
| **Klaster 2: Registrasi, UKT, dan Keuangan** | - Tata cara pembayaran UKT & IPI per jalur.<br>- Prosedur sanggah/penurunan UKT.<br>- Mekanisme registrasi online & offline.<br>- KIP-Kuliah dan beasiswa. | - `Registrasi UKT dan KRS/KB_Biaya_UKT_IPI_Pembayaran.pdf`<br>- `Registrasi UKT dan KRS/KB_Registrasi_Mahasiswa_Semester_Gasal_2026_2027_UM+(2).pdf`<br>- `Informasi Penerimaan Maba/KB+Penurunan+dan+Penarikan+UKT.pdf`<br>- `KB_FAQ_Umum_KIP_Prosedur.pdf` |
| **Klaster 3: Akademik, SIAKAD, dan KRS** | - Aktivasi akun SIAKAD pertama kali.<br>- Pengisian KRS, evaluasi PBM.<br>- Semester Antara/Pendek.<br>- Kendala login / lupa akun. | - `Registrasi UKT dan KRS/KB_Registrasi_Akun_SIAKAD_DaftarUlang.pdf`<br>- `Panduan Siakad/1) Panduan Siakad Mahasiswa.pdf`<br>- `Panduan Siakad/3) Panduan Aktifasi Akun Siakad UM untuk Mahasiswa Baru UM.pdf` |
| **Klaster 4: Layanan Kampus & Helpdesk Terpusat** | - Kebijakan Helpdesk 1 Nomor UM.<br>- Fasilitas umum, sarana & prasarana, parkir gate, kehilangan barang.<br>- Pengajuan kerja sama. | - `Helpdesk+1+Nomor.pdf`<br>- `Sarana+Prasarana+UM.pdf`<br>- `KNOWLEDGE+BASE+PANDUAN+PENGAJUAN+KERJA+SAMA+DI+UNIVERSITAS+NEGERI+MALANG+(REV).pdf`<br>- `FAQ+_+INFORMASI+DAFTAR+PERTANYAAN+UMUM+YANG+SERING+DISAMPAIKAN.pdf` |

---

## 4. Bahan Diskusi Teknis QA dengan Tim Developer

Sebelum proses upload knowledge base ke Mekari Qontak dimulai, diskusikan poin-poin berikut dengan Tim Dev:

### 1. Persona & Tone of Voice Chatbot
- Sapaan resmi: Gunakan *"Kak / Halo Kak"* (sesuai standar WhatsApp UM).
- Gaya bahasa: Santun, ramah, solutif, tidak kaku, namun tetap formal akademis.
- Batasan panjang jawaban: Maksimal 2–3 paragraf ringkas di WhatsApp dengan bullet points agar tidak melelahkan dibaca di layar HP.
- Penyertaan Link Resmi: Setiap informasi penting wajib menyertakan link portal resmi (contoh: `seleksi.um.ac.id`, `siakad.um.ac.id`).

### 2. Guardrails (Batasan Pengetahuan) & Out-of-Scope (OOS)
- **Tanya tugas/skripsi:** Bot dilarang mengerjakan tugas kuliah mahasiswa (*"Maaf Kak, bot layanan ini hanya membantu informasi seputar administrasi dan perkuliahan di UM..."*).
- **Tanya hal sensitif / politik / SARA / kampus lain:** Bot harus netral dan mengarahkan kembali ke topik layanan UM.
- **Tanya hal yang tidak ada di dokumen:** Bot dilarang mengarang/halusinasi. Jika tidak ada di KB, gunakan *Standard Fallback*.

### 3. Fallback Mechanism & Handoff to Live Agent
- Karena UM menerapkan kebijakan **Helpdesk 1 Nomor**, jika bot tidak memahami pertanyaan atau pertanyaan membutuhkan penanganan data pribadi (misal: NIM terblokir, bukti transfer bermasalah), bot harus memberikan eskalasi:
  > *"Untuk kendala verifikasi data pribadi atau kendala sistem, silakan hubungi Helpdesk Terpusat UM melalui WhatsApp: [Nomor Resmi Helpdesk UM] pada jam kerja operasional."*

### 4. Penanganan Tanggal Dinamis (Dynamic Date Injection)
- Minta Tim Dev memastikan System Prompt Mekari Qontak menyertakan tag variabel tanggal hari ini (misal: `{{current_date}}`), sehingga bot tahu apakah suatu jalur seleksi saat ini sedang dibuka atau sudah lewat.

---

## 5. Matriks Skenario Pengujian QA (UAT Internal & SIT)

| Kategori Pengujian | ID Test | Skenario Uji (Prompt Input Pengguna) | Ekspektasi Hasil (Expected Output) |
|---|---|---|---|
| **Happy Path (Informasi Jalur)** | TC-01 | *"Kak, pendaftaran jalur skor UTBK masih buka ga?"* | Bot menjelaskan jadwal gelombang aktif, syarat, biaya, dan link `seleksi.um.ac.id`. |
| **Happy Path (UKT & Biaya)** | TC-02 | *"Berapa biaya UKT untuk jurusan Teknik Informatika jalur mandiri?"* | Bot memberikan kisaran/kategori UKT dan IPI serta mengarahkan ke tabel biaya resmi. |
| **Happy Path (SIAKAD)** | TC-03 | *"Saya maba, cara aktivasi akun SIAKAD gimana ya?"* | Bot memberikan langkah runtut: buka siakad.um.ac.id, masukkan nomor peserta/NIM, buat password, dll. |
| **Skenario Batas Waktu (Closed)** | TC-04 | *"Saya mau daftar Jalur Prestasi sekarang bisa?"* | Bot menolak dengan sopan: *"Mohon maaf Kak, pendaftaran Jalur Prestasi telah ditutup pada [tanggal]. Namun saat ini Kakak bisa mengikuti jalur [jalur lain yang buka]..."* |
| **Edge Case (Typo & Slang)** | TC-05 | *"klo byar ukt telat gmna slur? bs minta keringanan ga"* | Bot mengenali intent pembayaran UKT terlambat / pengajuan penundaan atau penurunan UKT sesuai SOP. |
| **Guardrail (Out of Scope)** | TC-06 | *"Bikinin rangkuman materi kalkulus bab 1 dong"* | Bot menolak dengan sopan karena di luar kewenangan helpdesk administrasi kampus. |
| **Anti-Halusinasi** | TC-07 | *"Apakah UM membuka jurusan Kedokteran Nuklir tahun ini?"* | Bot memeriksa KB; jika tidak ada, bot menyatakan prodi tersebut belum tersedia di UM dan memberikan link daftar prodi resmi. |
| **Eskalasi / Human Handoff** | TC-08 | *"Saya sudah bayar UKT tapi status di web masih belum lunas, tolong bantu!"* | Bot memberikan langkah pengecekan mutasi bank dan langsung memberikan kontak Helpdesk 1 Nomor UM untuk konfirmasi bukti bayar. |
