import os
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, 'Knowledge_Base_MD')
TARGET_DIR = os.path.join(BASE_DIR, 'Knowledge_Base_Clean_Categorized')

# 1. Definisi 5 Kategori Master + 1 Folder Materi Visual
CATEGORIES = {
    '01_PMB_Penerimaan_Mahasiswa_Baru': os.path.join(TARGET_DIR, '01_PMB_Penerimaan_Mahasiswa_Baru'),
    '02_Keuangan_dan_Biaya_Pendidikan': os.path.join(TARGET_DIR, '02_Keuangan_dan_Biaya_Pendidikan'),
    '03_Akademik_dan_SIAKAD': os.path.join(TARGET_DIR, '03_Akademik_dan_SIAKAD'),
    '04_Layanan_Kampus_dan_Sarpras': os.path.join(TARGET_DIR, '04_Layanan_Kampus_dan_Sarpras'),
    '05_Helpdesk_dan_Eskalasi': os.path.join(TARGET_DIR, '05_Helpdesk_dan_Eskalasi'),
    '06_Materi_Visual_dan_Lampiran_PDF': os.path.join(TARGET_DIR, '06_Materi_Visual_dan_Lampiran_PDF'),
    '_ARSIP_VERSI_LAMA_DAN_DUPLIKAT': os.path.join(TARGET_DIR, '_ARSIP_VERSI_LAMA_DAN_DUPLIKAT'),
    '_ARSIP_NOISE_OUT_OF_SCOPE': os.path.join(TARGET_DIR, '_ARSIP_NOISE_OUT_OF_SCOPE')
}

