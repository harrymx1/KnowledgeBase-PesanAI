import json
import os
import sys

# Force utf-8 stdout
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('catalog_summary.json', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total files: {len(data)}")

print("\n=== 1. FILE BESAR / SPECIAL FILES ===")
for d in data:
    if d.get('size_kb', 0) > 1000 or 'transfer' in d['rel_path'].lower() or 'triase' in d['rel_path'].lower():
        print(f"- {d['rel_path']} | {d.get('pages')} pgs | {d.get('size_kb')} KB")
        print(f"    Intent: {d.get('has_intent')}, QA: {d.get('has_qa')}")
        print(f"    Snippet: {d.get('snippet')[:100]}...")

print("\n=== 2. KELOMPOK BERDASARKAN FOLDER ===")
folder_counts = {}
for d in data:
    top = os.path.dirname(d['rel_path']) or 'Root'
    folder_counts[top] = folder_counts.get(top, 0) + 1
for k, v in folder_counts.items():
    print(f"- {k}: {v} files")

print("\n=== 3. DETEKSI DUPLIKASI & VARIASI NAMA (REVISI/GELOMBANG) ===")
# Group by normalized filename
name_groups = {}
for d in data:
    fname = os.path.basename(d['rel_path']).lower()
    clean = fname.replace('+', ' ').replace('_', ' ').replace('.docx', '').replace('.pdf', '')
    # Simplify tokens
    tokens = [t for t in clean.split() if t not in ['kb', 'revisi', 'rev', '1', '2', '3', '4', 'v4', '(1)', '(2)', 'um', 'dan']]
    core_key = ' '.join(tokens[:3])
    name_groups.setdefault(core_key, []).append(d['rel_path'])

for k, v in name_groups.items():
    if len(v) > 1:
        print(f"[Group: {k}] ({len(v)} files):")
        for p in v:
            print(f"   -> {p}")
