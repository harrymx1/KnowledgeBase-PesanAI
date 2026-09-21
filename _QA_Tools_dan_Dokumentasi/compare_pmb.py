import os

mekari_files = [
    "FAQ_Registrasi_Online_Maba_Lulus_Seleksi",
    "Pedoman Seleksi Mandiri Kemitraan UM",
    "Pedoman Seleksi Mandiri Jalur Tes Masuk Berbasis Komputer (TMBK)",
    "Pedoman Seleksi Mandiri Jalur Skor UTBK UM 2026",
    "Pedoman Seleksi Mandiri Jalur Prestasi UM 2026",
    "Pedoman Seleksi Mandiri Jalur Leadership UM 2026",
    "Panduan Registrasi Mahasiswa Baru Jalur Masuk SNBP",
    "Panduan Registrasi 1 Atap SNBP 2026",
    "Knowledge Source New Revisi 1",
    "Knowledge Base Registrasi SNBP UM",
    "Knowledge Base Registrasi Mahasiswa Baru Universitas Negeri Malang",
    "KNOWLEDGE_BASE_ALL_PENERIMAAN_MABA (TRIASE)",
    "KB_Status_Aksi_Template_6Juli2026",
    "KB_SNBT_UM (1)",
    "KB_SNBP_UM",
    "KB_SM_RPL_Magister_UM (1)",
    "KB_SM_PJJ_Magister_UM",
    "KB_SM_Magister_Reguler_UM (1)",
    "KB_SM_Kelas_Internasional_UM",
    "KB_SM_Jalur_TMBK_UM",
    "KB_SM_Jalur_Skor_UTBK_UM  Revisi gel. 4",
    "KB_SM_Jalur_Prestasi_UM_1",
    "KB_SM_Jalur_Leadership_UM",
    "KB_SM_Jalur_Kemitraan_Mitra_Asuh_UM",
    "KB_SM_Jalur_Bapres_PPMI_UM",
    "KB_SM_Double_Degree_UM",
    "KB_ProgramStudi_Fakultas_DayaTampung",
    "KB_Jalur_Pendaftaran_SM_2026 (revisi)",
    "KB SM Doktor Reguler UM",
    "KB SM Doktor by Research UM",
    "Informasi dan Panduan Seleksi Magister dan Doktor tahun 2026",
    "Informasi dan Panduan RPL Sarjana dan Magister Universitas Negeri Malang tahun 2026",
    "Pengumuman Pasca Kegiatan Pendaftaran Maba",
    "FAQ_Pendaftaran_Mandiri_dan_Kendala_Form",
    "DAYA TAMPUNG PROGRAM STUDI & JADWAL SELEKSI MABA UM 2026"
]

local_pmb_dir = "Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru"
local_files = [f[:-3] if f.endswith(".md") else f for f in os.listdir(local_pmb_dir)]

print(f"Total di Mekari: {len(mekari_files)}")
print(f"Total di Local Clean Categorized PMB: {len(local_files)}")

# Exact matches
exact_in_both = [m for m in mekari_files if m in local_files]
print(f"\nCocok (Ada di Mekari & Ada di Local PMB) ({len(exact_in_both)}):")
for f in sorted(exact_in_both):
    print(f"  + {f}")

# In Mekari but not in local_files
not_in_local = [m for m in mekari_files if m not in local_files]
print(f"\nDi Mekari TAPI TIDAK ADA di Local Clean PMB ({len(not_in_local)}):")
for f in not_in_local:
    print(f"  - {f}")

# In local_files but not in Mekari
not_in_mekari = [l for l in local_files if l not in mekari_files]
print(f"\nDi Local Clean PMB TAPI BELUM ADA di Mekari ({len(not_in_mekari)}):")
for f in sorted(not_in_mekari):
    print(f"  * {f}")