# 2. Mapping Penempatan Seluruh 98 File secara Akurat & Objektif
FILE_MAPPING = {
    # === NOISE / OUT OF SCOPE ===
    'Pengumuman Penerimaan Dosen 20 Februari -  7 April 2026..md': ('_ARSIP_NOISE_OUT_OF_SCOPE', 'Rekrutmen dosen sudah tutup & bukan sasaran mahasiswa/calon mahasiswa'),
    'Peniadaan Car Free Day.md': ('_ARSIP_NOISE_OUT_OF_SCOPE', 'Pengumuman insidental lokal non-akademik'),

    # === MATERI VISUAL & PDF ASLI ===
    'SKB_Libur_Nasional_dan_Cuti_Bersama_Tahun_2026.pdf': ('06_Materi_Visual_dan_Lampiran_PDF', 'Dokumen scan resmi SKB Menteri'),
    'Transfer_Knowledge (1).pdf': ('06_Materi_Visual_dan_Lampiran_PDF', 'Dokumen transfer knowledge 77 halaman banyak diagram visual'),
    'Transfer_Knowledge (2)_compressed.pdf': ('06_Materi_Visual_dan_Lampiran_PDF', 'Dokumen transfer knowledge 257 halaman infografis & link media'),

    # === ARSIP VERSI LAMA / DUPLIKAT (Tersortir berdasarkan temuan SSOT) ===
    r'Informasi Penerimaan Maba\KB_SM_Jalur_Skor_UTBK_UM.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Versi awal; telah digantikan oleh Revisi Gelombang 4'),
    r'Informasi Penerimaan Maba\KB_SM_Jalur_Skor_UTBK_UM (1).md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Draft lama; telah digantikan oleh Revisi Gelombang 4'),
    r'Informasi Penerimaan Maba\KB_SM_Jalur_Skor_UTBK_UM_ Tambahan Gelombang 4.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Duplikat draft; disatukan ke Revisi Gelombang 4'),
    r'Informasi Penerimaan Maba\SELEKSI MANDIRI JALUR SKOR UTBK.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Draft awal; telah digantikan oleh Revisi Gelombang 4'),
    r'Informasi Penerimaan Maba\SM_Jalur_Skor_UTBK_UM.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Draft awal; telah digantikan oleh Revisi Gelombang 4'),
    r'Informasi Penerimaan Maba\KB Akselerasi Internal UM.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Versi lama; telah digantikan oleh KNOWLEDGE_BASE_ALL_PENERIMAAN_MABA (TRIASE)'),
    r'Informasi Penerimaan Maba\kb_akselerasi_internal.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Versi lama; telah digantikan oleh KNOWLEDGE_BASE_ALL_PENERIMAAN_MABA (TRIASE)'),
    r'Informasi Penerimaan Maba\KB_SM_RPL_Magister_UM.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Versi awal; telah digantikan oleh KB_SM_RPL_Magister_UM (1)'),
    r'Informasi Penerimaan Maba\KB_SM_Magister_Reguler_UM.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Draft awal 7 hal; telah digantikan oleh KB_SM_Magister_Reguler_UM (1) 11 hal'),
    r'Informasi Penerimaan Maba\kb_sm_doktor_by_research.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Versi 8 hal; telah digantikan oleh KB SM Doktor By Research UM 11 hal'),
    r'Informasi Penerimaan Maba\kb_sm_doktor_reguler.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Versi 8 hal; telah digantikan oleh KB SM Doktor Reguler UM 12 hal'),
    r'Informasi Penerimaan Maba\KB_SNBT_UM.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Versi draf awal; telah diperbarui di KB_SNBT_UM (1)'),
    r'Informasi Penerimaan Maba\knowledge-source_19-01-2026.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Versi awal 19 Januari; telah digantikan oleh knowledge-source new / Knowledge Source New Revisi 1'),
    r'Informasi Penerimaan Maba\knowledge source dinamis kemahasiswaan.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Versi awal 23 hal; telah digantikan oleh knowledge source dinamis kemahasiswaan-REV 1 (2) 24 hal'),
    r'Panduan Siakad\2) Panduan Aktifasi Akun Siakad UM untuk Mahasiswa Baru UM (1).md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Duplikat persis file 2) Panduan Aktifasi Akun Siakad'),
    r'Panduan Siakad\2) Panduan Siakad Mahasiswa.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Duplikat file 1) Panduan Siakad Mahasiswa'),
    r'Registrasi UKT dan KRS\KB_Registrasi_Mahasiswa_Semester_Gasal_2026_2027_UM (1).md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Versi awal 5 hal; telah digantikan oleh versi (2) 7 hal'),
    r'Registrasi UKT dan KRS\Registrasi Gasal 2026.md': ('_ARSIP_VERSI_LAMA_DAN_DUPLIKAT', 'Draft awal; telah disatukan di KB_Registrasi_Mahasiswa_Semester_Gasal_2026_2027_UM (2)'),

    # === KATEGORI 01: PMB PENERIMAAN MAHASISWA BARU (DOKUMEN UTUH & MUTAKHIR) ===
    '1. Pengumuman Pasca Kegiatan Pendaftaran Maba.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Pedoman kegiatan pasca pendaftaran mahasiswa baru'),
    'DAYA TAMPUNG PROGRAM STUDI & JADWAL SELEKSI MABA UM 2026.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Daya tampung lengkap seluruh prodi dan jadwal seleksi'),
    r'Informasi Penerimaan Maba\KB_SNBP_UM.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge Base resmi jalur SNBP'),
    r'Informasi Penerimaan Maba\KB_SNBT_UM (1).md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge Base resmi jalur SNBT mutakhir'),
    r'Informasi Penerimaan Maba\KB_Jalur_Pendaftaran_SM_2026 (revisi).md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Master Knowledge Base seluruh Jalur Seleksi Mandiri UM 2026'),
    r'Informasi Penerimaan Maba\KB_SM_Jalur_Skor_UTBK_UM  Revisi gel. 4.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge Base resmi Seleksi Mandiri Skor UTBK Gelombang 4'),
    r'Informasi Penerimaan Maba\SELEKSI MANDIRI JALUR SKOR UTBK V4.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Panduan teknis seleksi mandiri skor UTBK versi 4'),
    r'Informasi Penerimaan Maba\Pedoman Seleksi Mandiri Jalur Skor UTBK UM 2026.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Pedoman resmi pendaftaran jalur skor UTBK'),
    r'Informasi Penerimaan Maba\Pedoman Seleksi Mandiri Jalur Prestasi UM 2026.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Pedoman seleksi mandiri prestasi raport/kejuaraan'),
    r'Informasi Penerimaan Maba\SELEKSI MANDIRI JALUR PRESTASI.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Panduan teknis lengkap syarat prestasi kejuaraan/portofolio'),
    r'Informasi Penerimaan Maba\KB_SM_Jalur_Prestasi_UM_1.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge Base detail jalur prestasi UM'),
    r'Informasi Penerimaan Maba\Pedoman Seleksi Mandiri Jalur Tes Masuk Berbasis Komputer (TMBK).md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Pedoman seleksi mandiri TMBK'),
    r'Informasi Penerimaan Maba\SELEKSI MANDIRI JALUR TES MASUK BERBASIS KOMPUTER.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Panduan teknis ujian komputer mandiri TMBK'),
    r'Informasi Penerimaan Maba\KB_SM_Jalur_TMBK_UM.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge base jalur TMBK'),
    r'Informasi Penerimaan Maba\Pedoman Seleksi Mandiri Jalur Leadership UM 2026.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Pedoman seleksi mandiri jalur kepemimpinan / ketua OSIS'),
    r'Informasi Penerimaan Maba\KB_SM_Jalur_Leadership_UM.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge Base jalur leadership UM'),
    r'Informasi Penerimaan Maba\Pedoman Seleksi Mandiri Kemitraan UM.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Pedoman seleksi mandiri kemitraan'),
    r'Informasi Penerimaan Maba\KB_SM_Jalur_Kemitraan_Mitra_Asuh_UM.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge Base seleksi jalur kemitraan mitra asuh'),
    r'Informasi Penerimaan Maba\kb_kemitraan_institusi.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge base kemitraan institusi'),
    r'Informasi Penerimaan Maba\kb_kemitraan_outbound_mobility.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge base kemitraan pertukaran pelajar outbound'),
    r'Informasi Penerimaan Maba\KB_SM_Jalur_Bapres_PPMI_UM.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge Base jalur beasiswa prestasi PPMI'),
    r'Informasi Penerimaan Maba\SELEKSI MANDIRI KELAS INTERNASIONAL.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Panduan teknis seleksi mandiri kelas internasional'),
    r'Informasi Penerimaan Maba\KB_SM_Kelas_Internasional_UM.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge base kelas internasional'),
    r'Informasi Penerimaan Maba\KB_SM_Double_Degree_UM.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge base program gelar ganda double degree'),
    r'Informasi Penerimaan Maba\Informasi dan Panduan Seleksi Magister dan Doktor tahun 2026.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Informasi dan panduan lengkap seleksi S2 dan S3 UM'),
    r'Informasi Penerimaan Maba\KB_SM_Magister_Reguler_UM (1).md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge base seleksi mandiri magister reguler S2'),
    r'Informasi Penerimaan Maba\KB_SM_PJJ_Magister_UM.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge base magister pembelajaran jarak jauh PJJ'),
    r'Informasi Penerimaan Maba\KB SM Doktor Reguler UM.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge base seleksi mandiri doktor reguler S3'),
    r'Informasi Penerimaan Maba\KB SM Doktor By Research UM.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge base seleksi doktor berbasis riset S3'),
    r'Informasi Penerimaan Maba\KNOWLEDGE_BASE_ALL_PENERIMAAN_MABA (TRIASE).md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge base acuan fast-track akselerasi internal triase'),
    r'Informasi Penerimaan Maba\Informasi dan Panduan RPL Sarjana dan Magister Universitas Negeri Malang tahun 2026.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Informasi dan panduan RPL sarjana dan magister'),
    r'Informasi Penerimaan Maba\KB_SM_RPL_Magister_UM (1).md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge base RPL magister revisi 1'),
    r'Informasi Penerimaan Maba\KB_Status_Aksi_Template_6Juli2026.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Template baku sopan jawaban status jalur AI'),
    r'Informasi Penerimaan Maba\SELEKSI PROGRAM SARJANA DI UNIVERSITAS NEGERI MALANG TAHUN 2026.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Regulasi lengkap program sarjana UM tahun 2026'),
    r'Informasi Penerimaan Maba\KB_ProgramStudi_Fakultas_DayaTampung.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Daftar lengkap program studi fakultas dan daya tampung'),

    # === REGISTRASI ADMINISTRASI MABA (PMB) ===
    r'Informasi Penerimaan Maba\Panduan Registrasi 1 Atap SNBP 2026.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Panduan registrasi satu atap calon maba SNBP'),
    r'Informasi Penerimaan Maba\Panduan Registrasi Mahasiswa Baru Jalur Masuk SNBP.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Panduan registrasi mahasiswa baru SNBP'),
    r'Informasi Penerimaan Maba\Knowledge Base Registrasi SNBP UM.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge base registrasi SNBP'),
    r'Informasi Penerimaan Maba\Pengumuman Registrasi Administrasi Calon Mahasiswa Baru Sarjana .md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Pengumuman resmi registrasi administrasi maba sarjana'),
    r'Informasi Penerimaan Maba\Registrasi Administrasi Calon Mahasiswa Baru Universitas Negeri Malang (UM) Jalur SNBT Tahun Akademik 2026_2027.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Registrasi administrasi maba SNBT reguler'),
    r'Informasi Penerimaan Maba\Registrasi Administrasi Calon Mahasiswa Baru Universitas Negeri Malang (UM) Calon Penerima Beasiswa KIP-K Jalur SNBT Tahun Akademik 2026_2027.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Registrasi maba penerima beasiswa KIP-K SNBT'),
    r'Informasi Penerimaan Maba\Knowledge Base Registrasi Mahasiswa Baru Universitas Negeri Malang.docx.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge base teknis alur registrasi mahasiswa baru'),
    r'Informasi Penerimaan Maba\Knowledge Base FAQ REGISTRASI MAHASISWA BARU.docx.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'FAQ tanya jawab registrasi mahasiswa baru'),
    r'Informasi Penerimaan Maba\Knowledge Base FAQ REGISTRASI MAHASISWA BARU.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'FAQ resmi registrasi mahasiswa baru'),
    r'Informasi Penerimaan Maba\info s.d 24 Agustus 2026 - Pengumuman Registrasi Administrasi Calon Mahasiswa Baru Universitas Negeri Malang (UM) Jalur SNBP Tahun Akademik 2026-2027.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Pengumuman registrasi administrasi batas 24 Agustus'),

    # === KATEGORI 02: KEUANGAN DAN BIAYA PENDIDIKAN (DOKUMEN UTUH) ===
    r'Registrasi UKT dan KRS\Informasi dan Panduan Biaya Pendidikan Universitas Negeri Malang tahun 2026.md': ('02_Keuangan_dan_Biaya_Pendidikan', 'Panduan lengkap rincian biaya pendidikan UKT dan IPI per prodi'),
    r'Registrasi UKT dan KRS\KB_Biaya_UKT_IPI_Pembayaran.md': ('02_Keuangan_dan_Biaya_Pendidikan', 'Master Knowledge Base Biaya UKT IPI dan Pembayaran Bank'),
    r'Registrasi UKT dan KRS\Revisi - Knowledge Base Keuangan UM.md': ('02_Keuangan_dan_Biaya_Pendidikan', 'Knowledge Base Keuangan UM versi revisi'),
    r'Registrasi UKT dan KRS\knowledge source dinamis keuangan.md': ('02_Keuangan_dan_Biaya_Pendidikan', 'Knowledge base dinamis kebijakan keuangan'),
    r'Informasi Penerimaan Maba\KB_IPI_S1_D4_Deskriptif.md': ('02_Keuangan_dan_Biaya_Pendidikan', 'Tabel dan deskripsi nominal IPI jenjang S1 dan D4'),
    r'Registrasi UKT dan KRS\Panduan Pembayaran UKT Mahasiswa UM - (diluar tanggal batas pembayaran) .md': ('02_Keuangan_dan_Biaya_Pendidikan', 'Panduan pembayaran UKT bank dan di luar tanggal batas'),
    r'Registrasi UKT dan KRS\Panduan Permasalahan Pembayaran UKT.md': ('02_Keuangan_dan_Biaya_Pendidikan', 'SOP penanganan kendala pembayaran UKT'),
    r'Informasi Penerimaan Maba\KB Penurunan dan Penarikan UKT.md': ('02_Keuangan_dan_Biaya_Pendidikan', 'Ketentuan penurunan, keringanan, sanggah, dan batas penarikan UKT'),
    r'Informasi Penerimaan Maba\KB_FAQ_Umum_KIP_Prosedur.md': ('02_Keuangan_dan_Biaya_Pendidikan', 'Prosedur beasiswa KIP-Kuliah dan tanya jawab umum'),

    # === KATEGORI 03: AKADEMIK DAN SIAKAD (DOKUMEN UTUH) ===
    r'Panduan Siakad\1) Panduan Aktifasi Akun Siakad UM untuk Mahasiswa Baru UM.md': ('03_Akademik_dan_SIAKAD', 'Panduan aktivasi akun SIAKAD tahap 1'),
    r'Panduan Siakad\2) Panduan Aktifasi Akun Siakad UM untuk Mahasiswa Baru UM.md': ('03_Akademik_dan_SIAKAD', 'Panduan aktivasi akun SIAKAD tahap 2'),
    r'Panduan Siakad\3) Panduan Aktifasi Akun Siakad UM untuk Mahasiswa Baru UM.md': ('03_Akademik_dan_SIAKAD', 'Panduan aktivasi akun SIAKAD tahap 3'),
    r'Panduan Siakad\1) Panduan Siakad Mahasiswa.md': ('03_Akademik_dan_SIAKAD', 'Panduan penggunaan modul SIAKAD bagi mahasiswa'),
    r'Registrasi UKT dan KRS\KB_Registrasi_Akun_SIAKAD_DaftarUlang.md': ('03_Akademik_dan_SIAKAD', 'Knowledge Base registrasi akun, login, dan kendala teknis'),
    r'Registrasi UKT dan KRS\KB_Registrasi_Mahasiswa_Semester_Gasal_2026_2027_UM (2).md': ('03_Akademik_dan_SIAKAD', 'Ketentuan registrasi mahasiswa semester gasal revisi 2'),
    r'Informasi Penerimaan Maba\KB Evaluasi PBM - Registrasi - KRS.md': ('03_Akademik_dan_SIAKAD', 'Knowledge base evaluasi proses belajar mengajar dan pengisian KRS'),
    r'Informasi Penerimaan Maba\KB Evaluasi PBM - Registrasi - KRS 2.md': ('03_Akademik_dan_SIAKAD', 'Knowledge base evaluasi PBM dan KRS versi 2'),
    r'Informasi Penerimaan Maba\KNOWLEDGE BASE CHATBOT  Semester Antara atau pendek di Universitas Negeri Malang (UM)  Intent- penjelasan_semester_antara atau pendek.docx.md': ('03_Akademik_dan_SIAKAD', 'Panduan lengkap semester antara/pendek'),
    r'Registrasi UKT dan KRS\Pembatalan Mata Kuliah  Intent- pembatalan_KRS dan  Biaya SKS semester_antara atau pendek.docx.md': ('03_Akademik_dan_SIAKAD', 'Prosedur pembatalan mata kuliah KRS dan biaya SKS'),
    r'Informasi Penerimaan Maba\KB Proses Yudisium - versi 1.md': ('03_Akademik_dan_SIAKAD', 'Knowledge Base proses dan pendaftaran yudisium'),
    r'Informasi Penerimaan Maba\KB_Legalisir_Ijazah_UM.md': ('03_Akademik_dan_SIAKAD', 'Prosedur legalisir ijazah dan pengambilan ijazah'),

    # === KATEGORI 04: LAYANAN KAMPUS DAN SARPRAS ===
    'Sarana Prasarana UM.md': ('04_Layanan_Kampus_dan_Sarpras', 'Fasilitas sarana prasarana, perpustakaan, asrama, poliklinik'),
    'KNOWLEDGE BASE PANDUAN PENGAJUAN KERJA SAMA DI UNIVERSITAS NEGERI MALANG (REV).md': ('04_Layanan_Kampus_dan_Sarpras', 'Panduan resmi pengajuan kerja sama instansi di UM'),

    # === KATEGORI 05: HELPDESK DAN ESKALASI ===
    'Helpdesk 1 Nomor.md': ('05_Helpdesk_dan_Eskalasi', 'Kebijakan resmi terpusat Helpdesk 1 Nomor UM'),
    'FAQ _ INFORMASI DAFTAR PERTANYAAN UMUM YANG SERING DISAMPAIKAN.md': ('05_Helpdesk_dan_Eskalasi', 'Kompilasi tanya jawab umum layanan sivitas'),
    r'Registrasi UKT dan KRS\Registrasi - Layanan di Loket Administrasi Sub Direktorat Layanan Pendidikan.md': ('05_Helpdesk_dan_Eskalasi', 'Prosedur layanan loket administrasi Graha Rektorat & eskalasi'),

    # === KNOWLEDGE SOURCE BESAR (MEMUAT BANYAK TOPIK CAMPURAN LENGKAP) ===
    r'Informasi Penerimaan Maba\Knowledge Source New Revisi 1.md': ('01_PMB_Penerimaan_Mahasiswa_Baru', 'Knowledge source komprehensif PMB revisi 1 (59 halaman lengkap)'),
    r'Informasi Penerimaan Maba\knowledge source dinamis kemahasiswaan-REV 1 (2).md': ('04_Layanan_Kampus_dan_Sarpras', 'Knowledge source kemahasiswaan & layanan terpadu (24 halaman lengkap)'),
    r'Informasi Penerimaan Maba\knowledge-source new.md': ('03_Akademik_dan_SIAKAD', 'Knowledge source akademik, fasilitas & peraturan rektor (84 halaman lengkap)'),
    'knowledger_source_statis.md': ('05_Helpdesk_dan_Eskalasi', 'Knowledge source statis profil dan layanan UM')
}

