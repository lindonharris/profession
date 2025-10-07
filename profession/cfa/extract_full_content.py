#!/usr/bin/env python3
"""
CFA Full Content Extractor - Extracts actual text content from PDFs
"""

import pdfplumber
import re
import json
from pathlib import Path
from datetime import datetime
import hashlib

def extract_volume_full_content(pdf_path, output_dir, sample_only=False):
    """
    Extract full text content from a CFA volume

    Args:
        pdf_path: Path to PDF file
        output_dir: Output directory for extracted content
        sample_only: If True, only extract first 30 pages for testing
    """

    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"📖 Extracting full content from: {pdf_path.name}")
    print("=" * 60)

    volume_content = {
        'source_file': pdf_path.name,
        'extraction_date': datetime.now().isoformat(),
        'total_pages': 0,
        'modules': {},
        'full_text': [],
        'page_content': {}
    }

    current_module = None
    current_module_text = []

    with pdfplumber.open(pdf_path) as pdf:
        volume_content['total_pages'] = len(pdf.pages)

        # Determine page range
        page_limit = 30 if sample_only else len(pdf.pages)
        print(f"Processing {page_limit} of {len(pdf.pages)} pages...")

        for page_num in range(page_limit):
            page = pdf.pages[page_num]

            try:
                # Extract text
                text = page.extract_text()
                if not text:
                    continue

                # Clean headers/footers
                text = re.sub(r'© CFA Institute.*Not for distribution\.', '', text)
                text = re.sub(r'^\d+$', '', text, flags=re.MULTILINE)  # Remove page numbers

                # Store page content
                volume_content['page_content'][page_num + 1] = {
                    'text': text,
                    'word_count': len(text.split()),
                    'char_count': len(text)
                }

                # Check for module markers
                module_match = re.search(
                    r'L\s*E\s*A\s*R\s*N\s*I\s*N\s*G\s+M\s*O\s*D\s*U\s*L\s*E\s*\n\s*(\d+)\s*\n([^\n]+)',
                    text, re.MULTILINE
                )

                if module_match:
                    # Save previous module
                    if current_module and current_module_text:
                        module_full_text = '\n\n'.join(current_module_text)
                        volume_content['modules'][current_module] = {
                            'title': current_module,
                            'text': module_full_text,
                            'word_count': len(module_full_text.split()),
                            'content_hash': hashlib.md5(module_full_text.encode()).hexdigest()[:8]
                        }

                    # Start new module
                    module_num = module_match.group(1)
                    module_title = module_match.group(2).strip()
                    current_module = f"Module {module_num}: {module_title}"
                    current_module_text = [text]
                    print(f"  Found {current_module} at page {page_num + 1}")

                elif current_module:
                    # Add to current module
                    current_module_text.append(text)
                else:
                    # No module yet, add to general content
                    volume_content['full_text'].append(text)

                # Progress indicator
                if (page_num + 1) % 10 == 0:
                    print(f"  Processed {page_num + 1} pages...")

            except Exception as e:
                print(f"  ⚠️ Error on page {page_num + 1}: {str(e)[:50]}")
                continue

        # Save last module
        if current_module and current_module_text:
            module_full_text = '\n\n'.join(current_module_text)
            volume_content['modules'][current_module] = {
                'title': current_module,
                'text': module_full_text,
                'word_count': len(module_full_text.split()),
                'content_hash': hashlib.md5(module_full_text.encode()).hexdigest()[:8]
            }

    # Save extracted content
    save_extracted_content(volume_content, output_dir, sample_only)

    return volume_content


