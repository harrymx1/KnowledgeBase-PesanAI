import os
import shutil

src_dir = r"Knowledge_Base_Clean_Categorized/03_Akademik_dan_SIAKAD"
archive_dir = r"Knowledge_Base_Clean_Categorized/_ARSIP_VERSI_LAMA_DAN_DUPLIKAT"
os.makedirs(archive_dir, exist_ok=True)

print("Starting Subfolder 3 Standardization...")

# ==========================================
# 1. Panduan_Aktivasi_Akun_SIAKAD_Mahasiswa_Baru.md
# ==========================================
doc_aktivasi = """# Panduan Aktivasi Akun SIAKAD dan Login Mahasiswa Baru Universitas Negeri Malang

> **Kategori:** `akademik`  
> **Department:** `Akademik`  
> **Target Pengguna:** Mahasiswa Baru (Maba) Universitas Negeri Malang (UM)  
> **Status:** Resmi Aktif  

---

## 1. Alur Mendapatkan NIM dan Aktivasi Akun SIAKAD

### Bagaimana cara mendapatkan Nomor Induk Mahasiswa (NIM) bagi mahasiswa baru UM?
Nomor Induk Mahasiswa (NIM) yang terdiri dari **12 digit angka** diterbitkan secara otomatis oleh sistem setelah calon mahasiswa baru menyelesaikan pembayaran UKT:
1. Selesaikan pembayaran UKT menggunakan Kode Bayar di bank mitra resmi UM.
2. Login kembali ke portal registrasi: https://registrasiv4.um.ac.id/.
3. Unduh dan cetak **Formulir Biodata** atau **Bukti Registrasi Online**.
4. NIM (12 digit) tertera secara jelas di bagian atas dokumen bukti registrasi tersebut.
*(Catatan: Jika baru saja membayar, tunggu proses sinkronisasi perbankan sekitar 1 hingga 3 jam).*

### Bagaimana cara mengaktifkan akun SIAKAD untuk pertama kali?
Aktivasi akun SIAKAD dilakukan setelah proses registrasi online di portal registrasi selesai:
1. Lengkapi seluruh pengisian data dan unggah berkas di portal https://registrasiv4.um.ac.id/ hingga seluruh tab berstatus centang hijau.
2. Pada halaman akhir ringkasan pendaftaran, klik tombol bertuliskan **"Buat Akun Siakad"**.
3. Sistem akademik UM akan memproses pembuatan akun SIAKAD secara otomatis.
*(Jika tombol "Buat Akun Siakad" belum muncul, periksa kembali seluruh tab pengisian data karena ada berkas atau isian wajib yang belum tersimpan).*

---

## 2. Cara Mendapatkan Password & Prosedur Login SIAKAD

### Bagaimana cara mendapatkan password login SIAKAD untuk mahasiswa baru?
Detail login (NIM dan Password) diperoleh melalui 2 opsi:
- **Opsi A (Email Otomatis):** Cek kotak masuk (*Inbox*) atau folder *Spam/Promotions* pada alamat email pribadi yang didaftarkan saat registrasi online. Sistem mengirimkan kredensial akun secara otomatis setelah tombol buat akun diklik.
- **Opsi B (Reset Mandiri via Fitur Lupa Kata Sandi):** Jika email belum diterima dalam waktu 1x24 jam:
  1. Buka laman portal akademik: https://siakad.um.ac.id/.
  2. Klik tautan **"Lupa kata sandi?"** di bawah tombol login.
  3. Masukkan 12 digit NIM Anda.
  4. Buka link pemulihan yang masuk ke email terdaftar untuk membuat password baru.

### Bagaimana langkah login ke SIAKAD UM untuk mahasiswa baru?
Langkah-langkah login ke SIAKAD UM:
1. Buka peramban dan akses portal resmi: https://siakad.um.ac.id/.
2. Masukkan **12 digit NIM** pada kolom *Username*.
3. Masukkan **Password** (dari email atau hasil reset kata sandi).
4. Ketikkan kode angka/huruf **Captcha** yang muncul di layar dengan benar.
5. Klik **Login**.
*(Demi keamanan akun, segera ganti password default setelah berhasil login pertama kali).*

---

## 3. Penanganan Masalah Teknis Login & Akun SIAKAD

### Bagaimana jika muncul error 'Username atau Password Salah' saat login SIAKAD?
Langkah pengecekan:
1. Pastikan NIM yang diketikkan tepat berjumlah 12 digit angka tanpa spasi.
2. Pastikan tidak ada spasi tambahan di awal atau di akhir password (terutama jika disalin/copy-paste dari email).
3. Jika tetap gagal, gunakan fitur **"Lupa kata sandi?"** di laman https://siakad.um.ac.id/ untuk mengatur ulang password baru.

### Bagaimana jika email pendaftaran salah ketik atau tidak aktif saat aktivasi SIAKAD?
Jika email yang terdaftar salah atau tidak dapat diakses sehingga link aktivasi tidak masuk:
- Mahasiswa wajib melakukan verifikasi dan pembaruan email ke **Subag Registrasi & Statistik, Gedung Graha Rektorat Lantai 2 UM**, atau
- Mengajukan tiket permohonan pembaruan email melalui helpdesk resmi UPT TIK UM dengan melampirkan foto KTP, KTM sementara, dan bukti registrasi online resmi.

### Bagaimana jika captcha selalu salah atau gambar captcha tidak muncul?
Solusi kendala captcha di SIAKAD:
1. Muat ulang (*refresh*) halaman peramban web Anda.
2. Buka web SIAKAD menggunakan mode penyamaran (*Incognito Window / Private Browsing*).
3. Hapus data penjelajahan (*cache & cookies*) pada browser.

### Bagaimana jika halaman SIAKAD berwarna putih/blank atau mengalami Error 500?
Halaman putih atau error server 500 biasanya terjadi ketika lonjakan trafik sangat tinggi (misalnya saat hari pertama pengisian KRS serentak). Silakan coba akses kembali secara berkala di luar jam sibuk (malam atau pagi hari).

---

## Tautan Resmi & Kontak Layanan Bantuan SIAKAD
- **Portal SIAKAD UM:** https://siakad.um.ac.id/
- **Portal Registrasi Mahasiswa Baru:** https://registrasiv4.um.ac.id/
- **Layanan Data Mahasiswa & NIM:** Subag Registrasi, Gedung Graha Rektorat Lantai 2 UM
- **Helpdesk UPT TIK UM:** https://support.um.ac.id/
- **Helpdesk Terpusat UM:** WhatsApp **0822-1333-4445** (Senin–Jumat pukul 07.30–16.00 WIB)
"""

