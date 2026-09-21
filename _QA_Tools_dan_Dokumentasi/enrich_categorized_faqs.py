import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(BASE_DIR, 'Knowledge_Base_Clean_Categorized')

# ==========================================
# 1. PMB FAQ
# ==========================================
pmb_content = """# FAQ: Pendaftaran Seleksi Mandiri, Persyaratan Berkas & Kendala Form Isian

> **Kategori:** `pmb`  
> **Department:** `PMB`  
> **Target Pengguna:** Calon Mahasiswa Baru Jalur Seleksi Mandiri Universitas Negeri Malang (UM)  
> **Status:** Resmi Aktif  

---

## 1. Alur Pembuatan Akun & Pendaftaran Seleksi Mandiri

### Bagaimana cara daftar ke Universitas Negeri Malang untuk jalur mandiri?
Untuk mendaftar Seleksi Mandiri Universitas Negeri Malang (UM), ikuti alur resmi berikut:
1. Buka laman resmi pendaftaran seleksi: https://seleksi.um.ac.id/
2. Klik menu **Daftar Akun** untuk membuat akun baru menggunakan email aktif dan nomor WhatsApp yang valid.
3. Login ke sistem pendaftaran menggunakan email dan kata sandi yang telah didaftarkan.
4. Pilih jalur seleksi mandiri yang diminati (contoh: Jalur Prestasi, Jalur Skor UTBK, Jalur TMBK, Jalur Kemitraan).
5. Lengkapi biodata diri, data sekolah, dan data nilai/skor secara cermat dan benar.
6. Unggah seluruh dokumen persyaratan yang diwajibkan sesuai jalur pilihan.
7. Lakukan pembayaran biaya pendaftaran menggunakan **Kode Bayar** yang muncul di sistem pada bank mitra resmi UM (bukan ke nomor rekening).
8. Setelah pembayaran terverifikasi oleh perbankan, lakukan finalisasi pendaftaran dan cetak Kartu Peserta Seleksi Mandiri UM.

### Mengapa saya tidak bisa membuat akun registrasi pendaftaran?
Jika mengalami kendala gagal saat membuat akun pendaftaran seleksi:
- **Gunakan Komputer / Laptop:** Sangat disarankan mendaftar menggunakan PC atau laptop, hindari menggunakan smartphone/HP karena tampilan notifikasi dan tautan verifikasi email sering terpotong atau tidak tampil sempurna pada layar HP.
- **Cek Folder Spam / Promosi:** Periksa folder *Spam* atau *Promotions* pada email Anda untuk menemukan tautan aktivasi akun pendaftaran.

### Bagaimana jika Ijazah atau SKL (Surat Keterangan Lulus) belum keluar saat mendaftar?
Jika ijazah atau SKL resmi dari sekolah belum diterbitkan, pendaftar dapat menggunakan **Surat Keterangan Kelas XII** atau Surat Keterangan Sedang Mengikuti Ujian Sekolah dari pihak sekolah asal yang ditandatangani oleh Kepala Sekolah dan berstempel resmi sebagai pengganti sementara dokumen ijazah.

---

## 2. Kendala Teknis Unggah Berkas & Cetak Dokumen

### Mengapa setiap unggah (upload) foto atau dokumen selalu gagal?
Pastikan dokumen dan pasfoto yang diunggah memenuhi spesifikasi teknis sistem UM berikut:
1. **Resolusi & Dimensi Foto:** Pasfoto berdimensi minimal **800 x 600 pixel**, ukuran cetak **4 x 6 cm**, posisi tegak (*portrait*), berpakaian rapi/sopan, dan berlatar belakang polos warna merah atau biru.
2. **Format File:** Format file harus **JPG / JPEG / PNG** untuk foto, dan format **PDF** untuk dokumen berkas pendukung.
3. **Ukuran File:** Ukuran file maksimal **2 MB (2.048 KB)**. Jika ukuran terlalu besar, lakukan kompresi/resize secukupnya tanpa mengurangi keterbacaan dokumen.
4. **Nama File:** Gunakan penamaan file standar huruf dan angka (contoh: `Pasfoto_Nama.jpg`), hindari penggunaan karakter khusus atau simbol aneh.
5. **Browser & Jaringan:** Gunakan browser Google Chrome versi terbaru dan pastikan koneksi internet stabil.

### Mengapa dokumen kartu pendaftaran atau formulir tidak bisa dicetak?
Jika Anda mengalami kendala saat mencetak (*print*) dokumen kartu peserta atau formulir:
- Pastikan perangkat PC/laptop telah terhubung dengan perangkat *printer* aktif.
- Jangan mencetak langsung dari smartphone/HP.
- Jika tombol cetak atau dokumen PDF tidak merespons di Google Chrome, gunakan peramban alternatif seperti **Mozilla Firefox** atau **Opera**.

---

## 3. Kendala Kolom Isian Formulir Biodata Pendaftaran

### Untuk kolom Alamat di Malang jika belum ada tempat tinggal/kos bagaimana ya?
Jika saat ini calon pendaftar belum memiliki tempat tinggal, kontrakan, atau tempat kos di Kota Malang, kolom Alamat di Malang dapat diisikan dengan **alamat tempat tinggal atau domisili asal saat ini**. Pembaruan alamat kos di Malang dapat dilakukan setelah resmi diterima dan her-registrasi.

### Bagaimana jika pekerjaan orang tua tidak ada pada pilihan menu dropdown?
Pilihlah opsi jenis pekerjaan yang **paling mendekati atau serupa** dengan jenis pekerjaan orang tua Anda (contoh: untuk pedagang kecil/toko dapat memilih sektor Wiraswasta/Perdagangan, untuk pekerja harian dapat memilih Buruh/Pekerja Lepas).

### Bagaimana jika nama sekolah asal saya tidak muncul dalam pilihan sistem?
Jika nama sekolah asal tidak tercantum pada daftar pencarian sistem pendaftaran:
1. Pilih opsi: **"Sekolah Lain-Lain"**.
2. Kemudian ketik dan masukkan nama sekolah asal Anda secara manual pada kolom isian yang muncul.

### Bagaimana jika tempat lahir tidak tersedia atau tidak muncul dalam daftar sistem?
Hal ini umumnya terjadi akibat adanya pemekaran wilayah administratif baru:
1. Pilih nama kabupaten atau kota induk yang paling dekat/sebelum pemekaran.
2. Perbaikan detail data tempat lahir dapat diajukan pada saat proses her-registrasi akademik setelah dinyatakan diterima.

### Bagaimana jika data NISN tidak terdeteksi atau tidak sinkron?
Pastikan NISN yang dimasukkan adalah 10 digit resmi yang tercatat di portal Dapodik/Kemdikbud: https://nisn.data.kemdikbud.go.id/. Jika data tetap tidak sinkron, hubungi pihak operator sekolah asal Anda atau Helpdesk Seleksi PMB UM.

---

## Tautan Resmi & Kontak Bantuan PMB
- **Portal Seleksi PMB UM:** https://seleksi.um.ac.id/
- **Pusat Informasi Pendaftaran (Simaba):** WhatsApp **0851-7116-7273** atau **0851-2441-4488**
- **Helpdesk Terpusat UM:** WhatsApp **0822-1333-4445** (Senin–Jumat pukul 07.30–16.00 WIB)
"""