def execute():
    print("Memulai rekonstruksi Knowledge_Base_Clean_Categorized (100% Data Preservation)...")
    if os.path.exists(TARGET_DIR):
        shutil.rmtree(TARGET_DIR)
    for path in CATEGORIES.values():
        os.makedirs(path, exist_ok=True)

    copied = 0
    missing = 0
    total_text_copied = 0

    for rel_path, (cat_key, note) in FILE_MAPPING.items():
        src_file = os.path.join(SRC_DIR, rel_path)
        dest_folder = CATEGORIES[cat_key]
        dest_file = os.path.join(dest_folder, os.path.basename(rel_path))

        if os.path.exists(src_file):
            # Salin file UTUH 100% tanpa pemotongan satu karakter pun!
            shutil.copy2(src_file, dest_file)
            size_bytes = os.path.getsize(dest_file)
            total_text_copied += size_bytes
            copied += 1
        else:
            print(f"[MISSING] {src_file}")
            missing += 1

    print("\n" + "="*60)
    print("HASIL REKONSTRUKSI KNOWLEDGE BASE (100% DATA UTUH):")
    print(f"- Total file terdistribusi: {copied} dari {len(FILE_MAPPING)} file")
    print(f"- Total data tersalin utuh: {total_text_copied / (1024*1024):.2f} MB")
    print(f"- File hilang / missing: {missing}")
    print("\nRincian per Kategori:")
    for cat_name, cat_folder in CATEGORIES.items():
        file_count = len(os.listdir(cat_folder))
        folder_size = sum(os.path.getsize(os.path.join(cat_folder, f)) for f in os.listdir(cat_folder)) / 1024
        print(f"  * {cat_name}: {file_count} file ({folder_size:.1f} KB)")
    print("="*60)

if __name__ == '__main__':
    execute()