# ==========================================
# 2. Panduan_Registrasi_Akun_SIAKAD_dan_Daftar_Ulang.md
# ==========================================
doc_daftar_ulang = """# Panduan Registrasi Akun SIAKAD, Daftar Ulang & Kendala Teknis Website

> **Kategori:** `akademik`  
> **Department:** `Akademik`  
> **Target Pengguna:** Calon Mahasiswa Baru & Mahasiswa Universitas Negeri Malang (UM)  
> **Status:** Resmi Aktif  

---

## 1. Daftar Istilah & Glosarium Akademik UM
- **SIAKAD:** Sistem Informasi Akademik UM (https://siakad.um.ac.id) — portal akademik mahasiswa aktif untuk pengisian KRS, melihat KHS/transkrip nilai, jadwal kuliah, dan bimbingan tugas akhir.
- **registrasiv4.um.ac.id:** Portal resmi pengisian biodata, unggah berkas, dan penentuan UKT mahasiswa baru sebelum aktif di SIAKAD.
- **SKL (Surat Keterangan Lulus):** Dokumen resmi pengganti ijazah sementara bagi calon mahasiswa yang ijazah aslinya belum diterbitkan sekolah.
- **UKBIng (Uji Kemampuan Berbahasa Inggris):** Tes kemampuan bahasa Inggris wajib bagi mahasiswa baru UM yang jadwal dan kartunya diunduh via SIAKAD.
- **Registrasi Satu Atap:** Sesi verifikasi fisik berkas asli secara tatap muka di Gedung Graha Cakrawala UM setelah menyelesaikan seluruh registrasi online.

---

## 2. Alur Lengkap Registrasi Online & Daftar Ulang Mahasiswa Baru

### Bagaimana alur lengkap pendaftaran ulang mahasiswa baru di Universitas Negeri Malang?
Tahapan daftar ulang mahasiswa baru seluruh jalur masuk (SNBP, SNBT, dan Mandiri):
1. **Buat Akun & Isi Biodata:** Akses https://registrasiv4.um.ac.id/ menggunakan Nomor Peserta seleksi resmi.
2. **Unggah Berkas Registrasi:** Unggah hasil scan dokumen asli berwarna:
   - Ijazah asli atau Surat Keterangan Lulus (SKL) resmi.
   - Kartu Keluarga (KK) dan Akta Kelahiran asli.
   - Surat Keterangan Penghasilan / Slip Gaji orang tua yang disahkan.
   - Foto rumah tampak depan, ruang tamu, dan dapur (disarankan menggunakan aplikasi GPS Camera).
   - Bukti bayar PBB, bukti rekening listrik/token, dan bukti rekening air PDAM/surat sumur non-PDAM.
   - Surat Pernyataan Mahasiswa (SPM) bermeterai Rp10.000.
   - Pasfoto resmi (ukuran 4x6 cm, format JPG/JPEG maks. 200 KB, latar belakang merah, kemeja putih polos berkerah, tanpa kacamata).
3. **Cek Penetapan UKT:** Lihat hasil pengumuman kategori tarif UKT pada laman registrasi online.
4. **Pembayaran Biaya Pendidikan:** Bayar UKT (dan IPI bagi jalur mandiri) menggunakan Kode Bayar unik di bank mitra resmi UM.
5. **Registrasi Satu Atap (Fisik):** Hadir ke Gedung Graha Cakrawala UM sesuai jadwal dengan membawa berkas asli dan cetak formulir registrasi.
6. **Pelaksanaan UKBIng:** Unduh jadwal dan kartu tes kemampuan bahasa Inggris melalui portal SIAKAD.

---

## 3. Penanganan Masalah & Kendala Teknis Registrasi Online

### Mengapa calon mahasiswa tidak bisa membuat akun registrasi online?
Penyebab dan solusi kendala pembuatan akun registrasi:
- **Jadwal Belum Dibuka:** Pastikan jadwal registrasi online untuk jalur masuk Anda sudah dimulai sesuai tanggal di kalender seleksi resmi.
- **Salah Format Nomor Peserta:** Pastikan nomor peserta yang dimasukkan sesuai dengan kartu tanda peserta seleksi (SNBP, SNBT, atau Seleksi Mandiri).
- **Status Kelulusan:** Pastikan nomor peserta yang dimasukkan dinyatakan LULUS pada pengumuman resmi di https://seleksi.um.ac.id/.

### Mengapa unggah berkas di portal registrasi online selalu gagal?
Ketentuan teknis agar unggahan berkas berhasil:
1. **Ukuran File:** Ukuran file dokumen tidak boleh melebihi batas maksimal **200 KB per file** (atau maksimal 2 MB jika ketentuan khusus PDF). Kompres file terlebih dahulu jika ukurannya terlalu besar.
2. **Format File:** Gunakan format **JPG atau JPEG** (atau PDF jika diminta secara khusus).
3. **Nama File:** Gunakan nama file yang sederhana (hanya huruf dan angka tanpa karakter khusus seperti `/`, `\`, `&`, `@`, tanda kutip, atau spasi berlebih).
4. **Peramban:** Gunakan Google Chrome atau Mozilla Firefox terbaru pada laptop/PC dengan koneksi internet yang stabil.

### Bagaimana jika data registrasi online salah setelah disimpan permanen?
Data biodata yang sudah disimpan permanen tidak dapat diubah secara mandiri oleh calon mahasiswa. Pemohon harus membawa dokumen bukti asli pendukung saat pelaksanaan verifikasi berkas Registrasi Satu Atap di kampus untuk diperbaiki oleh petugas verifikator akademik.

---

## Tautan Resmi & Layanan Registrasi
- **Portal Registrasi Online UM:** https://registrasiv4.um.ac.id/
- **Panduan e-Payment UM:** https://support.um.ac.id/topic/epayment/
- **Portal Akademik SIAKAD:** https://siakad.um.ac.id/
- **Helpdesk Registrasi Mahasiswa Baru:** WhatsApp **0813-3344-400**
- **Helpdesk Terpusat UM:** WhatsApp **0822-1333-4445**
"""

