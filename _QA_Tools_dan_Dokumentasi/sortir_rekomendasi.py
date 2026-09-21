import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Daftar file yang DIREKOMENDASIKAN UNTUK DIARSIPKAN / DIELIMINASI DARI UNGGAH MEKARI
ARCHIVE_CANDIDATES = [
    # 1. Dokumen kadaluwarsa / out of scope
    "Pengumuman+Penerimaan+Dosen+20+Februari+-++7+April+2026..pdf",
    "Peniadaan+Car+Free+Day.pdf",
    "SKB_Libur_Nasional_dan_Cuti_Bersama_Tahun_2026.pdf",
    
    # 2. Versi lama yang sudah tertimpa revisi terbaru
    "Informasi Penerimaan Maba/KB_SM_Jalur_Skor_UTBK_UM.pdf",
    "Informasi Penerimaan Maba/KB_SM_Jalur_Skor_UTBK_UM+(1).pdf",
    "Informasi Penerimaan Maba/SELEKSI+MANDIRI+JALUR+SKOR+UTBK.pdf",
    "Informasi Penerimaan Maba/KB_SM_RPL_Magister_UM.pdf",
    "Informasi Penerimaan Maba/KB+Akselerasi+Internal+UM.pdf",
    "Informasi Penerimaan Maba/kb_akselerasi_internal.pdf",
    "Informasi Penerimaan Maba/knowledge-source_19-01-2026.pdf",
    "Panduan Siakad/2) Panduan Aktifasi Akun Siakad UM untuk Mahasiswa Baru UM (1).pdf",
    "Registrasi UKT dan KRS/KB_Registrasi_Mahasiswa_Semester_Gasal_2026_2027_UM+(1).pdf"
]

print("=== REKOMENDASI SORTIR KNOWLEDGE BASE UNTUK MEKARI QONTAK ===")
print(f"Total file terdeteksi untuk diarsipkan/dieliminasi dari RAG: {len(ARCHIVE_CANDIDATES)}")
for f in ARCHIVE_CANDIDATES:
    exists = os.path.exists(f)
    print(f"[{'ADA' if exists else 'TIDAK DITEMUKAN'}] {f}")
