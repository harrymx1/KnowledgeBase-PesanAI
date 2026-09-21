import os
import sys
import re
import shutil

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_MD_DIR = os.path.join(BASE_DIR, 'Knowledge_Base_MD')
OUT_DIR = os.path.join(BASE_DIR, 'Knowledge_Base_Clean_Categorized')

# Definition of the 5 Clean Master Categories
CATEGORIES = {
    '01_PMB_Penerimaan_Mahasiswa_Baru': os.path.join(OUT_DIR, '01_PMB_Penerimaan_Mahasiswa_Baru'),
    '02_Keuangan_dan_Biaya_Pendidikan': os.path.join(OUT_DIR, '02_Keuangan_dan_Biaya_Pendidikan'),
    '03_Akademik_dan_SIAKAD': os.path.join(OUT_DIR, '03_Akademik_dan_SIAKAD'),
    '04_Layanan_Kampus_dan_Sarpras': os.path.join(OUT_DIR, '04_Layanan_Kampus_dan_Sarpras'),
    '05_Helpdesk_dan_Eskalasi': os.path.join(OUT_DIR, '05_Helpdesk_dan_Eskalasi')
}

def clean_text(text):
    text = re.sub(r'[\uf0b7\u2022\u25cf\u25aa\u25b6\u25ba\u27a4●\*\-]\s*', '- ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def write_article(category_key, filename, title, summary, content, links=None, helpdesk_note=True):
    folder = CATEGORIES[category_key]
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    
    md = []
    md.append(f"# {title}\n")
    md.append(f"> **Kategori:** `{category_key.replace('_', ' ')}`  ")
    md.append(f"> **Target Pembaca:** Calon Mahasiswa Baru / Mahasiswa Aktif / Sivitas Akademika UM\n")
    md.append("---\n")
    
    if summary:
        md.append("## Ringkasan Singkat\n")
        md.append(f"{summary.strip()}\n")
        
    md.append(content.strip())
    md.append("\n")
    
    # Official links and contact section
    md.append("## Tautan Resmi & Kontak Terkait\n")
    if links:
        for label, url in links.items():
            md.append(f"- **{label}:** {url}")
    else:
        md.append("- **Portal Resmi UM:** https://um.ac.id")
        md.append("- **Portal Seleksi PMB:** https://seleksi.um.ac.id")
        md.append("- **Portal Akademik SIAKAD:** https://siakad.um.ac.id")
        
    if helpdesk_note:
        md.append("- **Layanan Bantuan Resmi:** Helpdesk 1 Nomor UM (WhatsApp Terpusat: 0813-3344-400)")
        
    md_text = '\n'.join(md) + '\n'
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_text)
    print(f"[CREATED] {category_key} / {filename}")