# ==========================================
# 3. Panduan_Penggunaan_Fitur_SIAKAD_Mahasiswa_Aktif.md
# ==========================================
doc_fitur_siakad = """# Panduan Penggunaan Fitur SIAKAD untuk Mahasiswa Aktif Universitas Negeri Malang

> **Kategori:** `akademik`  
> **Department:** `Akademik`  
> **Target Pengguna:** Mahasiswa Aktif Universitas Negeri Malang (UM)  
> **Status:** Resmi Aktif  

---

## 1. Dashboard & Navigasi Utama SIAKAD
Halaman Dashboard SIAKAD (https://siakad.um.ac.id/) merupakan tampilan utama setelah login yang memuat:
- **Profil Mahasiswa:** Nama lengkap, NIM, Program Studi, Fakultas, dan nama Dosen Pembimbing Akademik (PA).
- **Ringkasan Status Perkuliahan:** Status registrasi semester berjalan (Aktif/Cuti/Non-Aktif).
- **Grafik Perkembangan Studi:** Riwayat perolehan Indeks Prestasi Semester (IPS) dan Indeks Prestasi Kumulatif (IPK).
- **Pemberitahuan & Pengumuman Kampus:** Informasi kalender akademik dan agenda penting universitas.

---

## 2. Pengisian Rencana Studi (KRS Online)

### Bagaimana tata cara pengisian KRS online bagi mahasiswa aktif di SIAKAD UM?
Langkah-langkah pengisian Kartu Rencana Studi (KRS):
1. Buka laman https://siakad.um.ac.id/ dan lakukan login menggunakan NIM dan password Anda.
2. Masuk ke menu **Akademik** > pilih submenu **Rencana Studi**.
3. Klik tombol **"Tambah Mata Kuliah"** untuk melihat daftar sajian mata kuliah pada semester berjalan.
4. Pilih mata kuliah dan kelas yang diinginkan sesuai dengan kurikulum program studi dan jadwal kuliah Anda.
5. Klik **"Ambil"** pada mata kuliah yang dipilih, lalu periksa agar tidak terjadi jadwal bentrok antar-mata kuliah.
6. Klik **"Simpan KRS"** untuk menyimpan rencana studi Anda.
7. Lakukan konsultasi dan ajukan persetujuan pengesahan KRS kepada **Dosen Pembimbing Akademik (Dosen PA)**.

### Berapa batas maksimal SKS yang dapat diambil dalam pengisian KRS?
Ketentuan beban SKS per semester:
- Mahasiswa Baru (Semester 1): Diberikan paket mata kuliah maksimal **20 SKS**.
- Mahasiswa Semester 2 ke atas: Batas maksimal beban SKS ditentukan berdasarkan perolehan **Indeks Prestasi Semester (IPS)** pada semester sebelumnya (berkisar antara 18 hingga 24 SKS sesuai pedoman pendidikan UM).

---

## 3. Menu Administrasi, Nilai Studi & Kurikulum

### Bagaimana cara melihat nilai KHS dan transkrip nilai akademik di SIAKAD?
- **Kartu Hasil Studi (KHS):** Menampilkan rekapitulasi nilai dan IP pada semester tertentu. Akses menu **Akademik** > **Hasil Studi Semester (KHS)**. *(Syarat nilai KHS muncul: mahasiswa wajib menyelesaikan pengisian kuesioner Evaluasi PBM).*
- **Daftar Hasil Studi Kumulatif (DHS/Transkrip Sementara):** Menampilkan seluruh nilai mata kuliah yang pernah ditempuh dari semester awal hingga akhir. Akses menu **Akademik** > **Daftar Hasil Studi (DHS)**.
- **RPS & Kurikulum:** Rencana Pembelajaran Semester (RPS) dapat diunduh melalui menu **Rencana Studi** > klik kolom **Aksi** pada mata kuliah terkait > pilih **Unduh RPS**.

### Bagaimana cara memeriksa riwayat pembayaran UKT di SIAKAD?
Mahasiswa dapat memantau status pembayaran biaya kuliah melalui menu **Administrasi** > pilih **Riwayat Keuangan (SPP/SPSA)** atau **Riwayat Registrasi**. Status tagihan semester berjalan akan bertanda "Lunas" setelah pembayaran bank terverifikasi.

---

## 4. Menu Bimbingan Skripsi & Tugas Akhir

### Bagaimana alur bimbingan skripsi atau tugas akhir secara online di SIAKAD?
Pada menu **Tugas Akhir**, mahasiswa dapat:
1. Memantau Surat Keputusan (SK) penetapan Dosen Pembimbing Skripsi/Tesis/Disertasi.
2. Mencatat logbook dan riwayat konsultasi/bimbingan tugas akhir bersama Dosen Pembimbing.
3. Memeriksa status persetujuan kelayakan ujian tugas akhir dari dosen pembimbing sebelum mendaftar ujian akhir di SIMAWA.

---

## Tautan Resmi & Panduan Visual SIAKAD
- **Portal SIAKAD UM:** https://siakad.um.ac.id/
- **Panduan Visual Lengkap Penggunaan SIAKAD:** https://drive.google.com/file/d/118qJZOTWJdo6Sd8-NawuQl8Bjlw2VrK9/view?usp=sharing
- **Helpdesk UPT TIK UM:** https://support.um.ac.id/
- **Helpdesk Terpusat UM:** WhatsApp **0822-1333-4445**
"""

