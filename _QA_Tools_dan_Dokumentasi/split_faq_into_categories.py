import os
import sys
import re
import shutil

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(BASE_DIR, 'Knowledge_Base_Clean_Categorized')

# Baca teks mentah FAQ
src_faq = os.path.join(TARGET_DIR, '05_Helpdesk_dan_Eskalasi', 'FAQ _ INFORMASI DAFTAR PERTANYAAN UMUM YANG SERING DISAMPAIKAN.md')
with open(src_faq, encoding='utf-8', errors='replace') as f:
    raw_faq = f.read()

print(f"Membaca file sumber FAQ: {len(raw_faq)} karakter")

# =========================================================================
# MODUL 1: FAQ PMB (Pendaftaran Mandiri, Foto & Form Data Isian)
# =========================================================================
faq_pmb_content = """# FAQ: Pendaftaran Seleksi Mandiri, Persyaratan Berkas & Kendala Form Isian

> **Kategori:** `pmb`  
> **Department:** `PMB`  
> **Target Pengguna:** Calon Mahasiswa Baru Jalur Seleksi Mandiri Universitas Negeri Malang (UM)  
> **Status:** Resmi Aktif  

---

## 1. Alur Pembuatan Akun & Pendaftaran Seleksi Mandiri

### Bagaimana cara daftar ke Universitas Negeri Malang untuk jalur mandiri?
Untuk mendaftar Seleksi Mandiri Universitas Negeri Malang (UM), ikuti langkah berikut:
1. Buka laman resmi pendaftaran: https://seleksi.um.ac.id/
2. Klik tombol **Daftar Akun** untuk membuat akun pendaftaran baru menggunakan email aktif dan nomor WhatsApp yang valid.
3. Login ke sistem menggunakan email dan kata sandi yang telah didaftarkan.
4. Pilih jalur seleksi mandiri yang diminati (contoh: Jalur Prestasi, Jalur Skor UTBK, Jalur TMBK, atau Kemitraan).
5. Isi data diri (biodata), riwayat pendidikan, dan nilai raport/skor UTBK secara lengkap dan benar.
6. Unggah dokumen persyaratan yang diminta sesuai dengan jalur yang dipilih.
7. Lakukan pembayaran biaya pendaftaran menggunakan Kode Bayar yang tertera di sistem melalui bank mitra resmi UM.
8. Setelah pembayaran terverifikasi, selesaikan finalisasi data dan cetak Kartu Peserta Seleksi Mandiri UM.

### Bagaimana jika Ijazah atau SKL (Surat Keterangan Lulus) belum keluar saat mendaftar?
Bagi pendaftar lulusan tahun berjalan yang ijazah atau SKL resminya belum diterbitkan dari pihak sekolah, dokumen tersebut dapat digantikan untuk sementara waktu menggunakan **Surat Keterangan Kelas XII** atau **Surat Keterangan Sedang Mengikuti Ujian Sekolah** yang ditandatangani oleh Kepala Sekolah dan dibubuhi cap basah/resmi dari sekolah.

---

## 2. Kendala Teknis Pengunggahan Berkas (Upload Foto/Dokumen)

### Kenapa setiap upload file foto atau dokumen selalu gagal atau tidak bisa ya?
Jika mengalami kegagalan saat mengunggah foto atau dokumen di portal pendaftaran seleksi UM, periksa beberapa ketentuan teknis berikut:
1. **Format File:** Pastikan format file sesuai yang diminta (format **JPG/JPEG** untuk pasfoto, dan format **PDF** untuk dokumen berkas).
2. **Ukuran File Maksimal:** Ukuran pasfoto dan dokumen maksimal adalah **2 MB (2.048 KB)**. Jika melebihi batas, lakukan kompresi terlebih dahulu.
3. **Resolusi & Dimensi Foto:** Pasfoto wajib berukuran standar **4x6 cm** atau beresolusi **800 x 600 pixel** dengan posisi tegak (*portrait*), berpakaian sopan/rapi, wajah tampak jelas, dan latar belakang (*background*) polos (warna merah atau biru).
4. **Nama File Dokumen:** Hindari penamaan file yang menggunakan karakter khusus atau simbol aneh (seperti `@, #, $, %, &, *, /, \\`). Gunakan nama file standar (contoh: `Pasfoto_NamaLengkap.jpg` atau `Raport_NamaLengkap.pdf`).
5. **Koneksi & Cache:** Gunakan peramban (*browser*) Chrome versi terbaru pada komputer/laptop, serta bersihkan *cache/cookies* browser jika halaman mengalami macet (*stuck*).

---

## 3. Solusi Kendala Kolom Isian Formulir Biodata

### Untuk kolom Alamat di Malang jika saya belum ada tempat tinggal bagaimana ya?
Jika saat ini Anda belum memiliki tempat tinggal, kos, atau asrama di Kota Malang, Anda dapat mengisikan kolom Alamat di Malang dengan **alamat tempat tinggal atau domisili asal Anda saat ini**. Data ini dapat diperbarui kembali saat Anda resmi diterima dan telah menetap di Malang.

### Bagaimana jika pekerjaan orang tua tidak ada pada pilihan menu dropdown?
Jika jenis pekerjaan orang tua Anda tidak tercantum secara spesifik pada daftar pilihan menu *dropdown*, silakan pilih opsi jenis pekerjaan yang **paling serupa, sejenis, atau mendekati** dengan pekerjaan asli orang tua Anda (contoh: untuk wiraswasta skala kecil/pedagang dapat memilih sektor Wiraswasta/Perdagangan, untuk pekerja harian lepas dapat memilih Buruh/Pekerja Lepas).

### Bagaimana jika data NISN saya tidak terdeteksi atau tidak sinkron dengan data Dapodik?
Pastikan NISN (Nomor Induk Siswa Nasional) yang diinputkan terdiri dari 10 digit angka yang sesuai dengan data di kartu NISN atau data resmi Kemdikbudristek pada laman https://nisn.data.kemdikbud.go.id/. Jika masih terdapat kendala ketidaksinkronan data NISN atau asal sekolah, segera hubungi operator sekolah asal Anda atau hubungi Helpdesk Seleksi Masuk UM di WhatsApp 0851-7116-7273.

---

## Tautan Resmi & Kontak Bantuan
- **Portal Seleksi PMB UM:** https://seleksi.um.ac.id/
- **Pusat Informasi Pendaftaran (Simaba):** WhatsApp 0851-7116-7273 atau 0851-2441-4488
- **Helpdesk Terpusat UM:** WhatsApp 0822-1333-4445
"""

