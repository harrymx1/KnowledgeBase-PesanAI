# KB Evaluasi PBM - Registrasi - KRS 2
> **Sumber Dokumen:** `KB+Evaluasi+PBM+-+Registrasi+-+KRS+2.pdf`  
> **Kategori:** `Informasi Penerimaan Maba`

---

KNOWLEDGE BASE — PENGISIAN EVALUASI PBM (PROSES BELAJAR MENGAJAR) DI SIAKAD AI ASSIST
MEKARI QONTAK — UNIVERSITAS NEGERI MALANG (UM) Segmen: MAHASISWA AKTIF (bukan calon
mahasiswa baru/masyarakat umum)
Sumber:
1. Screenshot langsung antarmuka siakad.um.ac.id (14 Agustus 2026) — halaman "Hasil Studi
Semester" dan form "Isi Evaluasi PBM".
2. Alur langkah dari pengguna (admin/staf UM), konsisten dengan screenshot.
3. Tautan Instagram Reel yang disertakan pengguna TIDAK dapat diakses/diekstrak (konten video,
di luar kemampuan pengambilan teks) — TIDAK dijadikan sumber narasi ini, sesuai prinsip tidak
mengarang isi dari sumber yang tidak terverifikasi.
4. Screenshot tabel Kalender Akademik UM 2025/2026 (baris E.3 — jadwal resmi evaluasi PBM)
dari https://um.ac.id/wp-content/uploads/2025/05/Kalender-Akademik-2025-2026-1.pdf — link
PDF-nya sendiri TIDAK bisa diekstrak via fetch (kemungkinan hasil scan, sama seperti dokumen
um.ac.id lain), sehingga hanya bagian yang terlihat di screenshot yang dijadikan acuan, BUKAN
keseluruhan isi kalender akademik.
5. Konsekuensi keterlambatan pengisian & solusinya, dari konfirmasi admin/staf UM langsung (14
Agustus 2026). Tanggal ekstraksi: 14 Agustus 2026.
STATUS PER TANGGAL ACUAN (14 Agustus 2026): saat ini SEDANG BERJALAN Semester GENAP
2025/2026 (bukan Gasal). Sesuai tabel Kalender Akademik: jendela pengisian evaluasi PBM Semester
Genap 2025/2026 adalah 18 Mei – 02 Juni 2026 (SUDAH LEWAT per tanggal acuan ini), dan batas akhir
pengisian Nilai (DNA) Semester Genap 2025/2026 adalah 26 Januari – 13 Agustus 2026 (BARU SAJA
BERAKHIR KEMARIN per tanggal acuan ini). Artinya, mahasiswa yang BELUM mengisi evaluasi PBM
Semester Genap 2025/2026 saat ini SUDAH masuk skenario "terlambat" (lihat Bagian B.2) — Semester
Gasal 2026/2027 adalah "semester berikutnya" yang dimaksud dalam skema solusi keterlambatan tsb.
Admin WAJIB memperbarui tanggal acuan ini saat semester berganti.
Posisi pemasangan yang disarankan: cabang "Mahasiswa & Alumni" (Node 1B) → Pendidikan →
Akademik (topik Hasil Studi Semester/Evaluasi PBM) — salah satu node "Akademik Fakultas" yang
menurut Spesifikasi_Alur_Bot_Layanan_Satu_Atap.md saat ini masih Default Fallback tanpa KB.
===================================================================

## A. Aturan Penjawaban Ai Assist

1. Evaluasi PBM adalah kuesioner penilaian PROSES BELAJAR MENGAJAR (kinerja dosen &
pelaksanaan RPS) per matakuliah yang ditempuh mahasiswa pada suatu semester — BUKAN
nilai/IP mahasiswa itu sendiri, meski keduanya ditampilkan di halaman & proses yang sama.
2. AI Assist TIDAK dapat mengisikan evaluasi PBM atas nama mahasiswa, TIDAK dapat
melihat/mengonfirmasi status pengisian evaluasi PBM milik mahasiswa tertentu (ini data pribadi
— lihat Ketentuan_Umpan_Balik_Pertanyaan_Tidak_Lengkap_dan_Data_Pribadi.md Bagian B).
AI hanya menjelaskan CARA mengisi, bukan memproses/mengecekkan punya siapa pun.

