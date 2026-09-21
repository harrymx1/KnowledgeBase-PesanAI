import re

def parse_and_print(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    lines = [l.strip() for l in content.splitlines() if l.strip()]
    words = []
    for l in lines:
        if l.startswith("#") or l.startswith(">") or l.startswith("---"):
            continue
        words.append(l)
    
    full_text = " ".join(words)
    full_text = re.sub(r"##\s*", "", full_text)
    full_text = re.sub(r"\s+", " ", full_text)
    print(f"\n{'='*30}\n{filepath}\n{'='*30}")
    print(full_text)

files = [
    "Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru/Registrasi Administrasi Calon Mahasiswa Baru Universitas Negeri Malang (UM) Calon Penerima Beasiswa KIP-K Jalur SNBT Tahun Akademik 2026_2027.md",
    "Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru/Pengumuman Registrasi Administrasi Calon Mahasiswa Baru Sarjana .md",
    "Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru/KB_ProgramStudi_Fakultas_DayaTampung.md"
]

for f in files:
    parse_and_print(f)