# =========================================================================
# MODUL 2: FAQ KEUANGAN (Pembayaran, Slip Gaji Ortu, Surat Kesanggupan & KIP-K)
# =========================================================================
faq_keuangan_content = """# FAQ: Pembayaran Biaya Seleksi, Ketentuan Slip Gaji & Kebijakan KIP-K Mandiri

> **Kategori:** `keuangan`  
> **Department:** `Keuangan`  
> **Target Pengguna:** Calon Mahasiswa Baru & Orang Tua/Wali Pendaftar Universitas Negeri Malang (UM)  
> **Status:** Resmi Aktif  

---

## 1. Sistem & Tata Cara Pembayaran Biaya Pendaftaran

### Bagaimana cara bayar uang pendaftaran seleksi mandiri UM?
Pembayaran biaya pendaftaran seleksi mandiri dilakukan menggunakan **Kode Bayar** (bukan transfer nomor rekening biasa). Tata cara pembayaran mendetail dapat diakses melalui portal e-payment resmi UM: https://support.um.ac.id/topic/epayment/.
Langkah umum pembayaran:
1. Catat Kode Bayar unik yang diterbitkan oleh sistem seleksi setelah finalisasi pendaftaran.
2. Lakukan pembayaran melalui teller bank, ATM, mobile banking, atau internet banking dari bank mitra resmi UM.
3. Masukkan Kode Bayar pada menu pembayaran institusi/pendidikan Universitas Negeri Malang.
4. Simpan bukti transfer pembayaran sebagai bukti sah transaksi.

### Pembayaran biaya pendaftaran bisa dilakukan di bank apa saja dan di mana?
Pembayaran biaya pendidikan dan pendaftaran UM dapat dilakukan di seluruh wilayah Indonesia melalui **Bank Mitra Resmi UM**:
- Bank Negara Indonesia (BNI)
- Bank Rakyat Indonesia (BRI)
- Bank Tabungan Negara (BTN)
- Bank Mandiri
- Bank Jatim
- CIMB Niaga
- BTN Syariah
- Bank Syariah Indonesia (BSI)

---

## 2. Ketentuan Berkas Finansial & Slip Gaji Orang Tua

### Bagaimana jika orang tua saya tidak punya slip gaji (wiraswasta, petani, pedagang, buruh)?
Ketentuan dokumen bukti penghasilan orang tua untuk pendaftaran seleksi mandiri UM adalah sebagai berikut:
1. **PNS / TNI / POLRI / Karyawan BUMN / Karyawan Swasta Tetap:** Wajib menggunakan **Slip Gaji Resmi** atau Surat Keterangan Penghasilan yang diterbitkan dan ditandatangani oleh bendahara/instansi/perusahaan tempat bekerja.
2. **Wiraswasta / Pedagang / Petani / Nelayan / Buruh / Pekerja Lepas / Tidak Memiliki Slip Gaji:** Wajib mengunggah **Surat Keterangan Penghasilan Orang Tua** yang diterbitkan dan disahkan oleh pihak **Kelurahan atau Kepala Desa (Kades) setempat**.
3. **Surat Keterangan Penghasilan dari Desa/Kelurahan:** Surat harus mencantumkan rata-rata penghasilan kotor per bulan dan jumlah tanggungan keluarga, serta dibubuhi tanda tangan pejabat dan stempel basah/resmi kelurahan/desa.

### Dokumen rekening listrik, tagihan air PDAM, atau PBB apa yang harus diunggah?
Calon mahasiswa diminta mengunggah bukti pengeluaran rumah tangga keluarga:
- **Rekening Listrik (PLN):** Bukti pembayaran rekening listrik pascabayar bulan terakhir, atau bukti struk pembelian token listrik prabayar terakhir.
- **PBB (Pajak Bumi dan Bangunan):** Bukti pelunasan SPPT PBB rumah tinggal tahun berjalan atau tahun sebelumnya. Jika rumah kontrak/sewa, lampirkan surat keterangan sewa atau bukti bayar sewa.
- **Tagihan Air (PDAM):** Bukti pembayaran rekening air PDAM bulan terakhir (jika menggunakan sumur gali/pompa, dapat membuat surat pernyataan menggunakan air sumur pribadi).

---

## 3. Kebijakan Beasiswa KIP-Kuliah pada Jalur Seleksi Mandiri

### Untuk Jalur Seleksi Mandiri apakah bisa menggunakan KIP-Kuliah (KIP-K)?
**Kebijakan Resmi Universitas Negeri Malang:**  
Jalur Seleksi Mandiri di Universitas Negeri Malang (UM) **tidak dapat menggunakan KIP-Kuliah (KIP-K)**, kecuali program seleksi kemitraan khusus yang diumumkan secara eksplisit oleh rektorat.  
Seluruh pendaftar Seleksi Mandiri reguler **diwajibkan mengunggah Surat Pernyataan Kesanggupan Membayar Biaya Pendidikan** (UKT dan IPI).

### Di mana saya bisa mengunduh format Surat Pernyataan Kesanggupan Membayar Biaya Pendidikan Mandiri?
Format resmi dokumen Surat Pernyataan Kesanggupan Membayar Biaya Pendidikan Jalur Mandiri dapat diunduh langsung pada tautan resmi panitia seleksi:  
https://seleksi.um.ac.id/wp-content/uploads/2023/05/Surat-Pernyataan-Kesanggupan-Membayar-Biaya-Pendidikan-Mandiri-2023.pdf  
Format dokumen wajib diisi lengkap, ditandatangani di atas meterai Rp10.000 oleh orang tua/wali, lalu dipindai (*scan*) menjadi format PDF dengan ukuran maksimal 2 MB.

---

## Tautan Resmi & Kontak Layanan Keuangan
- **Panduan e-Payment UM:** https://support.um.ac.id/topic/epayment/
- **Helpdesk Keuangan & UKT:** WhatsApp 0822-1333-4445 (Hari kerja Senin–Jumat 07.30–16.00 WIB)
- **Portal Seleksi PMB UM:** https://seleksi.um.ac.id/
"""