3. Jangan mengarang isi lengkap seluruh 15 pertanyaan kuesioner jika ditanya — dokumen ini
hanya mencatat CONTOH pertanyaan yang terlihat di screenshot (13 pertanyaan skala + 2 esai),
kemungkinan jumlah/redaksi bisa berbeda per matakuliah/dosen. Sampaikan gambaran umum
formatnya, bukan mendiktekan isi pasti tiap soal.
4. Panjang jawaban 2-4 kalimat per topik.
===================================================================

## B. Apa Itu Evaluasi Pbm & Kenapa Penting

1. Evaluasi PBM adalah kuesioner penilaian mahasiswa terhadap pelaksanaan perkuliahan &
kinerja dosen pengampu, untuk setiap matakuliah yang ditempuh dalam 1 semester.
2. PENTING: pengisian evaluasi PBM berkaitan dengan MUNCULNYA NILAI/IP mahasiswa untuk
semester tersebut. Sesuai notifikasi resmi di SIAKAD: "Perubahan status pengisian evaluasi PBM
dan Nilai IP dilakukan H+1" — artinya status evaluasi maupun nilai IP TIDAK langsung update
saat itu juga, tapi diproses keesokan harinya (H+1).
3. Mahasiswa yang belum mengisi evaluasi PBM untuk suatu matakuliah akan melihat tombol "Isi
evaluasi PBM" di baris matakuliah tersebut. Setelah diisi, tombol berubah jadi status "Evaluasi
PBM sudah diisi" beserta cap waktu pengiriman (contoh: "wkt kirim: 14 Agt 2026 00:08:46").
Contoh jawaban singkat: "Evaluasi PBM adalah kuesioner penilaian Anda terhadap perkuliahan dan
kinerja dosen untuk tiap matakuliah di semester tersebut. Pengisiannya penting karena terkait
munculnya nilai/IP semester Anda, dan status pembaruannya baru berubah H+1 (besok) setelah diisi,
bukan langsung saat itu juga."
===================================================================
B.1 — JADWAL RESMI PENGISIAN (Kalender Akademik UM 2025/2026)
Sesuai Kalender Akademik UM 2025/2026, bagian E "Kegiatan Akhir Semester" poin 3: "Evaluasi PBM
terhadap dosen dilakukan oleh mahasiswa secara online (mulai UAS s.d. sebelum KHS)":
- Semester Gasal 2025/2026: 16 Desember 2025 – 06 Januari 2026.
- Semester Genap 2025/2026: 18 Mei – 02 Juni 2026. Jendela waktu ini SELALU dimulai sejak
masa UAS dan berakhir SEBELUM tanggal terbit KHS (Kartu Hasil Studi) Online semester tersebut
— di luar jendela ini, evaluasi normalnya tidak bisa diisi pada periode semester yang sama (lihat
konsekuensi & solusi jika telat di Bagian B.2).
Contoh jawaban singkat: "Pengisian evaluasi PBM untuk semester genap 2025/2026 dibuka 18 Mei – 02
Juni 2026, dan untuk semester gasal 16 Desember 2025 – 06 Januari 2026 — selalu mulai dari masa UAS
sampai sebelum KHS terbit."
===================================================================

## B.2 — Jika Terlambat Mengisi: Konsekuensi & Solusi (Penting)

