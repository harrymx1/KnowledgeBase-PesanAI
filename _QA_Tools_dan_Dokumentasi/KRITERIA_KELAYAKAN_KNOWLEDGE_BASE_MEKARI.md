# STANDAR OPERASIONAL & KRITERIA KELAYAKAN KNOWLEDGE BASE
## AI WhatsApp Chatbot Universitas Negeri Malang (UM)
**Dutamedia Malang — Quality Assurance & Project Delivery Standard**

---

## 🎯 Ringkasan Eksekutif
Dalam implementasi Generative AI Chatbot (berbasis RAG - Retrieval-Augmented Generation pada platform Mekari Qontak), **kualitas Knowledge Base menentukan 90% keberhasilan proyek**. Chatbot tidak akan pernah bisa menjawab lebih pintar daripada kualitas dokumen yang disuntikkan ke dalamnya (*Garbage In, Garbage Out*).

Dokumen ini memuat **6 Pilar Kriteria Kelayakan Mutlak** yang harus lolos uji (*QA Gate Passed*) sebelum Knowledge Base dinyatakan layak untuk diunggah dan digunakan di sistem produksi.

---

## 🏛️ 6 PILAR KRITERIA KELAYAKAN KNOWLEDGE BASE

### PILAR 1: Integritas & Kebenaran Data (Accuracy & Single Source of Truth)
*Risiko jika gagal: Bot memberikan jadwal yang salah, tarif UKT keliru, atau informasi yang sudah kedaluwarsa, yang dapat memicu tuntutan hukum dan komplain publik.*

1. **Prinsip Single Source of Truth (SSOT):**
   - Tidak boleh ada 2 dokumen yang memuat data bertentangan untuk topik yang sama.
   - Hanya versi revisi final yang dimasukkan. Seluruh draf lama (Gelombang 1, 2, revisi parsial) wajib dieliminasi.
2. **Pemisahan Data Statis vs Dinamis (Time-Sensitivity):**
   - Data statis: Visi-misi, fakultas/prodi, alur aktivasi SIAKAD, SOP kerja sama.
   - Data dinamis: Tanggal buka/tutup pendaftaran, gelombang seleksi, batas bayar UKT.
   - *Syarat Kelayakan:* Informasi dinamis harus mencantumkan tanggal acuan yang jelas dan tidak boleh menggunakan kata relatif ("besok", "minggu depan") tanpa tanggal eksplisit.
3. **Akurasi Angka Finansial:**
   - Besaran UKT (Kelompok 1 s.d. 7) dan sumbangan IPI per prodi harus terverifikasi 100% sesuai SK Rektor terbaru.
   - Masa aktif kode bayar bank wajib seragam dinyatakan berlaku **48 jam**.

---

### PILAR 2: Optimasi Arsitektur RAG & Chunking (Machine Readability)
*Risiko jika gagal: Mesin pencari semantik Mekari gagal mengambil bagian teks yang tepat, atau context window LLM terpotong sehingga bot menjawab tidak lengkap.*

1. **Atomicity (Satu Dokumen, Satu Fokus Topik):**
   - Panjang ideal per dokumen adalah **300 hingga 1.500 kata**.
   - Dilarang mengunggah dokumen monolitik (50-100 halaman) yang mencampur topik pendaftaran, UKT, dan fasilitas dalam satu file.
2. **Transformasi Tabel Menjadi Prosa Deskriptif:**
   - AI Chatbot WhatsApp sering mengalami disorientasi saat membaca tabel baris-kolom yang kompleks.
   - *Syarat Kelayakan:* Tabel tarif atau prodi harus dinarasikan secara terstruktur (menggunakan heading dan bullet points per prodi/kelompok biaya).
3. **Struktur Heading Semantik yang Jelas:**
   - Hirarki judul wajib konsisten: `# Judul Utama`, `## Sub-Bab`, `### Pertanyaan/Poin Spesifik`.
   - Hindari teks dekoratif yang tidak memiliki makna semantik.

---

### PILAR 3: Kelengkapan Semantik & Query Coverage (Retrieval Match)
*Risiko jika gagal: Bot menjawab "Maaf saya tidak tahu" hanya karena pengguna menggunakan istilah yang berbeda dari bahasa resmi kampus.*

1. **Penyelarasan Istilah Resmi vs Bahasa Lapangan (Glosarium & Sinonim):**
   - "IPI" harus diselaraskan dengan "Uang Gedung / Uang Pangkal / SPI".
   - "UKT" harus diselaraskan dengan "SPP / Biaya Kuliah / Uang Semester".
   - "Fast Track" harus diselaraskan dengan "Akselerasi".
   - "SIAKAD" harus diselaraskan dengan "Web KRS / Portal Nilai".
2. **Pasangan Tanya Jawab (Q&A Pairs) Realistis:**
   - Setiap dokumen modul wajib menyertakan minimal 2–5 pasang Q&A yang merefleksikan pertanyaan riil calon mahasiswa.