# =========================================================================
# MODUL 3: FAQ AKADEMIK (Registrasi Online Pasca Lulus Seleksi)
# =========================================================================
faq_akademik_content = """# FAQ: Registrasi Online Mahasiswa Baru (Pasca-Lulus Seleksi) & SIAKAD

> **Kategori:** `akademik`  
> **Department:** `Akademik`  
> **Target Pengguna:** Mahasiswa Baru yang Dinyatakan Lolos Seleksi Universitas Negeri Malang (UM)  
> **Status:** Resmi Aktif  

---

## 1. Alur Registrasi Online Mahasiswa Baru

### Bagaimana proses dan alur Registrasi Online Mahasiswa Baru UM setelah dinyatakan lulus seleksi?
Bagi calon mahasiswa baru yang dinyatakan lulus seleksi (jalur SNBP, SNBT, maupun Seleksi Mandiri), alur registrasi online wajib dilakukan melalui tahapan berikut:
1. **Pengumuman Kelulusan:** Cek status kelulusan di portal resmi https://seleksi.um.ac.id/.
2. **Pembayaran Biaya Pendidikan (UKT / IPI):** Lakukan pembayaran biaya UKT sesuai penetapan kelompok menggunakan Kode Bayar melalui bank mitra resmi UM.
3. **Penerbitan NIM:** Setelah pembayaran terverifikasi oleh perbankan (sinkronisasi memakan waktu 1–3 jam kerja), sistem akan menerbitkan **Nomor Induk Mahasiswa (NIM)** 12 digit secara otomatis.
4. **Login ke Sistem Registrasi:** Buka laman https://registrasiv4.um.ac.id/ dan login menggunakan nomor peserta dan tanggal lahir/kata sandi yang ditentukan.
5. **Pengisian Biodata Lengkap:** Isi seluruh formulir biodata induk mahasiswa, data keluarga, riwayat kesehatan, dan unggah berkas pendukung (KTP, KK, Ijazah/SKL, dan bukti pembayaran).
6. **Unduh Bukti Registrasi:** Cetak dan unduh Formulir Biodata Registrasi Online sebagai bukti resmi Anda telah terdaftar sebagai mahasiswa baru UM.
7. **Aktivasi Akun SIAKAD:** Lakukan aktivasi akun Sistem Informasi Akademik (SIAKAD) di https://siakad.um.ac.id/ untuk persiapan pengisian KRS dan perkuliahan.

---

## 2. Kendala Registrasi Online Setelah Pembayaran UKT

### Kenapa setelah bayar UKT status saya di web registrasi masih belum lunas atau NIM belum keluar?
Penerbitan NIM dan perubahan status pembayaran pada web registrasi membutuhkan proses sinkronisasi transaksi dari server perbankan ke sistem akademik UM:
1. **Waktu Tunggu Sinkronisasi:** Tunggu sekitar **1 s.d. 3 jam kerja** setelah transaksi pembayaran berhasil didebet.
2. **Cek Bukti Transaksi:** Pastikan Kode Bayar yang diinputkan saat pembayaran di bank sudah benar dan transaksi berstatus berhasil (*sukses*).
3. **Eskalasi Kendala:** Jika setelah lebih dari 3 jam status pembayaran belum berubah menjadi lunas, segera hubungi **Helpdesk Registrasi Mahasiswa Baru** melalui WhatsApp resmi di nomor **0813-3344-400** dengan melampirkan foto/struk bukti bayar yang sah.

---

## Tautan Resmi & Kontak Bantuan Registrasi
- **Portal Registrasi Mahasiswa Baru:** https://registrasiv4.um.ac.id/
- **Portal Akademik SIAKAD:** https://siakad.um.ac.id/
- **Helpdesk Registrasi Maba:** WhatsApp 0813-3344-400 (Khusus chat pada hari dan jam kerja operasional)
- **Helpdesk Terpusat UM:** WhatsApp 0822-1333-4445
"""