KONSEKUENSI jika mahasiswa tidak mengisi evaluasi PBM dalam jendela waktu resminya (Bagian B.1):
1. Mahasiswa TIDAK BISA mengecek nilai akhir DNA (Daftar Nilai Akhir) pada akhir semester
tersebut.
2. Mahasiswa TIDAK BISA melakukan KRS (Kartu Rencana Studi) online pada SEMESTER
BERIKUTNYA — ini konsekuensi paling krusial karena berdampak ke semester baru, bukan cuma
semester yang terlewat.
SOLUSI (langkah pemulihan di semester berikutnya):
1. Mahasiswa TETAP menunggu sampai semester berikutnya tiba — TIDAK ADA cara mengisi
evaluasi PBM di luar jendela waktu pada semester yang sama setelah lewat.
2. Melakukan registrasi & pembayaran UKT semester berikutnya seperti biasa.
3. Saat masa KRS semester berikutnya tiba, buka kembali menu Akademik > Hasil Studi Semester di
SIAKAD, lihat kolom untuk semester yang TERLEWAT (semester lampau) — jika tombol "Isi
Evaluasi PBM" MASIH muncul di situ, isi evaluasi tersebut.
4. WAJIB mengisi evaluasi PBM untuk SEMUA matakuliah di semester lampau yang belum terisi
(bukan hanya sebagian) — lihat Bagian C untuk cara mengisi per matakuliah.
5. Setelah SELESAI mengisi seluruh evaluasi yang tertunggak, WAJIB MENUNGGU 1 x 24 JAM (H+1)
sebelum sistem mengizinkan KRS Online — ini konsisten dengan notifikasi resmi SIAKAD
"Perubahan status pengisian evaluasi PBM dan Nilai IP dilakukan H+1" (lihat Bagian B).
6. Setelah masa tunggu 24 jam terlewati, mahasiswa BARU BISA melakukan KRS Online seperti
biasa.
Contoh jawaban singkat: "Kalau telat mengisi evaluasi PBM, dampaknya Anda tidak bisa cek nilai DNA
akhir semester DAN tidak bisa KRS online di semester berikutnya. Solusinya: tunggu semester depan,
registrasi & bayar UKT seperti biasa, lalu saat masa KRS tiba cek Hasil Studi Semester — kalau tombol Isi
Evaluasi PBM masih muncul untuk semester lampau, isi semuanya. Setelah itu tunggu 1x24 jam, baru
KRS Online bisa dilakukan."
===================================================================

## C. Langkah-Langkah Pengisian

1. Buka laman resmi SIAKAD UM di https://siakad.um.ac.id melalui browser.
2. Login menggunakan NIM (nama pengguna) dan kata sandi Anda.
3. Masuk ke menu "Akademik" pada sidebar kiri, lalu pilih "Hasil Studi Semester".
4. Sistem menampilkan daftar matakuliah yang ditempuh pada periode tersebut (kode, nama
matakuliah, SKS, kelas-offering), beserta ringkasan Jumlah SKS (dan IP, jika sudah tersedia).
5. Untuk matakuliah yang evaluasinya BELUM diisi, klik tombol merah "Isi evaluasi PBM" pada baris
matakuliah yang bersangkutan.
6. Sistem menampilkan detail matakuliah (Kode, Nama Matakuliah, SKS, Kelas-Offr, Dosen) diikuti
daftar pertanyaan kuesioner.
7. Jawab seluruh pertanyaan kuesioner secara jujur dan objektif — mayoritas berupa skala
penilaian 4 poin: Sangat Baik (Excellent), Baik (Very Good), Cukup Baik (Good), Kurang Baik
(Poor); ditambah 2 pertanyaan esai terbuka di bagian akhir (pengalaman baik selama
matakuliah, dan saran/masukan perbaikan).
8. Setelah seluruh pertanyaan terisi, klik tombol biru "Simpan" untuk mengirimkan evaluasi
(tombol "Batal" membatalkan pengisian).
9. Ulangi langkah 5-8 untuk setiap matakuliah yang masih menampilkan tombol "Isi evaluasi PBM"
— evaluasi diisi PER MATAKULIAH, bukan sekali untuk semua matakuliah sekaligus.
10. Setelah semua matakuliah berstatus "Evaluasi PBM sudah diisi", pastikan menunggu H+1 untuk
melihat pembaruan status dan nilai IP semester secara lengkap.
Contoh jawaban singkat: "Login ke siakad.um.ac.id dengan NIM dan password, buka menu Akademik >
Hasil Studi Semester, lalu klik tombol 'Isi evaluasi PBM' pada tiap matakuliah yang belum diisi. Jawab
seluruh pertanyaan kuesioner (skala penilaian + 2 pertanyaan esai) dengan jujur, lalu klik Simpan. Ulangi
untuk semua matakuliah, dan nilai IP semester akan update H+1 setelahnya."
===================================================================

