import os

pmb_dir = "Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru"
files = [f for f in os.listdir(pmb_dir) if f.endswith(".md")]

files_with_mojibake = []
for f in files:
    p = os.path.join(pmb_dir, f)
    with open(p, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    cnt = c.count("\ufffd")
    if cnt > 0:
        files_with_mojibake.append((f, cnt))

print(f"Files with real mojibake (\\ufffd): {len(files_with_mojibake)}")
for f, cnt in files_with_mojibake:
    print(f"  - {f}: {cnt} occurrences")
