import re

def parse_numbered_items(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # Strip markdown headers at the top
    lines = [l.strip() for l in content.splitlines() if l.strip()]
    
    # Filter out header lines
    words = []
    for l in lines:
        if l.startswith("#") or l.startswith(">") or l.startswith("---"):
            continue
        words.append(l)
    
    full_text = " ".join(words)
    full_text = re.sub(r"##\s*", "", full_text)
    full_text = re.sub(r"\s+", " ", full_text)
    
    # Find numbered items: "1. ", "2. ", etc.
    parts = re.split(r"(\d+\.\s+[A-Z][^\.]+?(?:Tanggal:|Narasi:))", full_text)
    print(f"=== FULL TEXT FOR {filepath} ({len(full_text)} chars) ===")
    print(full_text)
    return full_text

parse_numbered_items("Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru/Registrasi Administrasi Calon Mahasiswa Baru Universitas Negeri Malang (UM) Jalur SNBT Tahun Akademik 2026_2027.md")
