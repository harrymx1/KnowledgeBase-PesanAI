import re

with open("Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru/KB_ProgramStudi_Fakultas_DayaTampung.md", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

lines = text.splitlines()
print(f"Total lines: {len(lines)}")
for i, l in enumerate(lines[:40]):
    print(f"{i+1}: {l}")