## D. Gambaran Isi Kuesioner (Contoh, Bukan Daftar Pasti/Lengkap)

Berdasarkan screenshot yang tersedia, kuesioner terdiri dari sekitar 13 pertanyaan skala 4 poin (Sangat
Baik/Baik/Cukup Baik/Kurang Baik) seputar pelaksanaan RPS (Rencana Pembelajaran Semester) dan
kinerja dosen, di antaranya menyangkut:
- Penyampaian & pembahasan RPS oleh dosen di awal perkuliahan.
- Kesesuaian RPS dengan capaian matakuliah & kompetensi lulusan.
- Strategi pembelajaran & metode penilaian berbasis proyek/kasus dalam RPS.
- Umpan balik dosen terhadap kinerja mahasiswa untuk kemajuan belajar.
- Kesesuaian tugas-tugas dengan capaian matakuliah & kompetensi lulusan.
- Cakupan penilaian (ujian tengah & akhir semester, serta pengumpulan proyek/produk/dokumen
akhir). Ditutup dengan 2 pertanyaan esai terbuka: pengalaman baik selama matakuliah, dan
saran/masukan perbaikan perkuliahan mendatang.
CATATAN: nomor soal yang terlihat di screenshot adalah 1-3 dan 11-15 — kemungkinan ada soal 4-10
yang tidak tertangkap di screenshot yang tersedia. AI Assist TIDAK BOLEH memastikan jumlah total soal
secara pasti (kemungkinan lebih dari 15) — cukup sampaikan gambaran format & tema pertanyaannya.
Contoh jawaban singkat: "Kuesioner evaluasi PBM berisi pertanyaan skala (Sangat Baik s.d. Kurang Baik)
seputar pelaksanaan RPS, kesesuaian tugas dengan capaian matakuliah, dan umpan balik dosen, ditutup
2 pertanyaan esai tentang pengalaman dan saran Anda. Jumlah pastinya bisa bervariasi per matakuliah."
===================================================================

## E. Keterbatasan Data

1. Tautan Instagram Reel yang disertakan pengguna tidak dapat diakses/diekstrak kontennya
(video), sehingga TIDAK menjadi bagian sumber narasi ini.
2. Jumlah total pertanyaan kuesioner tidak terkonfirmasi pasti (soal 4-10 tidak terlihat di
screenshot yang tersedia) — lihat Bagian D.
3. Belum ada informasi apakah ada batas waktu (deadline) pengisian evaluasi PBM per semester,
atau konsekuensi jika tidak diisi sama sekali (selain nilai IP yang mungkin tertunda tampil) — AI
Assist TIDAK BOLEH mengarang kebijakan ini, arahkan ke Kasubag Akademik Fakultas jika
ditanya.
===================================================================

## F. Kontak Resmi

Dokumen sumber tidak mencantumkan kontak spesifik terkait evaluasi PBM. Untuk kendala teknis
SIAKAD atau pertanyaan kebijakan evaluasi PBM di luar cakupan dokumen ini, arahkan ke Kasubag
Akademik Fakultas mahasiswa yang bersangkutan.

Contoh jawaban jika di luar cakupan: "Mohon maaf, untuk detail tersebut mohon menghubungi Kasubag
Akademik Fakultas Anda, karena kebijakan teknisnya diatur di tingkat fakultas."
