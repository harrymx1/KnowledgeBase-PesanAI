import os

mekari_docs = [
    # Image 1 (Page 1)
    {"name": "FAQ_Registrasi_Online_Maba_Lulus_Seleksi", "ver": "v1", "status": "ACTIVE", "chunks": 6},
    {"name": "Pedoman Seleksi Mandiri Kemitraan UM", "ver": "v1", "status": "ACTIVE", "chunks": 7},
    {"name": "Pedoman Seleksi Mandiri Jalur Tes Masuk Berbasis Komputer (TMBK)", "ver": "v1", "status": "ACTIVE", "chunks": 9},
    {"name": "Pedoman Seleksi Mandiri Jalur Skor UTBK UM 2026", "ver": "v1", "status": "ACTIVE", "chunks": 8},
    {"name": "Pedoman Seleksi Mandiri Jalur Prestasi UM 2026", "ver": "v1", "status": "ACTIVE", "chunks": 8},
    {"name": "Pedoman Seleksi Mandiri Jalur Leadership UM 2026", "ver": "v1", "status": "ACTIVE", "chunks": 14},
    {"name": "Panduan Registrasi Mahasiswa Baru Jalur Masuk SNBP", "ver": "v1", "status": "ACTIVE", "chunks": 13},
    {"name": "Panduan Registrasi 1 Atap SNBP 2026", "ver": "v1", "status": "ACTIVE", "chunks": 5},
    {"name": "Knowledge Source New Revisi 1", "ver": "v1", "status": "ACTIVE", "chunks": 196},
    {"name": "Knowledge Base Registrasi SNBP UM", "ver": "v1", "status": "ACTIVE", "chunks": 10},
    {"name": "Knowledge Base Registrasi Mahasiswa Baru Universitas Negeri Malang", "ver": "v1", "status": "ACTIVE", "chunks": 10},
    {"name": "KNOWLEDGE_BASE_ALL_PENERIMAAN_MABA (TRIASE)", "ver": "v1", "status": "ACTIVE", "chunks": 18},
    {"name": "KB_Status_Aksi_Template_6Juli2026", "ver": "v1", "status": "ACTIVE", "chunks": 27},
    {"name": "KB_SNBT_UM (1)", "ver": "v1", "status": "ACTIVE", "chunks": 54},
    {"name": "KB_SNBP_UM", "ver": "v1", "status": "ACTIVE", "chunks": 25},
    {"name": "KB_SM_RPL_Magister_UM (1)", "ver": "v1", "status": "ACTIVE", "chunks": 27},
    {"name": "KB_SM_PJJ_Magister_UM", "ver": "v1", "status": "ACTIVE", "chunks": 72},
    {"name": "KB_SM_Magister_Reguler_UM (1)", "ver": "v1", "status": "ACTIVE", "chunks": 42},
    {"name": "KB_SM_Kelas_Internasional_UM", "ver": "v1", "status": "ACTIVE", "chunks": 32},
    {"name": "KB_SM_Jalur_TMBK_UM", "ver": "v1", "status": "ACTIVE", "chunks": 29},
    # Image 2 (Page 2)
    {"name": "KB_SM_Jalur_Skor_UTBK_UM  Revisi gel. 4", "ver": "v1", "status": "ACTIVE", "chunks": 58},
    {"name": "KB_SM_Jalur_Prestasi_UM_1", "ver": "v1", "status": "ACTIVE", "chunks": 49},
    {"name": "KB_SM_Jalur_Leadership_UM", "ver": "v1", "status": "ACTIVE", "chunks": 38},
    {"name": "KB_SM_Jalur_Kemitraan_Mitra_Asuh_UM", "ver": "v1", "status": "ACTIVE", "chunks": 43},
    {"name": "KB_SM_Jalur_Bapres_PPMI_UM", "ver": "v1", "status": "ACTIVE", "chunks": 23},
    {"name": "KB_SM_Double_Degree_UM", "ver": "v1", "status": "ACTIVE", "chunks": 26},
    {"name": "KB_ProgramStudi_Fakultas_DayaTampung", "ver": "v1", "status": "ACTIVE", "chunks": 15},
    {"name": "KB_Jalur_Pendaftaran_SM_2026 (revisi)", "ver": "v1", "status": "ACTIVE", "chunks": 145},
    {"name": "KB SM Doktor Reguler UM", "ver": "v1", "status": "ACTIVE", "chunks": 40},
    {"name": "KB SM Doktor by Research UM", "ver": "v1", "status": "ACTIVE", "chunks": 46},
    {"name": "Informasi dan Panduan Seleksi Magister dan Doktor tahun 2026", "ver": "v1", "status": "ACTIVE", "chunks": 16},
    {"name": "Informasi dan Panduan RPL Sarjana dan Magister Universitas Negeri Malang tahun 2026", "ver": "v1", "status": "ACTIVE", "chunks": 20},
    {"name": "Pengumuman Pasca Kegiatan Pendaftaran Maba", "ver": "v1", "status": "ARCHIVED", "chunks": 12},
    {"name": "FAQ_Pendaftaran_Mandiri_dan_Kendala_Form", "ver": "v1", "status": "ACTIVE", "chunks": 11},
    {"name": "DAYA TAMPUNG PROGRAM STUDI & JADWAL SELEKSI MABA UM 2026", "ver": "v1", "status": "ARCHIVED", "chunks": 110},
]

local_pmb_dir = "Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru"
local_files = [f[:-3] for f in os.listdir(local_pmb_dir) if f.endswith(".md")]

print(f"Total di Mekari: {len(mekari_docs)} (Active: {sum(1 for d in mekari_docs if d['status']=='ACTIVE')}, Archived: {sum(1 for d in mekari_docs if d['status']=='ARCHIVED')})")
print(f"Total di Local Clean: {len(local_files)}")

# 1. Dokumen yang ada di Mekari tapi namanya persis sama di Local Clean
mekari_names = [d["name"] for d in mekari_docs]
exact_matches = [f for f in local_files if f in mekari_names]
print(f"\n1. Match Persis ({len(exact_matches)}):")
for f in sorted(exact_matches):
    print(f"   [OK] {f}")

# 2. Dokumen yang ada di Local Clean tapi BELUM ADA di Mekari
not_in_mekari = [f for f in local_files if f not in mekari_names]
print(f"\n2. Ada di Local Clean tapi BELUM ADA di Mekari ({len(not_in_mekari)}):")
for f in sorted(not_in_mekari):
    print(f"   [UPLOAD BARU] {f}")

# 3. Dokumen yang ada di Mekari tapi TIDAK ADA di Local Clean
not_in_local = [d for d in mekari_docs if d["name"] not in local_files]
print(f"\n3. Ada di Mekari tapi TIDAK ADA di Local Clean ({len(not_in_local)}):")
for d in not_in_local:
    print(f"   [{d['status']}] {d['name']} ({d['chunks']} chunk)")