def build():
    print("Mempersiapkan folder Knowledge_Base_Clean_Categorized...")
    if os.path.exists(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    for cat_path in CATEGORIES.values():
        os.makedirs(cat_path, exist_ok=True)

    # =========================================================================
    # KATEGORI 01: PMB (Penerimaan Mahasiswa Baru)
    # =========================================================================
    
    # 1. Jalur Nasional (SNBP & SNBT)
    snbp_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'KB_SNBP_UM.md')
    snbt_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'KB_SNBT_UM.md')
    snbp_txt = open(snbp_src, encoding='utf-8').read() if os.path.exists(snbp_src) else ""
    snbt_txt = open(snbt_src, encoding='utf-8').read() if os.path.exists(snbt_src) else ""
    
    write_article(
        '01_PMB_Penerimaan_Mahasiswa_Baru',
        '01_Jalur_Nasional_SNBP_dan_SNBT.md',
        'Jalur Nasional Penerimaan Mahasiswa Baru: SNBP & SNBT',
        'Informasi lengkap seleksi penerimaan mahasiswa baru nasional di Universitas Negeri Malang (UM) melalui jalur prestasi raport (SNBP) dan tes berbasis komputer nasional (SNBT).',
        f"## 1. Seleksi Nasional Berdasarkan Prestasi (SNBP)\n{clean_text(snbp_txt[:4000])}\n\n## 2. Seleksi Nasional Berdasarkan Tes (SNBT)\n{clean_text(snbt_txt[:4500])}",
        {'Portal SNPMB Kemdikbud': 'https://snpmb.bppp.kemdikbud.go.id', 'Informasi Registrasi SNBP/SNBT UM': 'https://seleksi.um.ac.id'}
    )

    # 2. Seleksi Mandiri Jalur Prestasi
    prestasi_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'Pedoman Seleksi Mandiri Jalur Prestasi UM 2026.md')
    prestasi_txt = open(prestasi_src, encoding='utf-8').read() if os.path.exists(prestasi_src) else ""
    write_article(
        '01_PMB_Penerimaan_Mahasiswa_Baru',
        '02_Seleksi_Mandiri_Jalur_Prestasi.md',
        'Seleksi Mandiri Jalur Prestasi Universitas Negeri Malang',
        'Panduan pendaftaran, kriteria prestasi akademik/non-akademik, olahraga, seni, dan keagamaan untuk jenjang Sarjana (S1) dan Sarjana Terapan (D4).',
        clean_text(prestasi_txt[:5000]),
        {'Pendaftaran Seleksi Mandiri UM': 'https://seleksi.um.ac.id'}
    )

    # 3. Seleksi Mandiri Skor UTBK (FINAL GELOMBANG 4 - Single Source of Truth)
    utbk_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'KB_SM_Jalur_Skor_UTBK_UM  Revisi gel. 4.md')
    if not os.path.exists(utbk_src):
        utbk_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'Pedoman Seleksi Mandiri Jalur Skor UTBK UM 2026.md')
    utbk_txt = open(utbk_src, encoding='utf-8').read() if os.path.exists(utbk_src) else ""
    write_article(
        '01_PMB_Penerimaan_Mahasiswa_Baru',
        '03_Seleksi_Mandiri_Jalur_Skor_UTBK.md',
        'Seleksi Mandiri Jalur Skor UTBK UM (Gelombang 1 - 4 Mutakhir)',
        'Pedoman seleksi mandiri menggunakan nilai sertifikat UTBK-SNBT tanpa perlu mengikuti tes tulis ulang. Dokumen ini merupakan acuan mutakhir gelombang pendaftaran.',
        clean_text(utbk_txt[:6000]),
        {'Portal Seleksi Skor UTBK': 'https://seleksi.um.ac.id'}
    )

    # 4. Seleksi Mandiri TMBK
    tmbk_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'Pedoman Seleksi Mandiri Jalur Tes Masuk Berbasis Komputer (TMBK).md')
    tmbk_txt = open(tmbk_src, encoding='utf-8').read() if os.path.exists(tmbk_src) else ""
    write_article(
        '01_PMB_Penerimaan_Mahasiswa_Baru',
        '04_Seleksi_Mandiri_Jalur_TMBK.md',
        'Seleksi Mandiri Jalur Tes Masuk Berbasis Komputer (TMBK) UM',
        'Panduan seleksi ujian mandiri berbasis komputer yang diselenggarakan langsung di laboratorium komputer kampus UM maupun lokasi mitra.',
        clean_text(tmbk_txt[:5000]),
        {'Jadwal dan Panduan TMBK': 'https://seleksi.um.ac.id'}
    )

    # 5. Seleksi Mandiri Leadership & Kemitraan
    leader_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'Pedoman Seleksi Mandiri Jalur Leadership UM 2026.md')
    mitra_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'Pedoman Seleksi Mandiri Kemitraan UM.md')
    leader_txt = open(leader_src, encoding='utf-8').read() if os.path.exists(leader_src) else ""
    mitra_txt = open(mitra_src, encoding='utf-8').read() if os.path.exists(mitra_src) else ""
    write_article(
        '01_PMB_Penerimaan_Mahasiswa_Baru',
        '05_Seleksi_Mandiri_Leadership_dan_Kemitraan.md',
        'Seleksi Mandiri Jalur Kepemimpinan (Leadership) dan Kemitraan',
        'Ketentuan khusus bagi ketua OSIS / pengurus organisasi siswa, serta jalur kemitraan kerja sama instansi pemerintah, yayasan, atau perusahaan mitra asuh UM.',
        f"## 1. Jalur Leadership (Ketua OSIS / Organisasi)\n{clean_text(leader_txt[:4000])}\n\n## 2. Jalur Kemitraan Institusi\n{clean_text(mitra_txt[:4000])}",
        {'Informasi Seleksi Khusus': 'https://seleksi.um.ac.id'}
    )

    # 6. Kelas Internasional & Double Degree
    inter_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'KB_SM_Kelas_Internasional_UM.md')
    inter_txt = open(inter_src, encoding='utf-8').read() if os.path.exists(inter_src) else ""
    write_article(
        '01_PMB_Penerimaan_Mahasiswa_Baru',
        '06_Seleksi_Mandiri_Kelas_Internasional.md',
        'Seleksi Mandiri Program Sarjana Kelas Internasional UM',
        'Persyaratan kompetensi bahasa Inggris, kurikulum berstandar internasional, serta peluang pertukaran pelajar dan double degree di universitas mitra luar negeri.',
        clean_text(inter_txt[:5000]),
        {'Portal Kelas Internasional UM': 'https://seleksi.um.ac.id'}
    )

    # 7. Pascasarjana (Magister S2 & Doktor S3)
    s2_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'Informasi dan Panduan Seleksi Magister dan Doktor tahun 2026.md')
    s2_txt = open(s2_src, encoding='utf-8').read() if os.path.exists(s2_src) else ""
    write_article(
        '01_PMB_Penerimaan_Mahasiswa_Baru',
        '07_Seleksi_Program_Magister_S2_dan_Doktor_S3.md',
        'Panduan Seleksi Masuk Program Magister (S2) dan Doktor (S3)',
        'Informasi lengkap seleksi pascasarjana UM: Magister Reguler, Magister PJJ (Pembelajaran Jarak Jauh), Doktor Reguler, dan Doktor By Research.',
        clean_text(s2_txt[:6000]),
        {'Portal Pascasarjana UM': 'https://seleksi.um.ac.id'}
    )

    # 8. Fast-Track (Akselerasi Internal - Triase)
    fast_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'KNOWLEDGE_BASE_ALL_PENERIMAAN_MABA (TRIASE).md')
    fast_txt = open(fast_src, encoding='utf-8').read() if os.path.exists(fast_src) else ""
    write_article(
        '01_PMB_Penerimaan_Mahasiswa_Baru',
        '08_Program_Akselerasi_Fast_Track_Internal.md',
        'Program Percepatan Studi Akselerasi (Fast-Track) Internal UM',
        'Program strategis percepatan studi S1 langsung lanjut S2 atau S2 langsung lanjut S3 bagi mahasiswa internal UM dengan capaian akademik unggul.',
        clean_text(fast_txt[:5000]),
        {'Akselerasi Internal UM': 'https://seleksi.um.ac.id/akselerasi-internal/'}
    )

    # 9. RPL (Rekognisi Pembelajaran Lampau)
    rpl_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'Informasi dan Panduan RPL Sarjana dan Magister Universitas Negeri Malang tahun 2026.md')
    rpl_txt = open(rpl_src, encoding='utf-8').read() if os.path.exists(rpl_src) else ""
    write_article(
        '01_PMB_Penerimaan_Mahasiswa_Baru',
        '09_Program_RPL_Sarjana_dan_Magister.md',
        'Panduan Jalur Rekognisi Pembelajaran Lampau (RPL) S1 & S2',
        'Jalur pengakuan atas capaian pembelajaran dari pendidikan nonformal, informal, dan/atau pengalaman kerja sebagai dasar melanjutkan pendidikan formal di UM.',
        clean_text(rpl_txt[:5500]),
        {'Portal RPL UM': 'https://seleksi.um.ac.id'}
    )

    # 10. Daya Tampung & Kuota Seleksi
    daya_src = os.path.join(SRC_MD_DIR, 'DAYA TAMPUNG PROGRAM STUDI & JADWAL SELEKSI MABA UM 2026.md')
    daya_txt = open(daya_src, encoding='utf-8').read() if os.path.exists(daya_src) else ""
    write_article(
        '01_PMB_Penerimaan_Mahasiswa_Baru',
        '10_Daya_Tampung_dan_Jadwal_Seleksi_Maba.md',
        'Daya Tampung Program Studi & Jadwal Seleksi Mahasiswa Baru UM',
        'Daftar alokasi kuota daya tampung penerimaan mahasiswa baru per program studi dan jadwal resmi pelaksanaan seleksi di lingkungan UM.',
        clean_text(daya_txt[:6000]),
        {'Daftar Prodi & Daya Tampung Resmi': 'https://seleksi.um.ac.id'}
    )

    # 11. Template Jawaban Status Jalur & Aksi (Acuan Sopan AI)
    status_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'KB_Status_Aksi_Template_6Juli2026.md')
    status_txt = open(status_src, encoding='utf-8').read() if os.path.exists(status_src) else ""
    write_article(
        '01_PMB_Penerimaan_Mahasiswa_Baru',
        '11_Template_Sopan_Status_Jalur_dan_Aksi.md',
        'Standar Template Sopan Jawaban Status Jalur Pendaftaran (Helpdesk AI)',
        'Pedoman baku pola kalimat AI saat menjawab pertanyaan calon mahasiswa mengenai status buka/tutup kegiatan pendaftaran, registrasi online, dan PKKMB.',
        clean_text(status_txt[:6000]),
        {'Portal Seleksi UM': 'https://seleksi.um.ac.id'}
    )

    # =========================================================================
    # KATEGORI 02: KEUANGAN DAN BIAYA PENDIDIKAN
    # =========================================================================

    # 1. Biaya Pendidikan UKT & IPI
    ukt_src = os.path.join(SRC_MD_DIR, 'Registrasi UKT dan KRS', 'KB_Biaya_UKT_IPI_Pembayaran.md')
    ukt_txt = open(ukt_src, encoding='utf-8').read() if os.path.exists(ukt_src) else ""
    write_article(
        '02_Keuangan_dan_Biaya_Pendidikan',
        '01_Ketentuan_Biaya_UKT_dan_IPI.md',
        'Ketentuan Biaya Pendidikan: UKT (Uang Kuliah Tunggal) & IPI',
        'Daftar kelompok UKT (1 s.d. 7), ketentuan sumbangan IPI untuk jalur mandiri, kebijakan pengembalian dana, serta ketentuan beasiswa keringanan internal kategori A/B/C.',
        clean_text(ukt_txt[:6500]),
        {'Informasi Biaya Pendidikan': 'https://support.um.ac.id/topic/epayment/'}
    )

    # 2. Tata Cara Pembayaran & Bank Mitra
    bayar_src = os.path.join(SRC_MD_DIR, 'Registrasi UKT dan KRS', 'Panduan Pembayaran UKT Mahasiswa UM - (diluar tanggal batas pembayaran) .md')
    bayar_txt = open(bayar_src, encoding='utf-8').read() if os.path.exists(bayar_src) else ""
    write_article(
        '02_Keuangan_dan_Biaya_Pendidikan',
        '02_Tata_Cara_Pembayaran_dan_Bank_Mitra.md',
        'Tata Cara Pembayaran Biaya Pendidikan Melalui Bank Mitra',
        'Prosedur pembayaran memakai Kode Bayar unik (bukan transfer rekening pribadi) di bank mitra UM: BNI, BRI, BTN, Bank Mandiri, Bank Jatim, CIMB Niaga, BTN Syariah, dan BSI.',
        f"{clean_text(bayar_txt)}\n\n### Ketentuan Masa Berlaku Kode Bayar:\n- Kode bayar berlaku selama 48 jam sejak diaktifkan.\n- Jika kedaluwarsa, mahasiswa dapat mengaktifkan ulang melalui sistem e-payment.",
        {'Panduan e-Payment UM': 'https://support.um.ac.id/topic/epayment/'}
    )

    # 3. Penurunan, Sanggah, dan Keringanan UKT
    penurunan_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'KB+Penurunan+dan+Penarikan+UKT.md')
    penurunan_txt = open(penurunan_src, encoding='utf-8').read() if os.path.exists(penurunan_src) else ""
    write_article(
        '02_Keuangan_dan_Biaya_Pendidikan',
        '03_Prosedur_Keringanan_dan_Penurunan_UKT.md',
        'Prosedur Pengajuan Keringanan, Penundaan, dan Penurunan UKT',
        'Alur dan syarat mahasiswa mengajukan peninjauan kembali besaran UKT karena perubahan kemampuan ekonomi keluarga, serta ketentuan penundaan pembayaran.',
        clean_text(penurunan_txt[:5000]),
        {'Layanan Keuangan UM': 'https://support.um.ac.id'}
    )

    # 4. Beasiswa KIP-Kuliah
    kip_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'KB_FAQ_Umum_KIP_Prosedur.md')
    kip_txt = open(kip_src, encoding='utf-8').read() if os.path.exists(kip_src) else ""
    write_article(
        '02_Keuangan_dan_Biaya_Pendidikan',
        '04_Panduan_Beasiswa_KIP_Kuliah.md',
        'Panduan Pendaftaran & Verifikasi Beasiswa KIP-Kuliah UM',
        'Mekanisme pendaftaran, syarat berkas, dan tahapan verifikasi faktual lapangan bagi calon mahasiswa baru penerima beasiswa KIP-Kuliah di UM.',
        clean_text(kip_txt[:5500]),
        {'Portal KIP Kuliah Kemdikbud': 'https://kip-kuliah.kemdikbud.go.id', 'Informasi KIP UM': 'https://seleksi.um.ac.id'}
    )

    # 5. Kendala Pembayaran
    kendala_src = os.path.join(SRC_MD_DIR, 'Registrasi UKT dan KRS', 'Panduan Permasalahan Pembayaran UKT.md')
    kendala_txt = open(kendala_src, encoding='utf-8').read() if os.path.exists(kendala_src) else ""
    write_article(
        '02_Keuangan_dan_Biaya_Pendidikan',
        '05_Solusi_Kendala_Pembayaran_UKT.md',
        'Penanganan Kendala Pembayaran UKT Belum Terverifikasi',
        'Langkah-langkah yang harus dilakukan mahasiswa jika sudah mendebet saldo bank namun status tagihan di sistem belum berubah menjadi lunas.',
        clean_text(kendala_txt[:4000]),
        {'Helpdesk Pembayaran e-Payment': 'https://support.um.ac.id'}
    )

    # =========================================================================
    # KATEGORI 03: AKADEMIK DAN SIAKAD
    # =========================================================================

    # 1. Aktivasi Akun Siakad
    siakad_act_src = os.path.join(SRC_MD_DIR, 'Panduan Siakad', '1) Panduan Aktifasi Akun Siakad UM untuk Mahasiswa Baru UM.md')
    siakad_act_txt = open(siakad_act_src, encoding='utf-8').read() if os.path.exists(siakad_act_src) else ""
    write_article(
        '03_Akademik_dan_SIAKAD',
        '01_Panduan_Aktivasi_Akun_SIAKAD_Maba.md',
        'Panduan Aktivasi Akun SIAKAD untuk Mahasiswa Baru',
        'Petunjuk langkah demi langkah mahasiswa baru mengaktifkan akun Sistem Informasi Akademik (SIAKAD) UM untuk pertama kali.',
        clean_text(siakad_act_txt[:4500]),
        {'Portal SIAKAD UM': 'https://siakad.um.ac.id'}
    )

    # 2. Kendala Login & Registrasi Akun
    siakad_reg_src = os.path.join(SRC_MD_DIR, 'Registrasi UKT dan KRS', 'KB_Registrasi_Akun_SIAKAD_DaftarUlang.md')
    siakad_reg_txt = open(siakad_reg_src, encoding='utf-8').read() if os.path.exists(siakad_reg_src) else ""
    write_article(
        '03_Akademik_dan_SIAKAD',
        '02_Kendala_Login_dan_Registrasi_Akun.md',
        'Solusi Kendala Login, Lupa Password, dan Registrasi Akun SIAKAD',
        'Penanganan masalah teknis akun mahasiswa: lupa password, email pemulihan tidak masuk, NIM tidak ditemukan, atau akun terkunci.',
        clean_text(siakad_reg_txt[:4500]),
        {'Reset Akun SIAKAD': 'https://siakad.um.ac.id'}
    )

    # 3. Pengisian KRS & Evaluasi PBM
    krs_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'KB+Evaluasi+PBM+-+Registrasi+-+KRS.md')
    krs_txt = open(krs_src, encoding='utf-8').read() if os.path.exists(krs_src) else ""
    write_article(
        '03_Akademik_dan_SIAKAD',
        '03_Pengisian_KRS_dan_Evaluasi_PBM.md',
        'Tata Cara Pengisian KRS & Evaluasi Proses Belajar Mengajar (PBM)',
        'Aturan pengisian Kartu Rencana Studi (KRS), batas minimal/maksimal SKS, konsekuensi terlambat mengisi kuisioner evaluasi PBM, serta kontak operator fakultas.',
        f"{clean_text(krs_txt[:5000])}\n\n### Kontak Bantuan Akademik Per Fakultas:\n- FIP: 0877-5974-4572\n- FS: 0895-6368-91070\n- FMIPA: 0895-4245-14500\n- FEB: 0821-8838-1688\n- FT: 0878-5953-5360\n- FIK: 0813-3171-1127\n- FIS: 0813-1635-0700",
        {'Portal SIAKAD Pengisian KRS': 'https://siakad.um.ac.id'}
    )

    # 4. Semester Antara (Pendek) & Pembatalan KRS
    antara_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'KNOWLEDGE BASE CHATBOT  Semester Antara atau pendek di Universitas Negeri Malang (UM)  Intent- penjelasan_semester_antara atau pendek.docx.md')
    antara_txt = open(antara_src, encoding='utf-8').read() if os.path.exists(antara_src) else ""
    write_article(
        '03_Akademik_dan_SIAKAD',
        '04_Semester_Antara_dan_Pembatalan_KRS.md',
        'Panduan Pelaksanaan Semester Antara (Pendek) & Pembatalan Mata Kuliah',
        'Ketentuan pengambilan semester antara untuk perbaikan nilai atau percepatan kelulusan, biaya per SKS, dan prosedur pembatalan mata kuliah.',
        clean_text(antara_txt[:4500]),
        {'Informasi Akademik SIAKAD': 'https://siakad.um.ac.id'}
    )

    # 5. Yudisium & Kelulusan
    yudisium_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'KB+Proses+Yudisium+-+versi+1.md')
    yudisium_txt = open(yudisium_src, encoding='utf-8').read() if os.path.exists(yudisium_src) else ""
    write_article(
        '03_Akademik_dan_SIAKAD',
        '05_Prosedur_Yudisium_dan_Kelulusan.md',
        'Prosedur Pendaftaran Yudisium & Penjajakan Kelulusan',
        'Persyaratan bebas tanggungan perpustakaan/laboratorium, verifikasi transkrip nilai, dan alur pendaftaran yudisium online.',
        clean_text(yudisium_src[:5000] if yudisium_txt else ""),
        {'Portal Yudisium UM': 'https://siakad.um.ac.id'}
    )

    # 6. Pengambilan Ijazah & Legalisir
    ijazah_src = os.path.join(SRC_MD_DIR, 'Informasi Penerimaan Maba', 'KB_Legalisir_Ijazah_UM.md')
    ijazah_txt = open(ijazah_src, encoding='utf-8').read() if os.path.exists(ijazah_src) else ""
    write_article(
        '03_Akademik_dan_SIAKAD',
        '06_Pengambilan_Ijazah_dan_Legalisir.md',
        'Prosedur Pengambilan Ijazah Asli, Surat Alumni, dan Legalisir',
        'Syarat pengambilan ijazah/transkrip fisik, permohonan legalisir offline dan online, serta verifikasi keaslian ijazah.',
        clean_text(ijazah_txt[:4500]),
        {'Portal Legalisir Online': 'https://support.um.ac.id'}
    )

    # =========================================================================
    # KATEGORI 04: LAYANAN KAMPUS DAN SARPRAS
    # =========================================================================

    # 1. Fasilitas & Sarana Prasarana
    sarpras_src = os.path.join(SRC_MD_DIR, 'Sarana Prasarana UM.md')
    sarpras_txt = open(sarpras_src, encoding='utf-8').read() if os.path.exists(sarpras_src) else ""
    write_article(
        '04_Layanan_Kampus_dan_Sarpras',
        '01_Fasilitas_dan_Sarana_Prasarana_UM.md',
        'Fasilitas Akademik, Perpustakaan, Lab, dan Sarana Prasarana UM',
        'Informasi fasilitas gedung perkuliahan, Perpustakaan Pusat, Laboratorium Terpadu (UIL), Poliklinik/UPT Kesehatan, asrama mahasiswa, dan sarana olahraga.',
        clean_text(sarpras_txt[:6000]),
        {'Portal Fasilitas UM': 'https://um.ac.id/fasilitas/'}
    )

    # 2. Smart Gate Parkir & Akses Masuk
    smartgate_content = """## Sistem Smart Gate Parkir Kampus UM
Universitas Negeri Malang (UM) memberlakukan sistem **Smart Gate Parkir** terotomatisasi di seluruh gerbang masuk kampus untuk menjaga keamanan dan ketertiban lalu lintas sivitas akademika.

### Ketentuan Akses Smart Gate:
1. **Mahasiswa Aktif:** Menggunakan Kartu Tanda Mahasiswa (KTM) yang telah diaktivasi chip RFID-nya.
2. **Dosen & Tenaga Kependidikan:** Menggunakan kartu pegawai resmi UM.
3. **Tamu / Pengunjung Umum:** Mengambil tiket karcis parkir di pintu dispenser masuk gerbang.

### Prosedur Aktivasi KTM untuk Smart Gate:
- Bagi mahasiswa baru, aktivasi akses gate parkir dilakukan secara otomatis setelah KTM fisik diterima atau melalui loket pelayanan keamanan kampus di Graha Rektorat lantai dasar.

### Pertanyaan yang Sering Diajukan (FAQ):
### Q: Kak, apakah masuk kampus UM bayar parkir?
**Jawaban:** Halo Kak, bagi mahasiswa aktif, dosen, dan staf UM yang menggunakan KTM/kartu pegawai resmi, akses masuk dan parkir kampus tidak dipungut biaya (gratis). Untuk pengunjung umum/tamu diberlakukan tarif retribusi parkir standar sesuai perda.
"""
    write_article(
        '04_Layanan_Kampus_dan_Sarpras',
        '02_Smart_Gate_Parkir_dan_Akses_Kampus.md',
        'Sistem Smart Gate Parkir dan Akses Masuk Kampus UM',
        'Ketentuan akses gerbang masuk otomatis menggunakan KTM, prosedur aktivasi kartu parkir, dan aturan parkir mahasiswa serta tamu umum.',
        smartgate_content,
        {'Website Resmi UM': 'https://um.ac.id'}
    )

    # 3. Prosedur Kehilangan Barang (KTM / Helm)
    kehilangan_content = """## Prosedur Penanganan Kehilangan Barang (KTM, Helm, Dompet)
Bagi sivitas akademika yang mengalami kehilangan barang atau menemukan barang tertinggal di area kampus Universitas Negeri Malang, ikuti prosedur berikut:

### 1. Kehilangan Kartu Tanda Mahasiswa (KTM):
1. Buat Surat Keterangan Tanda Lapor Kehilangan (SKTLK) dari kantor kepolisian (Polsek) setempat.
2. Bawa SKTLK dan fotokopi KTP/KRS ke Subdirektorat Layanan Pendidikan (Gedung Graha Rektorat Lantai 2).
3. Lakukan pengajuan cetak ulang KTM pengganti melalui portal SIAKAD.

### 2. Kehilangan Helm atau Kendaraan Bermotor:
1. Segera laporkan ke Pos Satuan Pengamanan (Satpam) gerbang terdekat atau Markas Komando Keamanan UM.
2. Petugas keamanan akan mengecek rekaman CCTV di titik parkir terkait.
3. Tunjukkan STNK dan bukti identitas kepemilikan yang sah.

### Pertanyaan yang Sering Diajukan (FAQ):
### Q: Kak, helm saya hilang di parkiran perpustakaan, lapor ke mana ya?
**Jawaban:** Halo Kak, mohon segera menuju ke Pos Satpam terdekat atau Pos Keamanan Pusat di Graha Rektorat untuk membuat laporan kehilangan. Petugas keamanan akan membantu pengecekan rekaman CCTV di area parkir tersebut.
"""
    write_article(
        '04_Layanan_Kampus_dan_Sarpras',
        '03_Prosedur_Kehilangan_KTM_dan_Barang.md',
        'Prosedur Pelaporan Kehilangan Barang (KTM, Helm, & Fasilitas)',
        'Panduan langkah lapor kehilangan barang di lingkungan kampus UM, prosedur cek rekaman CCTV parkiran, dan alur pembuatan KTM pengganti.',
        kehilangan_content,
        {'Layanan Keamanan Kampus': 'https://um.ac.id'}
    )

    # 4. Kampus Inklusif & Layanan Disabilitas
    inklusif_content = """## Layanan Kampus Inklusif dan Ramah Disabilitas
Universitas Negeri Malang (UM) berkomitmen penuh mewujudkan lingkungan pendidikan tinggi yang ramah, aksesibel, dan inklusif bagi penyandang disabilitas.

### Fasilitas Ramah Disabilitas di UM:
- Jalur pemandu (tactile paving) untuk tuna netra di seluruh koridor pedestrian utama.
- Akses ramp kursi roda dan lift di setiap gedung perkuliahan bertingkat.
- Toilet khusus ramah disabilitas di setiap gedung fakultas.
- Pendampingan khusus saat proses perkuliahan dan seleksi ujian masuk kampus.

### Layanan Bantuan Khusus:
Mahasiswa dengan kebutuhan khusus dapat menghubungi Pusat Layanan Disabilitas UM untuk mendapatkan fasilitas pendampingan perkuliahan dan ujian.
"""
    write_article(
        '04_Layanan_Kampus_dan_Sarpras',
        '04_Kampus_Inklusif_dan_Layanan_Disabilitas.md',
        'Fasilitas Kampus Inklusif dan Layanan Ramah Disabilitas UM',
        'Informasi komitmen aksesibilitas sarana kampus UM, ramp kursi roda, jalur pemandu, serta layanan pendampingan studi bagi mahasiswa disabilitas.',
        inklusif_content,
        {'Pusat Inklusif UM': 'https://um.ac.id'}
    )

    # 5. Pengajuan Kerja Sama
    kerjasama_src = os.path.join(SRC_MD_DIR, 'KNOWLEDGE BASE PANDUAN PENGAJUAN KERJA SAMA DI UNIVERSITAS NEGERI MALANG (REV).md')
    kerjasama_txt = open(kerjasama_src, encoding='utf-8').read() if os.path.exists(kerjasama_src) else ""
    write_article(
        '04_Layanan_Kampus_dan_Sarpras',
        '05_Panduan_Pengajuan_Kerja_Sama.md',
        'Panduan Prosedur Pengajuan Kerja Sama di Universitas Negeri Malang',
        'Alur dan tata cara institusi pemerintah, swasta, industri, atau perguruan tinggi mitra mengajukan nota kesepahaman (MoU) dan perjanjian kerja sama (PKS) di UM.',
        clean_text(kerjasama_txt[:5000]),
        {'Direktorat Kerja Sama UM': 'https://um.ac.id'}
    )

    # =========================================================================
    # KATEGORI 05: HELPDESK DAN ESKALASI
    # =========================================================================

    # 1. Kebijakan Helpdesk 1 Nomor UM
    helpdesk_src = os.path.join(SRC_MD_DIR, 'Helpdesk 1 Nomor.md')
    helpdesk_txt = open(helpdesk_src, encoding='utf-8').read() if os.path.exists(helpdesk_src) else ""
    write_article(
        '05_Helpdesk_dan_Eskalasi',
        '01_Kebijakan_Helpdesk_1_Nomor_UM.md',
        'Kebijakan Sentralisasi Layanan: Helpdesk 1 Nomor UM',
        'Pedoman satu pintu layanan resmi UM. Seluruh pertanyaan, permohonan informasi, dan kendala administrasi mahasiswa dipusatkan melalui 1 nomor kontak WhatsApp Helpdesk resmi.',
        clean_text(helpdesk_txt[:4000]),
        {'Portal Layanan Terpadu UM': 'https://support.um.ac.id', 'WhatsApp Resmi Helpdesk 1 Nomor': '0813-3344-400'}
    )

    # 2. FAQ Umum Sivitas Akademika
    faq_src = os.path.join(SRC_MD_DIR, 'FAQ _ INFORMASI DAFTAR PERTANYAAN UMUM YANG SERING DISAMPAIKAN.md')
    faq_txt = open(faq_src, encoding='utf-8').read() if os.path.exists(faq_src) else ""
    write_article(
        '05_Helpdesk_dan_Eskalasi',
        '02_Daftar_Pertanyaan_Umum_FAQ_Sivitas.md',
        'Daftar Pertanyaan Umum (FAQ) Layanan Sivitas Akademika UM',
        'Kompilasi tanya jawab resmi yang paling sering diajukan masyarakat dan mahasiswa seputar layanan akademik, fasilitas, kalender studi, dan administrasi umum.',
        clean_text(faq_txt[:5000]),
        {'FAQ Portal Resmi UM': 'https://support.um.ac.id'}
    )

    # 3. Layanan Loket & Eskalasi Live Agent
    loket_src = os.path.join(SRC_MD_DIR, 'Registrasi UKT dan KRS', 'Registrasi - Layanan di Loket Administrasi Sub Direktorat Layanan Pendidikan.md')
    loket_txt = open(loket_src, encoding='utf-8').read() if os.path.exists(loket_src) else ""
    write_article(
        '05_Helpdesk_dan_Eskalasi',
        '03_Layanan_Loket_dan_Eskalasi_Live_Agent.md',
        'Prosedur Layanan Loket Administrasi & Eskalasi Live Agent',
        'Jam operasional loket layanan Graha Rektorat, etika pelayanan, serta mekanisme eskalasi tiket dari AI Chatbot ke petugas manusia (Live Agent) jika butuh verifikasi berkas.',
        clean_text(loket_txt[:4500]),
        {'Loket Layanan Subdit Pendidikan': 'Graha Rektorat Lantai 2 UM', 'Jam Layanan': 'Senin - Jumat 07.30 - 16.00 WIB'}
    )

    print("\n" + "="*50)
    print("HASIL PEMBANGUNAN KNOWLEDGE BASE CLEAN & CATEGORIZED:")
    total_articles = sum(len(os.listdir(p)) for p in CATEGORIES.values())
    print(f"- Total Artikel Modular Tercipta: {total_articles} file Markdown")
    for cat_name, cat_path in CATEGORIES.items():
        print(f"  * {cat_name}: {len(os.listdir(cat_path))} file")
    print(f"- Lokasi Output: {OUT_DIR}")
    print("="*50)

if __name__ == '__main__':
    build()
