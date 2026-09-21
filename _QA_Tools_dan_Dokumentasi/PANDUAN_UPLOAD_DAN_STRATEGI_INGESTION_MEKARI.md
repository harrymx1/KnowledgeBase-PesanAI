# PANDUAN STRATEGI & TATA CARA UPLOAD KNOWLEDGE BASE KE SISTEM
## AI WhatsApp Chatbot Universitas Negeri Malang (UM)
**Dutamedia Malang — Quality Assurance & Deployment Guide**

---

## 🎯 1. Memahami 3 Metode Penambahan Knowledge di Sistem

Berdasarkan antarmuka sistem *Knowledge Ingestion* yang tersedia, terdapat **3 metode penambahan pengetahuan**:

| Tab Metode | Karakteristik & Cara Kerja Sistem | Rekomendasi Penggunaan Terbaik |
|---|---|---|
| 📝 **1. Teks / FAQ** | Sistem menjaga pasangan pertanyaan (yang diakhiri tanda tanya `?`) dan jawabannya tetap dalam **satu chunk**. Sangat cepat untuk intent matching. | **Sangat Direkomendasikan untuk:**<br>- Template jawaban sopan (`KB_Status_Aksi_Template_6Juli2026.md`)<br>- FAQ singkat (FAQ Registrasi, FAQ Smart Gate, FAQ UKT)<br>- Alur SOP penting 1-2 halaman. |
| 📁 **2. Upload File** | Menerima format `.md`, `.pdf`, `.docx`, `.txt`, `.csv` dengan batas **maksimal 20 MB per file**. File diparsing secara otomatis melalui pipeline RAG. | **Sangat Direkomendasikan untuk:**<br>- Modul-modul `.md` dari folder `Knowledge_Base_Clean_Categorized/`<br>- Dokumen pedoman panjang (Daya Tampung 2026, Biaya UKT per prodi)<br>- File visual/lampiran PDF asli (`Transfer_Knowledge (1)` dan `Transfer_Knowledge (2)`). |
| 🌐 **3. Halaman Web** | Crawler mengambil konten langsung dari URL resmi secara berkala. | **Sangat Direkomendasikan untuk:**<br>- Portal resmi yang dinamis dan sering ada pengumuman mendadak:<br>  * `https://seleksi.um.ac.id`<br>  * `https://siakad.um.ac.id`<br>  * `https://support.um.ac.id/topic/epayment/` |

---

## ⚠️ PERHATIAN KRUSIAL: Penanganan Batas File 20 MB
Pada Tab **Upload File**, sistem memberlakukan batas:
> **"Maksimal ukuran file: 20 MB"**

- Dokumen `Transfer_Knowledge (1).pdf` ukurannya **9.33 MB** (Aman / Lolos).
- Dokumen `Transfer_Knowledge (2)_compressed.pdf` ukurannya **24.85 MB** (Akan GAGAL/ERROR jika diupload utuh).
- ✅ **Solusi QA:** Kami telah membagi dokumen tersebut menjadi 2 part yang aman dan tersimpan di folder `06_Materi_Visual_dan_Lampiran_PDF/`:
  1. `Transfer_Knowledge (2)_Part1 (Hal 1-128).pdf` (Ukuran: **6.59 MB**) -> **Lolos Upload**
  2. `Transfer_Knowledge (2)_Part2 (Hal 129-257).pdf` (Ukuran: **18.98 MB**) -> **Lolos Upload**

---

## 📋 2. Panduan Pengisian Field Form Upload (Metadata Mapping Matrix)

Agar pencarian semantik AI akurat dan filter departemen berfungsi optimal, gunakan panduan pengisian field berikut:

> ⚠️ **CATATAN VALIDASI MEKARI:** Kolom **Kategori** wajib diisi 1 kata huruf kecil/slug tunggal (contoh: `pmb`, `keuangan`, `akademik`, `sarpras`, `helpdesk`). Hindari spasi atau koma karena akan memicu error sistem: *"The category field format is invalid."*

### KATEGORI 01: PMB (Penerimaan Mahasiswa Baru)
* **Pilihan Tab:** `Upload file` (pilih file `.md` dari folder `01_PMB_Penerimaan_Mahasiswa_Baru`)
* **File Utama & FAQ:** Termasuk modul `FAQ_Pendaftaran_Mandiri_dan_Kendala_Form.md`
* **Field Judul:** Gunakan nama file tanpa ekstensi (Contoh: `FAQ Pendaftaran Seleksi Mandiri dan Kendala Form`)
* **Field Kategori:** `pmb`
* **Field Department:** Pilih **`PMB`**
* **Field Owner Knowledge:** `Subdirektorat Seleksi / PMB UM`
* **Field Status:** `Active (langsung dipakai)`
* **Field Tanggal Berlaku:** Tanggal hari ini
* **Field Kedaluwarsa (Opsi Pintar):** 
  - Untuk jalur yang memiliki tanggal penutupan jelas (misal pendaftaran jalur tertentu tutup 24 Agustus), isi dengan tanggal penutupan tersebut agar dokumen otomatis nonaktif setelah lewat tanggalnya.
  - Untuk pedoman umum/daya tampung: Kosongkan (berlaku sepanjang tahun akademik).

---

