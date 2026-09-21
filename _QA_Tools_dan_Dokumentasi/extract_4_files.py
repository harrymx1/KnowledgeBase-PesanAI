import re

def extract_content(filename):
    filepath = f"Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru/{filename}"
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    lines = content.splitlines()
    cleaned_lines = []
    current_sentence = []
    for line in lines:
        s = line.strip()
        if not s:
            if current_sentence:
                cleaned_lines.append(" ".join(current_sentence))
                current_sentence = []
            continue
        if s.startswith("#") or s.startswith(">") or s.startswith("---"):
            if current_sentence:
                cleaned_lines.append(" ".join(current_sentence))
                current_sentence = []
            cleaned_lines.append(s)
        else:
            current_sentence.append(s)
    if current_sentence:
        cleaned_lines.append(" ".join(current_sentence))
    
    text = "\n".join(cleaned_lines)
    text = re.sub(r" +", " ", text)
    return text

with open("_QA_Tools_dan_Dokumentasi/extracted_snbt_reg.txt", "w", encoding="utf-8") as out:
    out.write("=== SNBT REGULER ===\n")
    out.write(extract_content("Registrasi Administrasi Calon Mahasiswa Baru Universitas Negeri Malang (UM) Jalur SNBT Tahun Akademik 2026_2027.md"))
    out.write("\n\n=== SNBT KIP-K ===\n")
    out.write(extract_content("Registrasi Administrasi Calon Mahasiswa Baru Universitas Negeri Malang (UM) Calon Penerima Beasiswa KIP-K Jalur SNBT Tahun Akademik 2026_2027.md"))
    out.write("\n\n=== SELEKSI MANDIRI SARJANA ===\n")
    out.write(extract_content("Pengumuman Registrasi Administrasi Calon Mahasiswa Baru Sarjana .md"))
    out.write("\n\n=== DAYA TAMPUNG ===\n")
    out.write(extract_content("KB_ProgramStudi_Fakultas_DayaTampung.md"))

print("Extracted content successfully written to extracted_snbt_reg.txt")
