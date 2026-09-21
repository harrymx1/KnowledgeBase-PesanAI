import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_MD_DIR = os.path.join(BASE_DIR, 'Knowledge_Base_MD')
CLEAN_DIR = os.path.join(BASE_DIR, 'Knowledge_Base_Clean_Categorized')

# List all original files from Knowledge_Base_MD
all_src_files = []
for r, d, files in os.walk(SRC_MD_DIR):
    for f in files:
        rel = os.path.relpath(os.path.join(r, f), SRC_MD_DIR)
        size = os.path.getsize(os.path.join(r, f))
        all_src_files.append((rel, size))

# List all clean files in Knowledge_Base_Clean_Categorized
all_clean_files = []
for r, d, files in os.walk(CLEAN_DIR):
    for f in files:
        rel = os.path.relpath(os.path.join(r, f), CLEAN_DIR)
        size = os.path.getsize(os.path.join(r, f))
        all_clean_files.append((rel, size))

print(f"Total file di Knowledge_Base_MD: {len(all_src_files)}")
print(f"Total file di Knowledge_Base_Clean_Categorized: {len(all_clean_files)}")

total_src_size = sum(s for f, s in all_src_files if f.endswith('.md'))
total_clean_size = sum(s for f, s in all_clean_files if f.endswith('.md'))
print(f"Total ukuran teks MD asli: {total_src_size / 1024:.1f} KB")
print(f"Total ukuran teks MD Clean: {total_clean_size / 1024:.1f} KB")

ratio = (total_clean_size / total_src_size) * 100 if total_src_size else 0
print(f"Rasio kelengkapan volume teks: {ratio:.1f}%")
