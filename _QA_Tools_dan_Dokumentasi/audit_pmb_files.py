import os

pmb_dir = "Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru"
files = [f for f in os.listdir(pmb_dir) if f.endswith(".md")]

results = []
for f in files:
    p = os.path.join(pmb_dir, f)
    with open(p, "r", encoding="utf-8", errors="ignore") as fp:
        lines = fp.readlines()
    
    total_lines = len(lines)
    non_empty = [l.strip() for l in lines if l.strip()]
    total_non_empty = len(non_empty)
    
    # Check vertical shredded: lines with 1 or 2 words (ignoring markdown bullet points or headers)
    short_lines = [l for l in non_empty if len(l.split()) <= 2 and not l.startswith("#") and not l.startswith("-") and not l.startswith("---")]
    shredded_ratio = len(short_lines) / total_non_empty if total_non_empty > 0 else 0
    
    results.append({
        "name": f,
        "lines": total_lines,
        "non_empty": total_non_empty,
        "shredded_ratio": shredded_ratio,
        "bytes": os.path.getsize(p)
    })

print("=== ALL 45 FILES IN 01_PMB AUDIT ===")
results.sort(key=lambda x: x["lines"], reverse=True)
for r in results:
    status = "SHREDDED/BERANTAKAN" if r["shredded_ratio"] > 0.35 and r["lines"] > 100 else "NORMAL"
    print(f"[{status}] {r['name']}: {r['lines']} lines, {r['bytes']} bytes (shredded: {r['shredded_ratio']*100:.1f}%)")