# ==========================================
# 4. Panduan_Pengisian_Evaluasi_PBM_di_SIAKAD.md
# ==========================================
doc_evaluasi_pbm = """# Panduan Pengisian Evaluasi PBM di SIAKAD Universitas Negeri Malang

> **Kategori:** `akademik`  
> **Department:** `Akademik`  
> **Target Pengguna:** Mahasiswa Aktif Universitas Negeri Malang (UM)  
> **Status:** Resmi Aktif  

---

## 1. Pengertian & Urgensi Evaluasi PBM

### Apa itu Evaluasi PBM di SIAKAD dan mengapa mahasiswa wajib mengisinya?
Evaluasi PBM (Proses Belajar Mengajar) adalah kuesioner penilaian mahasiswa terhadap pelaksanaan perkuliahan, ketercapaian RPS, dan kinerja dosen pengampu untuk setiap mata kuliah yang ditempuh pada semester berjalan:
- **Kaitan dengan Nilai/KHS:** Pengisian evaluasi PBM merupakan syarat mutlak agar **Nilai Akhir dan Kartu Hasil Studi (KHS)** semester tersebut dapat ditampilkan di SIAKAD.
- **Waktu Pembaruan (H+1):** Sesuai aturan sistem di SIAKAD, perubahan status pengisian evaluasi PBM dan pemunculan nilai IP diproses **H+1 (keesokan harinya)** setelah pengiriman kuesioner, bukan secara instan.

### Kapan jadwal pengisian Evaluasi PBM dilaksanakan?
Sesuai Kalender Akademik Universitas Negeri Malang:
- Pengisian evaluasi PBM dibuka mulai masa **Ujian Akhir Semester (UAS) sampai dengan sebelum batas penerbitan KHS online**.
- **Semester Gasal:** Sekitar pertengahan Desember hingga awal Januari.
- **Semester Genap:** Sekitar pertengahan Mei hingga awal Juni.

---

## 2. Tata Cara Pengisian Kuesioner Evaluasi PBM

### Bagaimana langkah-langkah mengisi evaluasi PBM di SIAKAD?
Langkah pengisian evaluasi dosen/PBM:
1. Akses portal https://siakad.um.ac.id/ dan login menggunakan NIM dan password Anda.
2. Masuk ke menu **Akademik** > pilih **Hasil Studi Semester**.
3. Pada tabel mata kuliah, klik tombol **"Isi Evaluasi PBM"** yang tertera pada baris mata kuliah yang belum dinilai.
4. Isi kuesioner yang terdiri dari pertanyaan skala penilaian kinerja perkuliahan dan kolom saran/masukan tertulis secara objektif.
5. Klik **"Simpan / Kirim Evaluasi"**.
6. Setelah berhasil dikirim, tombol akan berubah status menjadi **"Evaluasi PBM sudah diisi"** lengkap dengan cap waktu pengiriman (*timestamp*).
7. Nilai mata kuliah dan KHS akan terbuka secara otomatis pada **H+1** setelah pengisian.

---

## 3. Konsekuensi & Solusi Keterlambatan Pengisian Evaluasi PBM

### Apa konsekuensinya jika mahasiswa terlambat atau tidak mengisi evaluasi PBM?
Mahasiswa yang tidak mengisi kuesioner evaluasi PBM hingga batas kalender akademik ditutup akan mengalami kendala:
- Nilai mata kuliah dan Kartu Hasil Studi (KHS) pada semester tersebut **TIDAK DAPAT DILIHAT/DIPEROLEH** di SIAKAD pada periode semester berjalan.
- Keterlambatan melihat nilai dapat menghambat perencanaan pengambilan mata kuliah dan pengisian KRS pada semester berikutnya.

### Bagaimana solusi jika terlambat mengisi evaluasi PBM dan nilai tidak muncul?
Jika masa pengisian evaluasi PBM pada semester berjalan sudah resmi ditutup:
1. Mahasiswa baru dapat mengisi susulan kuesioner evaluasi PBM pada **periode pengisian evaluasi semester berikutnya** ketika jendela evaluasi dibuka kembali di SIAKAD.
2. Nilai mata kuliah yang tertunda akan ditampilkan di KHS setelah evaluasi susulan tersebut diselesaikan.
3. Apabila nilai sangat mendesak diperlukan untuk keperluan beasiswa, sidang tugas akhir, atau yudisium, mahasiswa disarankan berkonsultasi langsung ke **Subag Akademik Fakultas** masing-masing dengan membawa bukti persetujuan dari dosen pengampu.

---

## Tautan Resmi & Kontak Layanan Akademik
- **Portal SIAKAD UM:** https://siakad.um.ac.id/
- **Layanan Akademik Fakultas:** Subag Akademik Fakultas masing-masing di lingkungan UM
- **Helpdesk Terpusat UM:** WhatsApp **0822-1333-4445** (Senin–Jumat pukul 07.30–16.00 WIB)
"""

