import os

pmb_dir = "Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru"
for f in [
    "info s.d 24 Agustus 2026 - Pengumuman Registrasi Administrasi Calon Mahasiswa Baru Universitas Negeri Malang (UM) Jalur SNBP Tahun Akademik 2026-2027.md",
    "kb_kemitraan_institusi.md",
    "kb_kemitraan_outbound_mobility.md",
    "1. Pengumuman Pasca Kegiatan Pendaftaran Maba.md"
]:
    p = os.path.join(pmb_dir, f)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8", errors="ignore") as fp:
            content = fp.read()
        print(f"=== {f} ({len(content.splitlines())} lines) ===")
        print(content[:350])
        print("\n" + "="*50)