# ==========================================
# 2. KEUANGAN FAQ
# ==========================================
keu_content = """# FAQ: Pembayaran Biaya Seleksi, Ketentuan Slip Gaji & Kebijakan KIP-K Mandiri

> **Kategori:** `keuangan`  
> **Department:** `Keuangan`  
> **Target Pengguna:** Calon Mahasiswa Baru & Orang Tua/Wali Pendaftar Universitas Negeri Malang (UM)  
> **Status:** Resmi Aktif  

---

## 1. Sistem & Tata Cara Pembayaran Biaya Pendaftaran

### Bagaimana cara membayar biaya pendaftaran seleksi mandiri UM?
Pembayaran biaya pendaftaran seleksi mandiri UM dilakukan menggunakan sistem **Kode Bayar** otomatis dari sistem seleksi (bukan transfer ke nomor rekening perorangan/rekening bank biasa).
1. Selesaikan pengisian formulir pendaftaran hingga tahap pembayaran untuk mendapatkan Kode Bayar unik.
2. Panduan tata cara pembayaran dari masing-masing bank mitra resmi dapat diakses pada portal e-Payment resmi UM: https://support.um.ac.id/topic/epayment/.
3. Panduan visual aktivasi kode bayar dapat diunduh pada tautan resmi: https://drive.google.com/file/d/10EAZepNXWTILkXgqO9AbKY_9D5eN55Yb/view.
4. Masukkan Kode Bayar pada menu pembayaran tagihan pendidikan Universitas Negeri Malang di ATM/Mobile Banking/Teller.
5. Simpan struk/bukti bayar sebagai bukti verifikasi yang sah.

### Pembayaran biaya pendaftaran bisa dilakukan di bank mana saja?
Pembayaran biaya pendaftaran dan pendidikan UM dapat dilakukan di seluruh wilayah Indonesia melalui **Bank Mitra Resmi UM**:
- Bank Negara Indonesia (BNI)
- Bank Rakyat Indonesia (BRI)
- Bank Tabungan Negara (BTN)
- Bank Mandiri
- Bank Jatim
- CIMB Niaga
- BTN Syariah
- Bank Syariah Indonesia (BSI)

**Catatan Penting Kode Bayar:**
- Kode Bayar memiliki masa aktif selama **48 jam**.
- Jika kode bayar kedaluwarsa sebelum sempat dibayarkan, peserta dapat mengaktifkan kembali kode bayar baru melalui sistem pendaftaran seleksi.

---

## 2. Ketentuan Bukti Dokumen Finansial Orang Tua

### Bagaimana jika orang tua saya tidak memiliki slip gaji?
Ketentuan dokumen bukti penghasilan orang tua untuk pendaftaran seleksi UM:
1. **PNS / TNI / POLRI / BUMN / Karyawan Swasta:** Wajib melampirkan **Slip Gaji Resmi** atau Surat Keterangan Penghasilan dari instansi/perusahaan tempat bekerja.
2. **Wiraswasta / Petani / Pedagang / Pekerja Informal / Buruh Harian:** Wajib membuat **Surat Pernyataan Penghasilan Rata-rata per Bulan** yang diketahui dan disahkan oleh RT/RW setempat atau Kepala Desa/Kelurahan.
   - Format contoh Surat Pernyataan Penghasilan dapat diunduh pada tautan resmi: https://docs.google.com/document/d/1mo6liEF-jDTVk8te14auGc7f6kfVVzoE/edit.

### Bagaimana jika tidak memiliki bukti Pajak Bumi dan Bangunan (PBB)?
Ketentuan pengganti bukti PBB:
- **Jika Rumah Kontrak atau Sewa:** Buat surat keterangan kontrak/sewa yang mencantumkan nominal biaya sewa per tahun/bulan, dan disahkan oleh RT/RW setempat.
- **Jika Menumpang di Rumah Keluarga/Orang Lain:** Buat surat keterangan menumpang dengan mencantumkan perkiraan luas bangunan yang ditempati, disahkan oleh RT/RW setempat.
- Format contoh Surat Pernyataan Tidak Punya PBB dapat diunduh pada tautan resmi: https://docs.google.com/document/d/1PKWd-5-KfmkcHZ6OpOW4UFgyRyTB2o-M/edit?rtpof=true&sd=true&tab=t.0.

### Bagaimana jika rumah tidak menggunakan air PDAM (menggunakan air sumur)?
Jika rumah tangga tidak berlangganan air PDAM:
- Buat **Surat Keterangan Penggunaan Air Non-PDAM** (sumur pribadi/pompa) yang disahkan oleh RT/RW setempat.
- Format contoh Surat Keterangan Rekening Air Non-PDAM dapat diunduh pada tautan resmi: https://docs.google.com/document/d/1_xDB4e6L_qxw7tzxzjPNPy_eIl40DD67/edit.

---

## 3. Kebijakan KIP-Kuliah pada Jalur Seleksi Mandiri

### Apakah jalur Seleksi Mandiri UM bisa menggunakan beasiswa KIP-Kuliah (KIP-K)?
**Tidak.**  
Jalur Seleksi Mandiri di Universitas Negeri Malang **tidak menggunakan beasiswa KIP-Kuliah (KIP-K)**. Seluruh pendaftar jalur seleksi mandiri diwajibkan membuat dan mengunggah **Surat Pernyataan Kesanggupan Membayar Biaya Pendidikan** (UKT dan IPI) bermeterai Rp10.000.  
- Format resmi Surat Pernyataan Kesanggupan Membayar Biaya Pendidikan dapat diunduh pada tautan resmi panitia seleksi: https://seleksi.um.ac.id/wp-content/uploads/2023/05/Surat-Pernyataan-Kesanggupan-Membayar-Biaya-Pendidikan-Mandiri-2023.pdf.

---

## Tautan Resmi & Kontak Layanan Keuangan
- **Panduan e-Payment UM:** https://support.um.ac.id/topic/epayment/
- **Helpdesk Keuangan & UKT:** WhatsApp **0822-1333-4445** (Senin–Jumat pukul 07.30–16.00 WIB)
- **Helpdesk Terpusat UM:** WhatsApp **0822-1333-4445**
"""