3. **Tautan Valid & Kontak Terverifikasi:**
   - Seluruh URL rujukan wajib aktif (`https://seleksi.um.ac.id`, `https://siakad.um.ac.id`, `https://support.um.ac.id`).
   - Tidak boleh mencantumkan nomor handphone pribadi pegawai. Semua kontak wajib mengarah ke **Helpdesk 1 Nomor UM (0813-3344-400)**.

---

### PILAR 4: Batasan Keamanan & Guardrails (Out-of-Scope Control)
*Risiko jika gagal: Bot disalahgunakan mahasiswa untuk mengerjakan tugas, berhalusinasi tentang kampus lain, atau memicu isu reputasi.*

1. **Batasan Pengetahuan Tegas (Defensive Boundaries):**
   - Bot dilarang menjawab pertanyaan non-akademik UM (politik, agama, opini pribadi, isu kampus luar).
   - Bot dilarang membuatkan esai, makalah, atau jawaban kuis kuliah.
2. **Pencegahan Halusinasi Prodi/Jalur Fiktif:**
   - Jika calon mahasiswa menanyakan jurusan yang tidak ada di UM (misal: Kedokteran Gigi, Teknik Perkapalan), bot harus secara eksplisit menyatakan prodi tersebut belum dibuka di UM dan memberikan link daftar prodi resmi.
3. **Kepatuhan Privasi Data (UU PDP):**
   - Knowledge base tidak boleh menyimpan data identitas pribadi (NIK, password default akun, bukti transfer perorangan).

---

### PILAR 5: Kesesuaian Format Layanan WhatsApp (Conversational UI/UX)
*Risiko jika gagal: Pengguna malas membaca karena chat terlalu panjang dan kaku, atau merasa ditolak secara kasar oleh bot.*

1. **Panjang Jawaban Ideal (Brevity):**
   - Jawaban bot di WhatsApp idealnya **maksimal 2–3 paragraf pendek** (sekitar 50–120 kata per pesan) dengan penggunaan bullet points agar mudah dibaca di layar HP.
2. **Persona & Tone of Voice Helpdesk UM:**
   - Sapaan wajib ramah menggunakan **"Halo Kak / Kak"**.
   - Gaya bahasa: Sopan, solutif, empatik, dan tetap profesional akademis.
3. **Larangan Jawaban Menolak Kaku:**
   - Dilarang keras menjawab: *"Tidak bisa"*, *"Sudah tutup"*, atau *"Bukan urusan kami"*.
   - Wajib menggunakan kalimat pembungkus:
     > *"Mohon maaf, Kak. Berdasarkan jadwal resmi, kegiatan tersebut sudah ditutup per [tanggal]. Namun Kakak bisa mengikuti [jalur/solusi lain]..."*

---

### PILAR 6: Jalur Eskalasi & Handover yang Jelas (Human-in-the-Loop)
*Risiko jika gagal: Kasus darurat (uang kuliah tertelan mesin ATM, akun terblokir jelang penutupan KRS) terabaikan dan berujung komplain fatal ke rektorat.*

1. **Trigger Eskalasi Terdefinisi Jelas:**
   - Pertanyaan yang melibatkan transaksi keuangan yang menggantung.
   - Kasus akun SIAKAD terkunci yang butuh verifikasi identitas resmi.
   - Kasus banding/keringanan UKT yang memerlukan keputusan dekanat.
2. **Informasi Alur Layanan Fisik/Loket:**
   - Lokasi: Gedung Graha Rektorat Lantai 2 (Subdirektorat Layanan Pendidikan).
   - Jam Layanan: Senin – Jumat pukul 07.30 – 16.00 WIB.
   - WhatsApp Sentral: 0813-3344-400.

---

## 📊 CHECKLIST VERIFIKASI SEBELUM UPLOAD (QA GATEWAY)

| No | Parameter Pemeriksaan | Standar Kelayakan | Status |
|:--:|---|---|:--:|
| 1 | **Format File** | Markdown (`.md`) bersih, UTF-8 tanpa karakter surrogate aneh | ✅ Lolos |
| 2 | **Struktur Modul** | Terbagi ke dalam 5 Kategori resmi (PMB, Keuangan, SIAKAD, Sarpras, Helpdesk) | ✅ Lolos |
| 3 | **Deduplikasi Versi** | Tidak ada file draft/versi lama yang saling bertentangan | ✅ Lolos |
| 4 | **Pembersihan Noise** | File out-of-scope (penerimaan dosen lama, CFD, SKB libur scan) disingkirkan | ✅ Lolos |
| 5 | **Kohesi Ukuran Dokumen** | File modular rata-rata 300 - 1.500 kata (Atomic Knowledge) | ✅ Lolos |
| 6 | **Struktur Heading & Q&A** | Dilengkapi ringkasan, ketentuan, langkah urut, dan pasangan FAQ | ✅ Lolos |
| 7 | **Verifikasi Tautan & Kontak** | Tautan resmi `um.ac.id` aktif & rujukan terpusat ke Helpdesk 1 Nomor | ✅ Lolos |
| 8 | **Guardrails & Eskalasi** | Memuat instruksi fallback jika data tidak ditemukan | ✅ Lolos |