# Tulis ketiga file ke lokasi kategorinya masing-masing
p1 = os.path.join(TARGET_DIR, '01_PMB_Penerimaan_Mahasiswa_Baru', 'FAQ_Pendaftaran_Mandiri_dan_Kendala_Form.md')
p2 = os.path.join(TARGET_DIR, '02_Keuangan_dan_Biaya_Pendidikan', 'FAQ_Pembayaran_Biaya_Slip_Gaji_dan_KIPK.md')
p3 = os.path.join(TARGET_DIR, '03_Akademik_dan_SIAKAD', 'FAQ_Registrasi_Online_Maba_Lulus_Seleksi.md')

with open(p1, 'w', encoding='utf-8') as f:
    f.write(faq_pmb_content.strip() + '\n')
print(f"[CREATED] {p1}")

with open(p2, 'w', encoding='utf-8') as f:
    f.write(faq_keuangan_content.strip() + '\n')
print(f"[CREATED] {p2}")

with open(p3, 'w', encoding='utf-8') as f:
    f.write(faq_akademik_content.strip() + '\n')
print(f"[CREATED] {p3}")

# Pindahkan file monolitik campur FAQ lama ke arsip
archive_dir = os.path.join(TARGET_DIR, '_ARSIP_VERSI_LAMA_DAN_DUPLIKAT')
if os.path.exists(src_faq):
    dest_archive = os.path.join(archive_dir, 'FAQ _ INFORMASI DAFTAR PERTANYAAN UMUM YANG SERING DISAMPAIKAN.md')
    shutil.move(src_faq, dest_archive)
    print(f"[ARCHIVED] File FAQ campur monolitik telah dipindahkan ke arsip: {dest_archive}")

print("\n" + "="*60)
print("PEMILAHAN FAQ CAMPUR BERHASIL DISELESAIKAN!")
print("1. FAQ PMB       -> 01_PMB_Penerimaan_Mahasiswa_Baru/FAQ_Pendaftaran_Mandiri_dan_Kendala_Form.md")
print("2. FAQ Keuangan  -> 02_Keuangan_dan_Biaya_Pendidikan/FAQ_Pembayaran_Biaya_Slip_Gaji_dan_KIPK.md")
print("3. FAQ Akademik  -> 03_Akademik_dan_SIAKAD/FAQ_Registrasi_Online_Maba_Lulus_Seleksi.md")
print("="*60)