# ==========================================
# 5. Panduan_Registrasi_Ulang_dan_KRS_Mahasiswa_Lama_Semester_Gasal.md
# ==========================================
doc_registrasi_lama = """# Panduan Registrasi Ulang & KRS Mahasiswa Lama Semester Gasal Universitas Negeri Malang

> **Kategori:** `akademik`  
> **Department:** `Akademik`  
> **Target Pengguna:** Mahasiswa Lama (Terdaftar) Universitas Negeri Malang (UM)  
> **Status:** Resmi Aktif  

---

## 1. Ketentuan Registrasi Administrasi & Pembayaran UKT Semester Berjalan

### Siapa saja target mahasiswa pada registrasi ulang semester gasal?
Pedoman ini berlaku khusus bagi **mahasiswa lama (terdaftar aktif)** jenjang Diploma (D4), Sarjana (S1), Magister (S2), dan Doktor (S3) di Universitas Negeri Malang, bukan untuk calon mahasiswa baru.

### Apa perbedaan Mahasiswa Kategori 1 dan Kategori 2 dalam registrasi semester?
Universitas Negeri Malang membagi mahasiswa lama ke dalam dua kategori administrasi:
- **Mahasiswa Kategori 1:** Mahasiswa yang membayar Uang Kuliah Tunggal (UKT) dengan nominal tarif penuh/normal sesuai penetapan kategori awal.
- **Mahasiswa Kategori 2:** Mahasiswa yang mengajukan dan memperoleh penetapan khusus, seperti penurunan UKT, perpanjangan masa studi (tugas akhir), atau penundaan pembayaran.

---

## 2. Alur Pembayaran UKT & Pengisian KRS Online Mahasiswa Lama

### Bagaimana prosedur registrasi administrasi dan KRS online mahasiswa lama?
Tahapan registrasi semester gasal:
1. **Cek Tagihan Pembayaran:** Buka menu keuangan di portal https://siakad.um.ac.id/ untuk melihat rincian tagihan UKT semester berjalan.
2. **Pembayaran UKT di Bank Mitra:** Lakukan pembayaran melalui teller, ATM, atau mobile banking bank mitra resmi UM (BNI, BRI, BTN, Mandiri, Bank Jatim, CIMB Niaga, BSI) menggunakan Kode Bayar unik.
3. **Penerbitan Status Registrasi:** Sistem perbankan secara otomatis menyinkronkan data pembayaran ke SIAKAD, dan status mahasiswa berubah menjadi **"Terdaftar/Aktif"**.
4. **Pengisian KRS Online:** Akses portal https://siakad.um.ac.id/ pada jadwal pengisian KRS yang telah ditentukan dalam kalender akademik.
5. **Konsultasi Dosen PA:** Ajukan rencana studi ke Dosen Pembimbing Akademik (PA) untuk divalidasi dan disahkan secara online.

---

## 3. Sanksi Keterlambatan Registrasi & Ketentuan Cuti Kuliah

### Apa akibatnya jika mahasiswa lama tidak membayar UKT atau tidak registrasi sesuai jadwal?
Konsekuensi bagi mahasiswa yang melewati batas waktu kalender akademik:
- Mahasiswa dinyatakan **TIDAK TERDAFTAR SEBAGAI MAHASISWA AKTIF** pada semester bersangkutan.
- Tidak berhak memperoleh layanan akademik, bimbingan, maupun perkuliahan, serta tidak diperkenankan mengisi KRS.
- Waktu tidak aktif tersebut tetap diperhitungkan dalam batas maksimal masa studi.

### Bagaimana ketentuan pengajuan cuti kuliah bagi mahasiswa lama?
- Mahasiswa yang berhalangan melanjutkan studi karena alasan kesehatan atau alasan sah lainnya wajib mengajukan **Cuti Kuliah** secara resmi melalui sistem SIAKAD sebelum batas waktu registrasi berakhir.
- Mahasiswa yang disetujui cuti kuliah dibebaskan dari kewajiban membayar UKT semester tersebut (atau sesuai SK Rektor yang berlaku).

---

## Tautan Resmi & Layanan Bantuan
- **Portal SIAKAD UM:** https://siakad.um.ac.id/
- **Panduan e-Payment UM:** https://support.um.ac.id/topic/epayment/
- **Helpdesk Keuangan & UKT:** WhatsApp **0822-1333-4445**
- **Helpdesk Terpusat UM:** WhatsApp **0822-1333-4445**
"""

