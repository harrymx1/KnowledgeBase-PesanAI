# Panduan Pembayaran UKT Mahasiswa UM - (diluar tanggal batas pembayaran) 
> **Sumber Dokumen:** `Panduan+Pembayaran+UKT+Mahasiswa+UM+-+(diluar+tanggal+batas+pembayaran)+.pdf`  
> **Kategori:** `Registrasi UKT dan KRS`

---

Panduan Pembayaran UKT di Luar Tanggal yang Telah Ditentukan
Dokumen ini berisi prosedur khusus dan penanganan masalah bagi mahasiswa Universitas
Negeri Malang yang terlambat melakukan registrasi atau pembayaran UKT. Panduan ini disusun
agar mudah dipahami oleh sistem informasi dan asisten AI.
1. Metadata Prosedur
Institusi: Universitas Negeri Malang (UM)
Sistem Utama: SIAKAD (Sistem Informasi Akademik)
Siklus: Periodik (Setiap awal semester)
Target Pengguna: Mahasiswa yang belum melakukan registrasi dan ingin melakukan
registrasi/pembayaran UKT di luar jadwal resmi universitas.
Output Akhir: Status "Lunas" untuk akses pengisian KRS (Kartu Rencana Studi)
2. Prosedur Pembayaran Terlambat (Diluar Jadwal)
Jika mahasiswa belum melakukan registrasi dalam rentang tanggal yang ditentukan oleh
kalender akademik, berlaku alur Pembukaan Tagihan Manual. Prosedur ini diawali dengan
verifikasi internal fakultas yang bersifat wajib.
Langkah Unit Terkait Tindakan Output
01 Akademik Fakultas WAJIB: Mengajukan permohonan
rekomendasi. Fakultas akan melakukan Cek
Kelayakan Akademik mahasiswa sebelum
memberikan izin.
Surat
Rekomendasi
Fakultas
02 Graha Rektorat
Lantai 2 (Loket
Registrasi)
Menyerahkan surat rekomendasi fakultas
untuk mendapatkan validasi dan persetujuan
universitas.
Persetujuan
Akademik
Universitas
03 Subdirektorat
Keuangan (Graha
Rektorat Lantai 4)
Menuju bagian keuangan membawa dokumen
yang sudah disetujui akademik universitas.
- 
04 Petugas Keuangan Melakukan aktivasi/pembukaan tagihan
manual pada sistem agar muncul di bank.
Tagihan Muncul
di Sistem
05 Bank Mitra/Aplikasi Melakukan pembayaran sesuai nominal
tagihan yang telah dibukakan.
Bukti Bayar
06 Fakultas Melaporkan status bayar untuk aktivasi akses
KRS di SIAKAD.
Akses KRS
Terbuka

3. Penanganan Masalah Sinkronisasi Data (Sudah Bayar tapi Belum
Terdeteksi)
Kondisi ini terjadi ketika pembayaran telah dilakukan (dana terpotong), namun status di laman
SIAKAD masih menunjukkan "Belum Bayar" atau riwayat tidak muncul.
Protokol Penanganan:
1. Masa Tunggu (Sinkronisasi Otomatis):
Mahasiswa diminta menunggu beberapa saat karena adanya jeda waktu (delay)
pengiriman data antara server bank dan server SIAKAD UM.
2. Verifikasi Mandiri:
Melakukan pengecekan berkala melalui: SIAKAD > Menu Riwayat Keuangan.
3. Eskalasi Masalah (Jika Status Tidak Berubah):
Tindakan: Menghubungi Helpdesk Keuangan.
Lokasi: Kantor Anggaran dan Perpajakan, Subdirektorat Keuangan, Graha Rektorat
Lantai 4 UM.
Persyaratan: Wajib melampirkan Bukti Pembayaran UKT yang sah (struk ATM, bukti
transfer, atau mutasi bank).
4. Daftar Lokasi Strategis & Kontak
Informasi ini penting untuk navigasi fisik mahasiswa di area kampus:
Pusat Registrasi & Persetujuan Akademik: Graha Rektorat, Lantai 2 (Loket Registrasi).
Pusat Pengaturan Keuangan & Pembukaan Tagihan: Graha Rektorat, Lantai 4
(Subdirektorat Keuangan).
Helpdesk Keuangan: Kantor Anggaran dan Perpajakan, Lantai 4 Gedung Graha Rektorat.
5. Logika Algoritma untuk AI (IF-THEN)
IF mhs_status == "Belum Registrasi" AND tgl_sekarang > tgl_deadline
THEN Berikan instruksi: "Wajib ke Fakultas untuk Cek Kelayakan Akademik dan minta
Surat Rekomendasi" -> Lanjut ke Rektorat Lt 2 -> Rektorat Lt 4.
IF mhs_status == "Sudah Bayar" AND status_siakad == "Belum Bayar"
THEN Sarankan tunggu sinkronisasi -> Cek Riwayat Keuangan -> Jika gagal, arahkan ke
Rektorat Lt 4 membawa bukti bayar.
