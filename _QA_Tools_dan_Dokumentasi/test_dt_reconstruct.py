import re

with open("Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru/KB_ProgramStudi_Fakultas_DayaTampung.md", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Let's find all rows with prodi numbers and digits
# Pattern for a prodi entry:
# e.g.: "1 S1 Bimbingan dan Konseling 215 60 59 70 71 85 85 10,9%"
# Let's inspect how the text looks when unwrapped
lines = text.splitlines()
unwrapped_lines = []
curr = []
for l in lines:
    s = l.strip()
    if not s:
        continue
    if s.startswith("## Fakultas") or s.startswith("Grand Total") or re.match(r"^\d+\s+(?:S1|D4)\b", s):
        if curr:
            unwrapped_lines.append(" ".join(curr))
            curr = []
        curr.append(s)
    elif curr:
        curr.append(s)
    else:
        unwrapped_lines.append(s)

if curr:
    unwrapped_lines.append(" ".join(curr))

for l in unwrapped_lines:
    if "S1 " in l or "D4 " in l or "Fakultas" in l:
        print(l[:100])