# ==========================================
# 6. Panduan_Ketentuan_Semester_Antara_dan_Pembatalan_KRS.md
# ==========================================
doc_semester_antara = """# Panduan dan Ketentuan Semester Antara (Semester Pendek) & Pembatalan KRS UM

> **Kategori:** `akademik`  
> **Department:** `Akademik`  
> **Target Pengguna:** Mahasiswa Aktif Universitas Negeri Malang (UM)  
> **Status:** Resmi Aktif  

---

## 1. Pengertian, Tujuan & Ketentuan Peserta Semester Antara

### Apa itu Semester Antara (Semester Pendek) di Universitas Negeri Malang dan apa fungsinya?
Semester Antara (Semester Pendek) adalah program perkuliahan tambahan pilihan (opsional/tidak wajib) yang diselenggarakan oleh Universitas Negeri Malang di antara semester genap dan gasal untuk:
- Memberikan kesempatan kepada mahasiswa untuk memperbaiki nilai mata kuliah (remedial/perbaikan).
- Mempercepat masa penyelesaian studi agar lulus tepat waktu.

### Apa saja syarat mahasiswa yang boleh mengikuti Semester Antara di UM?
Ketentuan peserta Semester Antara:
1. Terdaftar sebagai mahasiswa aktif pada semester berjalan (semester genap).
2. Mahasiswa yang sedang berstatus **cuti akademik TIDAK DIPERKENANKAN** mengikuti Semester Antara.
3. Mahasiswa dapat memprogram **maksimal 9 (sembilan) SKS** pada Semester Antara.

---

## 2. Jenis Mata Kuliah & Ketentuan Biaya Per SKS

### Berapa biaya kuliah Semester Antara di Universitas Negeri Malang?
Ketentuan tarif biaya Semester Antara UM:
- **Mata Kuliah Perbaikan Nilai:** Dikenakan tarif **Rp100.000 per SKS** sesuai tarif layanan resmi BLU UM.
- **Mata Kuliah Sajian Khusus (Bebas Biaya Tambahan):** KKN, KPL (Kependidikan & Non-Kependidikan), Tugas Akhir, Skripsi, dan Tesis tidak dikenakan biaya SKS tambahan.

### Mata kuliah apa saja yang boleh diambil pada Semester Antara?
1. **Mata Kuliah Perbaikan Nilai:** Mata kuliah yang sebelumnya mendapatkan nilai **C, D, atau E**. Nilai yang dicantumkan pada transkrip akademik resmi adalah nilai terbaik/terakhir yang diperoleh.
2. **Mata Kuliah Sajian Khusus:** KKN, KPL, Tugas Akhir, Skripsi, atau Tesis sesuai pembukaan oleh program studi masing-masing.

---

## 3. Alur Pendaftaran, Pembayaran & Pembatalan Mata Kuliah

### Bagaimana alur dan tahapan mengikuti Semester Antara di UM?
1. **Penjaringan Minat:** Mahasiswa mendata kebutuhan mata kuliah melalui HMD/Departemen.
2. **Unggah Sajian Kuliah:** Departemen/Prodi mengunggah daftar mata kuliah yang dibuka ke SIAKAD.
3. **Pengisian KRS Semester Antara:** Mahasiswa memprogram mata kuliah melalui portal SIAKAD (maksimal 9 SKS).
4. **Pembayaran Biaya SKS:** Bayar tagihan SKS via Kode Bayar di bank mitra resmi UM (BNI, BRI, BTN, Mandiri, Bank Jatim, CIMB Niaga, BSI) sebelum batas waktu. Panduan: https://support.um.ac.id/topic/epayment/.
5. **Perkuliahan & Ujian:** Perkuliahan Semester Antara dilaksanakan secara intensif diakhiri evaluasi/UAS.
6. **Penerbitan Nilai:** Hasil studi diumumkan melalui KHS online di SIAKAD.

### Apakah mata kuliah Semester Antara yang sudah diprogram bisa dibatalkan dan bagaimana pengembalian biayanya?
Ketentuan pembatalan mata kuliah Semester Antara:
- **Pembatalan oleh Mahasiswa:** Mata kuliah yang telah diprogram dan dibayar oleh mahasiswa **TIDAK DAPAT DIBATALKAN** secara sepihak.
- **Pembatalan oleh Program Studi:** Pembatalan hanya dapat dilakukan oleh program studi apabila jumlah peserta kelas tidak memenuhi batas kuota minimal yang ditetapkan.
- **Kompensasi Biaya:** Jika kelas dibatalkan oleh program studi dan mahasiswa tidak memilih mata kuliah pengganti lain, biaya SKS yang telah dibayarkan akan **diperhitungkan dan dikompensasikan ke tagihan UKT semester berikutnya**.

---

## Tautan Resmi & Panduan Registrasi Semester Antara
- **Portal SIAKAD UM:** https://siakad.um.ac.id/
- **Panduan e-Payment UM:** https://support.um.ac.id/topic/epayment/
- **Panduan Teknis KRS & Bayar SKS Semester Antara:** https://docs.google.com/document/d/1UQLp7r1e31FwWnW0a_ivkjzcpsoXICyA/edit?usp=sharing
- **Helpdesk Terpusat UM:** WhatsApp **0822-1333-4445**
"""

