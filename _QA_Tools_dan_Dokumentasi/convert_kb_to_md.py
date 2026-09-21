import os
import sys
import shutil
import re
from pypdf import PdfReader

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SOURCE_DIR = '.'
TARGET_DIR = os.path.join(SOURCE_DIR, 'Knowledge_Base_MD')

# Files to keep as PDF
EXCLUDE_PDFS = [
    'transfer_knowledge (1).pdf',
    'transfer_knowledge (2)_compressed.pdf',
    'skb_libur_nasional_dan_cuti_bersama_tahun_2026.pdf'
]

def clean_and_format_markdown(text, original_filename, relative_folder):
    """
    Format extracted raw PDF text into clean, structured Markdown.
    """
    lines = text.split('\n')
    cleaned_lines = []
    
    # Clean doc title from filename
    doc_title = os.path.splitext(os.path.basename(original_filename))[0]
    doc_title = doc_title.replace('+', ' ').replace('_', ' ')
    
    # Add metadata header
    cleaned_lines.append(f"# {doc_title}")
    cleaned_lines.append(f"> **Sumber Dokumen:** `{os.path.basename(original_filename)}`  ")
    cleaned_lines.append(f"> **Kategori:** `{relative_folder if relative_folder else 'Umum / Root'}`\n")
    cleaned_lines.append("---\n")
    
    in_code_or_block = False
    
    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            cleaned_lines.append("")
            continue
            
        # Replace non-standard bullets
        line = re.sub(r'^[\uf0b7\u2022\u25cf\u25aa\u25b6\u25ba\u27a4●\*\-]\s*', '- ', line)
        
        # Detect Headings
        # All caps line with length > 4 and < 80 that doesn't start with bullet or punctuation
        if line.isupper() and 4 < len(line) < 80 and not line.startswith(('-', '*', '#', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
            cleaned_lines.append(f"\n## {line.title()}\n")
            continue
            
        # Detect Sections like "BAB I", "BAGIAN I", "A. ", "B. ", "1. PENGANTAR"
        if re.match(r'^(BAB\s+[IVXLCDM]+|BAGIAN\s+[IVXLCDM]+)', line, re.IGNORECASE):
            cleaned_lines.append(f"\n## {line}\n")
            continue
        
        # Detect Q&A Patterns
        if re.match(r'^(Pertanyaan|Tanya|Q)\s*[:\.]\s*', line, re.IGNORECASE):
            cleaned_lines.append(f"\n### {line}\n")
            continue
            
        if re.match(r'^(Jawaban|Jawab|A)\s*[:\.]\s*', line, re.IGNORECASE):
            cleaned_lines.append(f"\n**{line}**\n")
            continue
            
        # Detect Checklist / Good vs Bad response markers
        if line.startswith('❌') or line.startswith('✅'):
            cleaned_lines.append(f"> {line}")
            continue
            
        # Format official URLs as links
        # line = re.sub(r'(https?://[^\s]+)', r'[\1](\1)', line)
        
        cleaned_lines.append(line)
        
    md_content = '\n'.join(cleaned_lines)
    
    # Clean excessive blank lines (more than 2 consecutive newlines)
    md_content = re.sub(r'\n{3,}', '\n\n', md_content)
    return md_content.strip() + '\n'

def main():
    print(f"Mempersiapkan folder tujuan: {TARGET_DIR}")
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    stats = {
        'converted_to_md': 0,
        'kept_as_pdf': 0,
        'errors': 0
    }
    
    # Walk through directory
    for root, dirs, files in os.walk(SOURCE_DIR):
        # Exclude the target directory from walking
        if 'Knowledge_Base_MD' in root or '.git' in root or '.gemini' in root:
            continue
            
        rel_folder = os.path.relpath(root, SOURCE_DIR)
        if rel_folder == '.':
            target_subfolder = TARGET_DIR
            rel_folder_name = ""
        else:
            target_subfolder = os.path.join(TARGET_DIR, rel_folder)
            rel_folder_name = rel_folder
            os.makedirs(target_subfolder, exist_ok=True)
            
        for f in files:
            if not f.lower().endswith('.pdf'):
                continue
                
            source_file_path = os.path.join(root, f)
            fname_clean = f.replace('+', ' ')
            base_name, _ = os.path.splitext(fname_clean)
            
            # Check if this file should be kept as PDF
            is_excluded = any(ex in f.lower() for ex in EXCLUDE_PDFS)
            
            if is_excluded:
                # Copy as PDF
                dest_file_path = os.path.join(target_subfolder, fname_clean)
                print(f"[COPY AS PDF] {f} -> {dest_file_path}")
                shutil.copy2(source_file_path, dest_file_path)
                stats['kept_as_pdf'] += 1
            else:
                # Convert to MD
                dest_md_path = os.path.join(target_subfolder, base_name + '.md')
                try:
                    reader = PdfReader(source_file_path)
                    all_text = []
                    for idx, page in enumerate(reader.pages):
                        text = page.extract_text() or ''
                        if text.strip():
                            all_text.append(text)
                    
                    full_raw_text = '\n\n'.join(all_text)
                    formatted_md = clean_and_format_markdown(full_raw_text, f, rel_folder_name)
                    
                    with open(dest_md_path, 'w', encoding='utf-8') as out_f:
                        out_f.write(formatted_md)
                        
                    stats['converted_to_md'] += 1
                    print(f"[CONVERTED TO MD] {f} -> {os.path.basename(dest_md_path)} ({len(reader.pages)} hal)")
                except Exception as e:
                    print(f"[ERROR] Gagal konversi {f}: {e}")
                    stats['errors'] += 1

    print("\n" + "="*50)
    print("HASIL PROSES REPLIKASI & KONVERSI KNOWLEDGE BASE:")
    print(f"- Total file dikonversi menjadi Markdown (.md): {stats['converted_to_md']}")
    print(f"- Total file dipertahankan sebagai PDF (.pdf): {stats['kept_as_pdf']}")
    print(f"- Total error: {stats['errors']}")
    print(f"Folder tujuan tersimpan di: {os.path.abspath(TARGET_DIR)}")
    print("="*50)

if __name__ == '__main__':
    main()
