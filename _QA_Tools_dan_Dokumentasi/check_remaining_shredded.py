import re

def preview_file(filename, n_chars=500):
    filepath = f"Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru/{filename}"
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    lines = content.splitlines()
    body_words = [l.strip() for l in lines if l.strip() and not l.startswith("#") and not l.startswith(">") and not l.startswith("---")]
    unwrapped = " ".join(body_words)
    unwrapped = re.sub(r"\s+", " ", unwrapped)
    print(f"=== PREVIEW: {filename} ===")
    print(unwrapped[:n_chars])
    print("\n" + "="*50)

for f in [
    "Registrasi Administrasi Calon Mahasiswa Baru Universitas Negeri Malang (UM) Jalur SNBT Tahun Akademik 2026_2027.md",
    "Registrasi Administrasi Calon Mahasiswa Baru Universitas Negeri Malang (UM) Calon Penerima Beasiswa KIP-K Jalur SNBT Tahun Akademik 2026_2027.md",
    "Pengumuman Registrasi Administrasi Calon Mahasiswa Baru Sarjana .md",
    "KB_ProgramStudi_Fakultas_DayaTampung.md"
]:
    preview_file(f)