# ==========================================
# 7. Panduan_Proses_Yudisium_Kelulusan_dan_Wisuda.md
# ==========================================
doc_yudisium = """# Panduan Proses Yudisium Kelulusan dan Wisuda Universitas Negeri Malang

> **Kategori:** `akademik`  
> **Department:** `Akademik`  
> **Target Pengguna:** Mahasiswa Tingkat Akhir (Sarjana, Magister, Doktor, Profesi) UM  
> **Status:** Resmi Aktif  

---

## 1. Alur Pasca-Ujian Akhir Menuju SK Yudisium

### Bagaimana alur proses yudisium setelah mahasiswa dinyatakan lulus ujian tugas akhir/skripsi di UM?
Tahapan lengkap pasca-ujian tugas akhir:
1. **Revisi Tugas Akhir:** Selesaikan revisi laporan skripsi/tesis/disertasi sesuai catatan dosen penguji dan peroleh lembar pengesahan resmi.
2. **Bebas Tanggungan & Unggah Mandiri:** Selesaikan verifikasi bebas tanggungan perpustakaan, laboratorium, serta unggah karya ilmiah ke repositori perpustakaan UM.
3. **Verifikasi Data Akademik di SIAKAD:** Pastikan seluruh nilai mata kuliah sudah lengkap dan tidak ada nilai kosong atau belum keluar di Daftar Hasil Studi (DHS).
4. **Verifikasi Data Ijazah (PISN):** Verifikasi kesesuaian Nama, NIK, Tempat/Tanggal Lahir, dan Nomor Ijazah Nasional di SIAKAD sesuai KTP dan Akta Kelahiran.
5. **Pengisian SKPI:** Lengkapi portofolio prestasi dan kegiatan kemahasiswaan pada sistem Surat Keterangan Pendamping Ijazah (SKPI) di SIMAWA (https://simawa.um.ac.id/).
6. **Pendaftaran Yudisium Online:** Ajukan pendaftaran yudisium melalui menu yudisium di portal SIAKAD.
7. **Penerbitan DHSY & SK Yudisium:** Fakultas memverifikasi berkas pendaftar, menerbitkan Daftar Hasil Studi Yudisium (DHSY), dan menerbitkan **Surat Keputusan (SK) Yudisium Rektor**.

---

## 2. Ketentuan Kelulusan, PISN & Foto Ijazah

### Apa syarat foto untuk ijazah yang diunggah saat pendaftaran yudisium?
Kriteria pasfoto resmi ijazah di UM:
- Foto studio terbaru dengan resolusi tajam dan pencahayaan baik.
- Pria: Mengenakan kemeja putih polos, berdasi, dan memakai jas formal hitam/gelap.
- Wanita: Mengenakan pakaian formal blazer/kebaya nasional rapi (bagi yang berhijab, gunakan jilbab rapi tidak menutupi wajah).
- Latar belakang (*background*) foto polos berwarna sesuai ketentuan universitas/fakultas.

### Apa itu PISN dan mengapa verifikasi data ijazah sangat penting?
Penomoran Ijazah Nasional (PISN) adalah sistem penomoran ijazah terpusat dari Kemendikbudristek:
- Mahasiswa wajib memastikan NIK terdaftar valid di Dukcapil dan data PDDIKTI sesuai dengan berkas kependudukan.
- Ketidaksesuaian data dapat menyebabkan nomor ijazah nasional gagal terbit (*unverified*).

---

## 3. Penanganan Jika Gagal Yudisium pada Semester Berjalan

### Bagaimana jika mahasiswa gagal yudisium pada semester berjalan?
- Mahasiswa yang telah lulus ujian tugas akhir tetapi belum menyelesaikan berkas yudisium hingga batas akhir semester berjalan wajib **melakukan registrasi administratif pada semester berikutnya**.
- Sesuai kebijakan keuangan UM, mahasiswa yang tinggal menyelesaikan tahapan yudisium/tugas akhir dapat mengajukan permohonan pembebasan atau keringanan UKT melalui sistem SIUKT (https://siukt.um.ac.id/) sesuai ketentuan yang berlaku.

---

## 4. Pasca-Yudisium: Ijazah, Transkrip & Pendaftaran Wisuda

### Kapan ijazah dan transkrip asli dapat diambil setelah yudisium?
- Ijazah dan transkrip akademik asli dicetak setelah SK Yudisium dan PISN terverifikasi.
- Pengambilan dokumen fisik dilakukan di **Subag Registrasi & Statistik, Gedung Graha Rektorat Lantai 2 UM** dengan membawa bukti bebas tanggungan dan tanda pengenal resmi.

### Bagaimana cara mendaftar wisuda di Universitas Negeri Malang?
Setelah SK Yudisium terbit, mahasiswa berhak mendaftar sebagai peserta wisuda melalui portal pendaftaran wisuda resmi UM (https://wisuda.um.ac.id/) untuk memilih periode wisuda yang tersedia.

---

## Tautan Resmi & Kontak Layanan Yudisium
- **Portal SIAKAD UM:** https://siakad.um.ac.id/
- **Portal Kemahasiswaan SIMAWA:** https://simawa.um.ac.id/
- **Portal Pendaftaran Wisuda UM:** https://wisuda.um.ac.id/
- **Subag Registrasi & Statistik:** Gedung Graha Rektorat Lantai 2 UM
- **Helpdesk Terpusat UM:** WhatsApp **0822-1333-4445**
"""