# ==========================================
# 3. AKADEMIK FAQ
# ==========================================
akd_content = """# FAQ: Registrasi Online Mahasiswa Baru (Pasca-Lulus Seleksi) & SIAKAD

> **Kategori:** `akademik`  
> **Department:** `Akademik`  
> **Target Pengguna:** Mahasiswa Baru yang Dinyatakan Lolos Seleksi Universitas Negeri Malang (UM)  
> **Status:** Resmi Aktif  

---

## 1. Alur Lengkap Registrasi Online Mahasiswa Baru

### Bagaimana proses dan alur Registrasi Online setelah calon mahasiswa dinyatakan lulus seleksi?
Bagi calon mahasiswa baru yang dinyatakan diterima (jalur SNBP, SNBT, maupun Seleksi Mandiri UM), tahapan registrasi online adalah:
1. **Cek Pengumuman:** Periksa status kelulusan di portal pendaftaran https://seleksi.um.ac.id/.
2. **Pembayaran Biaya Pendidikan (UKT / IPI):** Lakukan pembayaran biaya pendidikan menggunakan Kode Bayar melalui bank mitra resmi UM.
3. **Penerbitan NIM:** Setelah pembayaran terverifikasi oleh sistem perbankan, sistem akademik UM secara otomatis akan menerbitkan **Nomor Induk Mahasiswa (NIM)** 12 digit.
4. **Login Registrasi Online:** Masuk ke laman portal registrasi: https://registrasiv4.um.ac.id/ menggunakan nomor peserta dan kata sandi/tanggal lahir sesuai petunjuk.
5. **Pengisian Biodata & Berkas:** Lengkapi seluruh data induk mahasiswa baru, data riwayat keluarga, dan unggah berkas kelengkapan registrasi.
6. **Unduh Form Registrasi:** Cetak formulir biodata registrasi online yang telah ditandatangani sebagai bukti sah status mahasiswa baru UM.
7. **Aktivasi Akun SIAKAD:** Akses sistem informasi akademik di https://siakad.um.ac.id/ untuk aktivasi akun perkuliahan dan persiapan pengisian KRS.

---

## 2. Kendala Teknis Pasca-Pembayaran UKT & Registrasi

### Mengapa setelah bayar UKT status di web registrasi belum lunas atau NIM belum terbit?
Proses sinkronisasi data transaksi antara perbankan dan server akademik UM membutuhkan waktu verifikasi:
- Harap menunggu sekitar **1 hingga 3 jam kerja** setelah pembayaran berhasil didebet oleh pihak bank.
- Pastikan transaksi perbankan Anda berstatus berhasil (*success*) dan Kode Bayar yang diinput sesuai.
- Jika setelah lebih dari 3 jam status pembayaran belum berubah, segera hubungi **Helpdesk Registrasi Mahasiswa Baru** melalui WhatsApp di nomor **0813-3344-400** dengan mengirimkan foto bukti struk pembayaran perbankan yang jelas.

### Bagaimana memilih ukuran jas almamater saat pengisian registrasi online?
Pada formulir pemilihan jas almamater, pilihlah ukuran pakaian (S, M, L, XL, XXL) yang biasa Anda gunakan dalam aktivitas sehari-hari.

### Mengapa dokumen bukti registrasi online tidak bisa diunduh?
Jika dokumen bukti registrasi gagal diunduh:
- Gunakan perangkat komputer/laptop dan pastikan koneksi internet stabil.
- Bersihkan riwayat *cache* browser atau gunakan peramban lain seperti Mozilla Firefox.

### Akun email UM berhasil dibuat tetapi email konfirmasi tidak masuk?
Jika email konfirmasi akun mahasiswa UM belum masuk ke kotak masuk email Anda:
1. Buka laman portal akademik: https://siakad.um.ac.id/.
2. Lakukan login ke akun SIAKAD Anda.
3. Masuk ke **Menu Akun / Profil Mahasiswa** untuk melakukan verifikasi dan aktivasi email resmi UM secara mandiri.

---

## Tautan Resmi & Kontak Bantuan Registrasi
- **Portal Registrasi Online UM:** https://registrasiv4.um.ac.id/
- **Portal Akademik SIAKAD:** https://siakad.um.ac.id/
- **Helpdesk Registrasi Mahasiswa Baru:** WhatsApp **0813-3344-400** (Khusus chat, hari kerja Senin–Jumat)
- **Helpdesk Terpusat UM:** WhatsApp **0822-1333-4445**
"""

p1 = os.path.join(TARGET_DIR, '01_PMB_Penerimaan_Mahasiswa_Baru', 'FAQ_Pendaftaran_Mandiri_dan_Kendala_Form.md')
p2 = os.path.join(TARGET_DIR, '02_Keuangan_dan_Biaya_Pendidikan', 'FAQ_Pembayaran_Biaya_Slip_Gaji_dan_KIPK.md')
p3 = os.path.join(TARGET_DIR, '03_Akademik_dan_SIAKAD', 'FAQ_Registrasi_Online_Maba_Lulus_Seleksi.md')

with open(p1, 'w', encoding='utf-8') as f:
    f.write(pmb_content.strip() + '\n')
print(f"[UPDATED] {p1}")

with open(p2, 'w', encoding='utf-8') as f:
    f.write(keu_content.strip() + '\n')
print(f"[UPDATED] {p2}")

with open(p3, 'w', encoding='utf-8') as f:
    f.write(akd_content.strip() + '\n')
print(f"[UPDATED] {p3}")

print("\nSemua FAQ berhasil diperbarui dengan rincian lengkap & tautan template resmi!")
