import re

def preview_file(filename, n_chars=1000):
    filepath = f"Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru/{filename}"
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # Simple line unwrap
    lines = content.splitlines()
    header = []
    body_words = []
    for l in lines:
        s = l.strip()
        if not s:
            continue
        if s.startswith("#") or s.startswith(">") or s.startswith("---"):
            if not body_words:
                header.append(s)
            else:
                body_words.append(f"\n\n{s}\n")
        else:
            body_words.append(s)
    
    unwrapped = " ".join(body_words)
    unwrapped = re.sub(r"\s+", " ", unwrapped)
    print(f"=== PREVIEW: {filename} ===")
    print("\n".join(header[:4]))
    print("BODY PREVIEW:")
    print(unwrapped[:n_chars])
    print("\n" + "="*50)

for f in [
    "SELEKSI MANDIRI JALUR PRESTASI.md",
    "KB_SM_Jalur_Prestasi_UM_1.md",
    "Pedoman Seleksi Mandiri Jalur Prestasi UM 2026.md",
    "SELEKSI MANDIRI JALUR SKOR UTBK V4.md",
    "KB_SM_Jalur_Skor_UTBK_UM  Revisi gel. 4.md",
    "Pedoman Seleksi Mandiri Jalur Skor UTBK UM 2026.md"
]:
    preview_file(f, 400)