### KATEGORI 02: KEUANGAN DAN BIAYA PENDIDIKAN
* **Pilihan Tab:** `Upload file` (pilih file `.md` dari folder `02_Keuangan_dan_Biaya_Pendidikan`)
* **File Utama & FAQ:** Termasuk modul `FAQ_Pembayaran_Biaya_Slip_Gaji_dan_KIPK.md`
* **Field Judul:** Contoh: `Ketentuan Biaya Pendidikan UKT dan IPI 2026` / `FAQ Pembayaran Biaya Seleksi dan Slip Gaji`
* **Field Kategori:** `keuangan`
* **Field Department:** Pilih **`Keuangan`**
* **Field Owner Knowledge:** `Direktorat Keuangan UM`
* **Field Status:** `Active (langsung dipakai)`
* **Field Tanggal Berlaku:** Tanggal hari ini
* **Field Kedaluwarsa:** Kosongkan (kebijakan tarif berlaku sepanjang tahun akademik)

---

### KATEGORI 03: AKADEMIK DAN SIAKAD
* **Pilihan Tab:** `Upload file` (pilih file `.md` dari folder `03_Akademik_dan_SIAKAD`)
* **File Utama & FAQ:** Termasuk modul `FAQ_Registrasi_Online_Maba_Lulus_Seleksi.md`
* **Field Judul:** Contoh: `Panduan Aktivasi Akun SIAKAD Mahasiswa Baru` / `FAQ Registrasi Online Mahasiswa Baru`
* **Field Kategori:** `akademik`
* **Field Department:** Pilih **`Akademik`** (atau `IT Helpdesk` untuk kendala reset password/login)
* **Field Owner Knowledge:** `Subdit Layanan Pendidikan / UPT PTIK UM`
* **Field Status:** `Active (langsung dipakai)`
* **Field Tanggal Berlaku:** Tanggal hari ini
* **Field Kedaluwarsa:** Kosongkan

---

### KATEGORI 04: LAYANAN KAMPUS DAN SARPRAS
* **Pilihan Tab:** `Upload file` (pilih file `.md` dari folder `04_Layanan_Kampus_dan_Sarpras`)
* **Field Judul:** Contoh: `Fasilitas Sarana Prasarana dan Smart Gate Parkir UM`
* **Field Kategori:** `sarpras`
* **Field Department:** Pilih **`General Service`** (atau `Kemahasiswaan` untuk kehilangan KTM/asrama)
* **Field Owner Knowledge:** `Subdirektorat Sarana Prasarana UM`
* **Field Status:** `Active (langsung dipakai)`
* **Field Tanggal Berlaku:** Tanggal hari ini
* **Field Kedaluwarsa:** Kosongkan

---

### KATEGORI 05: HELPDESK DAN ESKALASI (GLOBAL SERVICE)
* **Pilihan Tab:** Bisa menggunakan **`Upload file`** ATAU **`Teks / FAQ`** (Copy-paste konten teksnya)
* **Field Judul:** `Kebijakan Layanan Terpusat Helpdesk 1 Nomor UM`
* **Field Kategori:** `helpdesk`
* **Field Department:** Pilih **`Semua department`** (karena nomor helpdesk ini melayani lintas departemen)
* **Field Owner Knowledge:** `Pusat Layanan Terpadu UM`
* **Field Status:** `Active (langsung dipakai)`
* **Field Tanggal Berlaku:** Tanggal hari ini
* **Field Kedaluwarsa:** Kosongkan

---

### KATEGORI 06: MATERI VISUAL & LAMPIRAN PDF (DOKUMEN ASLI)
* **Pilihan Tab:** `Upload file` (pilih file PDF dari folder `06_Materi_Visual_dan_Lampiran_PDF`)
* **File yang diunggah:**
  1. `Transfer_Knowledge (1).pdf` (9.33 MB)
  2. `Transfer_Knowledge (2)_Part1 (Hal 1-128).pdf` (6.59 MB)
  3. `Transfer_Knowledge (2)_Part2 (Hal 129-257).pdf` (18.98 MB)
  4. `SKB_Libur_Nasional_dan_Cuti_Bersama_Tahun_2026.pdf` (1 MB)
* **Field Department:** `Semua department` atau `General Service`
* **Field Owner Knowledge:** `Tim Helpdesk UM / Humas`
* **Field Status:** `Active (langsung dipakai)`

---

## 🚀 3. Urutan Eksekusi Pengunggahan (Execution Roadmap)

Agar efisien dan rapi, lakukan pengunggahan dengan urutan prioritas:

```
[Tahap 1: Helpdesk 1 Nomor (Semua Department)] 
                 ↓
[Tahap 2: Keuangan & Biaya UKT/IPI]
                 ↓
[Tahap 3: PMB Penerimaan Mahasiswa Baru]
                 ↓
[Tahap 4: Akademik & SIAKAD]
                 ↓
[Tahap 5: Layanan Kampus & Sarpras]
                 ↓
[Tahap 6: Materi Visual & Lampiran PDF (Part 1 & 2)]
                 ↓
[Tahap 7: Tambahkan 2-3 URL Resmi via Tab 'Halaman web']
```

---

## 🔍 4. Verifikasi Setelah Unggah (Post-Ingestion Smoke Test)
Setelah dokumen tersimpan dan statusnya `Active`, lakukan uji coba cepat:
1. Pastikan status dokumen berubah menjadi hijau / terindeks (`indexed`).
2. Kirim pesan uji coba di simulator bot WhatsApp:
   - *"Halo Kak, berapa biaya UKT di UM?"* -> Pastikan bot merujuk ke dokumen Keuangan.
   - *"Cara aktivasi SIAKAD maba gimana ya?"* -> Pastikan bot merujuk ke panduan SIAKAD.
   - *"Nomor helpdesk UM berapa?"* -> Pastikan bot merujuk ke Helpdesk 1 Nomor (0813-3344-400).