# ==========================================
# 8. Panduan_Layanan_Legalisir_Ijazah_Online_UM.md
# ==========================================
doc_legalisir = """# Panduan Layanan Legalisir Ijazah Online (e-Legalisir) Universitas Negeri Malang

> **Kategori:** `akademik`  
> **Department:** `Akademik`  
> **Target Pengguna:** Alumni & Lulusan Universitas Negeri Malang (UM)  
> **Status:** Resmi Aktif  

---

## 1. Alur Prosedur Pengajuan e-Legalisir Online

### Bagaimana cara mengajukan legalisir ijazah dan transkrip secara online di UM?
Tahapan pengajuan legalisir elektronik (e-Legalisir):
1. **Persiapan Berkas:** Siapkan dokumen ijazah asli, transkrip nilai asli, dan akta mengajar asli (jika ada).
2. **Buat Akun di Portal:** Akses portal resmi https://legalisir.um.ac.id/ dan buat akun permohonan menggunakan NIM yang terdaftar di database UM dan email aktif.
3. **Verifikasi Email:** Buka email dan klik tautan aktivasi akun legalisir.
4. **Unggah Scan Berkas Asli:** Unggah hasil scan dokumen asli berformat JPG/JPEG (maksimal 2 MB per berkas).
5. **Verifikasi Admin:** Tunggu proses verifikasi keabsahan dokumen oleh admin Subag Registrasi & Statistik UM.
6. **Pembayaran Biaya Legalisir:** Lakukan pembayaran sesuai Kode Bayar yang muncul di sistem.
7. **Unduh Dokumen e-Legalisir:** Setelah disahkan secara digital oleh Peruri, unduh file PDF legalisir resmi ber-QR Code dari akun Anda.

---

## 2. Ketentuan Berkas Scan, Tarif Biaya & Masa Berlaku

### Apa ketentuan format dan ukuran dokumen scan untuk legalisir?
- **Wajib Mesin Scanner:** Seluruh dokumen wajib dipindai menggunakan **mesin scanner flatbed/dokumen**. DILARANG menggunakan foto kamera ponsel atau aplikasi scanner HP.
- **Format File:** Wajib berformat **JPG atau JPEG** (tidak diperkenankan berformat PDF).
- **Ukuran File:** Maksimal **2 MB** per dokumen, dengan hasil pindaian bersih, tegak (tidak miring/terpotong), dan tulisan terbaca jelas.

### Berapa biaya legalisir ijazah online di UM dan berapa masa berlakunya?
- **Ijazah:** Rp50.000 per permohonan dokumen.
- **Transkrip Nilai:** Rp50.000 per permohonan dokumen.
- **Akta Mengajar:** Rp30.000 per permohonan dokumen.
- **Masa Berlaku e-Legalisir:** Dokumen e-Legalisir berlaku selama **6 (enam) bulan** terhitung sejak tanggal tanda tangan digital diterbitkan.
- **Verifikasi Keaslian QR Code:** Keaslian dokumen digital dapat dipindai langsung menggunakan aplikasi **Peruri Code Scanner** (unduh via Google Play Store).

---

## 3. Kanal Pembayaran Biaya Legalisir

### Pembayaran biaya legalisir bisa dilakukan melalui apa saja?
Pembayaran dapat dilakukan di seluruh Indonesia menggunakan Kode Bayar:
- **Bank Mitra Resmi UM:**
  - Bank BNI (Teller, ATM, Mobile Banking, Internet Banking)
  - Bank Mandiri (Teller, ATM, Mobile Banking, Internet Banking)
  - Bank BRI (Teller, ATM)
  - Bank BTN (Teller, ATM)
  - Bank Jatim (Teller, ATM)
  - Bank CIMB Niaga (ATM, Internet Banking)
  - Bank Syariah Indonesia (BSI)
- **E-Commerce:** Dapat dibayarkan melalui **Tokopedia** pada menu Pembayaran Biaya Pendidikan dengan memasukkan kode pembayaran yang sama.

---

## 4. Layanan Legalisir Offline (Tatap Muka Langsung)

### Apakah bisa melakukan legalisir secara langsung (offline) di kampus UM?
Bisa. Alumni dapat datang langsung dengan membawa ijazah dan transkrip asli serta fotokopi dokumen yang akan dilegalisasi ke:
- **Lokasi Layanan:** Loket Pelayanan Terpadu Subag Registrasi dan Statistik, **Gedung Graha Rektorat Lantai 2 UM**, Jl. Semarang No. 5 Malang.
- **Jam Pelayanan:** Hari kerja Senin–Jumat pukul 08.00–15.00 WIB.

---

## Tautan Resmi & Layanan Bantuan Legalisir
- **Portal e-Legalisir UM:** https://legalisir.um.ac.id/
- **Aplikasi Verifikasi Dokumen:** Peruri Code Scanner (Play Store)
- **Lokasi Layanan:** Subag Registrasi & Statistik, Gedung Graha Rektorat Lantai 2 UM
- **Helpdesk Terpusat UM:** WhatsApp **0822-1333-4445**
"""

# Write the new standardized files
files_to_write = {
    "Panduan_Aktivasi_Akun_SIAKAD_Mahasiswa_Baru.md": doc_aktivasi,
    "Panduan_Registrasi_Akun_SIAKAD_dan_Daftar_Ulang.md": doc_daftar_ulang,
    "Panduan_Penggunaan_Fitur_SIAKAD_Mahasiswa_Aktif.md": doc_fitur_siakad,
    "Panduan_Pengisian_Evaluasi_PBM_di_SIAKAD.md": doc_evaluasi_pbm,
    "Panduan_Registrasi_Ulang_dan_KRS_Mahasiswa_Lama_Semester_Gasal.md": doc_registrasi_lama,
    "Panduan_Ketentuan_Semester_Antara_dan_Pembatalan_KRS.md": doc_semester_antara,
    "Panduan_Proses_Yudisium_Kelulusan_dan_Wisuda.md": doc_yudisium,
    "Panduan_Layanan_Legalisir_Ijazah_Online_UM.md": doc_legalisir,
}

for fname, content in files_to_write.items():
    fpath = os.path.join(src_dir, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created/Standardized: {fname} ({len(content)} chars)")

# Move old raw / duplicate / shredded files to archive
old_files_to_archive = [
    "1) Panduan Aktifasi Akun Siakad UM untuk Mahasiswa Baru UM.md",
    "2) Panduan Aktifasi Akun Siakad UM untuk Mahasiswa Baru UM.md",
    "3) Panduan Aktifasi Akun Siakad UM untuk Mahasiswa Baru UM.md",
    "1) Panduan Siakad Mahasiswa.md",
    "KB Evaluasi PBM - Registrasi - KRS 2.md",
    "KB Evaluasi PBM - Registrasi - KRS.md",
    "KB_Registrasi_Mahasiswa_Semester_Gasal_2026_2027_UM (2).md",
    "KNOWLEDGE BASE CHATBOT  Semester Antara atau pendek di Universitas Negeri Malang (UM)  Intent- penjelasan_semester_antara atau pendek.docx.md",
    "Pembatalan Mata Kuliah  Intent- pembatalan_KRS dan  Biaya SKS semester_antara atau pendek.docx.md",
    "KB Proses Yudisium - versi 1.md",
    "KB_Legalisir_Ijazah_UM.md",
    "KB_Registrasi_Akun_SIAKAD_DaftarUlang.md",
    "knowledge-source new.md"
]

for old_f in old_files_to_archive:
    p = os.path.join(src_dir, old_f)
    if os.path.exists(p):
        dest = os.path.join(archive_dir, old_f)
        shutil.move(p, dest)
        print(f"Archived: {old_f} -> {archive_dir}")

print("\nSubfolder 3 Standardization COMPLETE!")
