import re

def preview_file(filename, n_chars=400):
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
    "SELEKSI MANDIRI JALUR TES MASUK BERBASIS KOMPUTER.md",
    "KB_SM_Jalur_TMBK_UM.md",
    "Pedoman Seleksi Mandiri Jalur Tes Masuk Berbasis Komputer (TMBK).md",
    "SELEKSI MANDIRI KELAS INTERNASIONAL.md",
    "KB_SM_Kelas_Internasional_UM.md"
]:
    preview_file(f)