def save_extracted_content(content, output_dir, sample_only=False):
    """Save extracted content in multiple formats"""

    output_dir = Path(output_dir)

    # 1. Save metadata JSON (lightweight)
    metadata = {
        'source_file': content['source_file'],
        'extraction_date': content['extraction_date'],
        'total_pages': content['total_pages'],
        'modules': list(content['modules'].keys()),
        'module_stats': {
            name: {
                'word_count': info['word_count'],
                'content_hash': info['content_hash']
            }
            for name, info in content['modules'].items()
        },
        'total_words': sum(page['word_count'] for page in content['page_content'].values())
    }

    metadata_path = output_dir / 'metadata.json'
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)
    print(f"\n✓ Saved metadata: {metadata_path}")

    # 2. Save full content JSON (complete extraction)
    if not sample_only:
        full_json_path = output_dir / 'full_content.json'
        with open(full_json_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved full content: {full_json_path}")

    # 3. Save each module as separate markdown
    for module_name, module_info in content['modules'].items():
        # Create safe filename
        safe_name = re.sub(r'[^\w\s-]', '', module_name).strip().replace(' ', '_')
        md_path = output_dir / f'{safe_name}.md'

        # Create markdown with module content
        md_content = f"# {module_name}\n\n"
        md_content += f"*Extracted from: {content['source_file']}*\n\n"
        md_content += f"**Word count**: {module_info['word_count']:,}\n\n"
        md_content += "---\n\n"

        # Add first 5000 chars as preview if full text is long
        if module_info['word_count'] > 1000:
            md_content += "## Content Preview (First 5000 characters)\n\n"
            md_content += module_info['text'][:5000]
            md_content += "\n\n*[Content truncated for preview - see full_content.json for complete text]*\n"
        else:
            md_content += module_info['text']

        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"✓ Saved module: {md_path.name} ({module_info['word_count']:,} words)")

    # 4. Create overview markdown
    overview_md = f"# Content Extraction Summary\n\n"
    overview_md += f"**Source**: {content['source_file']}\n"
    overview_md += f"**Pages extracted**: {len(content['page_content'])}\n"
    overview_md += f"**Total pages**: {content['total_pages']}\n"
    overview_md += f"**Extraction date**: {content['extraction_date'][:10]}\n\n"

    overview_md += "## Modules Extracted\n\n"
    for module_name, module_info in content['modules'].items():
        overview_md += f"### {module_name}\n"
        overview_md += f"- Words: {module_info['word_count']:,}\n"
        overview_md += f"- Content hash: {module_info['content_hash']}\n\n"

    overview_md += "## Statistics\n\n"
    total_words = sum(page['word_count'] for page in content['page_content'].values())
    overview_md += f"- Total words extracted: {total_words:,}\n"
    overview_md += f"- Average words per page: {total_words // len(content['page_content']) if content['page_content'] else 0:,}\n"
    overview_md += f"- Modules found: {len(content['modules'])}\n"

    overview_path = output_dir / 'EXTRACTION_OVERVIEW.md'
    with open(overview_path, 'w', encoding='utf-8') as f:
        f.write(overview_md)
    print(f"✓ Saved overview: {overview_path}")

    print(f"\n📊 Extraction Summary:")
    print(f"   Total words: {total_words:,}")
    print(f"   Modules: {len(content['modules'])}")
    print(f"   Output: {output_dir}")


def main():
    """Extract Volume 2 with full content"""

    base_dir = Path('/mnt/c/Users/lindo/Documents/Obsidian/profession/cfa')
    pdf_path = base_dir / '2025-level-ii-curriculum' / 'cfa-program2025L2V2.pdf'
    output_dir = base_dir / 'processed' / 'volume_2_full'

    print("\n" + "="*60)
    print("CFA VOLUME 2: FULL CONTENT EXTRACTION")
    print("="*60)

    # Extract sample first (30 pages)
    print("\n1. Extracting sample (first 30 pages)...")
    content = extract_volume_full_content(pdf_path, output_dir, sample_only=True)

    print("\n" + "="*60)
    print("Sample extraction complete!")
    print(f"Extracted {len(content['page_content'])} pages")
    print(f"Found {len(content['modules'])} modules")

    # Ask to continue
    response = input("\nExtract full volume (all 172 pages)? (y/n): ")
    if response.lower() == 'y':
        print("\n2. Extracting full volume...")
        extract_volume_full_content(pdf_path, output_dir, sample_only=False)

    print("\n✅ Done! Check processed/volume_2_full/ for extracted content")


if __name__ == "__main__":
    main()