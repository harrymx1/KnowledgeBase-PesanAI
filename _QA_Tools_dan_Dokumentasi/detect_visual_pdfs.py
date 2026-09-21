import os
import sys
from pypdf import PdfReader

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

root_dir = '.'
candidates_keep_pdf = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    if 'Knowledge_Base_MD' in dirpath:
        continue
    for f in filenames:
        if f.lower().endswith('.pdf'):
            full_path = os.path.join(dirpath, f)
            rel_path = os.path.relpath(full_path, root_dir)
            try:
                reader = PdfReader(full_path)
                num_pages = len(reader.pages)
                total_text_chars = sum(len(p.extract_text() or '') for p in reader.pages)
                avg_chars_per_page = total_text_chars / max(num_pages, 1)
                
                img_count = 0
                for p in reader.pages[:min(10, num_pages)]:
                    try:
                        img_count += len(p.images)
                    except:
                        pass
                
                is_explicit = 'transfer_knowledge' in f.lower()
                is_scanned = avg_chars_per_page < 80
                # If there are many images and very few text per image
                has_lots_of_diagrams = img_count > 5 and avg_chars_per_page < 300
                
                if is_explicit or is_scanned or has_lots_of_diagrams:
                    reason = []
                    if is_explicit:
                        reason.append("Diminta user (Transfer Knowledge)")
                    if is_scanned:
                        reason.append(f"Teks sangat sedikit/Scan ({avg_chars_per_page:.0f} chars/pg)")
                    if has_lots_of_diagrams:
                        reason.append(f"Banyak diagram/gambar ({img_count} imgs)")
                    
                    candidates_keep_pdf.append({
                        'file': rel_path,
                        'pages': num_pages,
                        'avg_chars': round(avg_chars_per_page, 1),
                        'images_sample': img_count,
                        'reason': ' & '.join(reason)
                    })
            except Exception as e:
                candidates_keep_pdf.append({
                    'file': rel_path,
                    'pages': -1,
                    'avg_chars': 0,
                    'images_sample': 0,
                    'reason': f'Error reading: {e}'
                })

print(f'Total candidates to keep as PDF: {len(candidates_keep_pdf)}')
for c in candidates_keep_pdf:
    print(f"- {c['file']} ({c['pages']} hal, avg {c['avg_chars']} chars/hal, {c['images_sample']} gambar) -> {c['reason']}")
