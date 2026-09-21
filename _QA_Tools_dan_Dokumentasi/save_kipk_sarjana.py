import re

def inspect_file(filepath):
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
    return full_text

text_kipk = inspect_file("Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru/Registrasi Administrasi Calon Mahasiswa Baru Universitas Negeri Malang (UM) Calon Penerima Beasiswa KIP-K Jalur SNBT Tahun Akademik 2026_2027.md")
text_sarjana = inspect_file("Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru/Pengumuman Registrasi Administrasi Calon Mahasiswa Baru Sarjana .md")

with open("_QA_Tools_dan_Dokumentasi/kipk_and_sarjana.txt", "w", encoding="utf-8") as out:
    out.write("=== KIP-K SNBT ===\n" + text_kipk + "\n\n=== SARJANA MANDIRI ===\n" + text_sarjana)

print("Saved to kipk_and_sarjana.txt")
