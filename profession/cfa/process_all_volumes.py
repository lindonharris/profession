#!/usr/bin/env python3
"""
CFA Level II Complete Curriculum Processor
Extracts and organizes all volumes for AI agent training
"""

import pdfplumber
import re
import json
from pathlib import Path
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

class CFACurriculumProcessor:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.curriculum_dir = self.base_dir / '2025-level-ii-curriculum'
        self.output_dir = self.base_dir / 'processed'
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Volume mapping
        self.volumes = {
            1: {'name': 'Quantitative Methods', 'file': 'cfa-program2025L2V1.pdf', 'pages': 380},
            2: {'name': 'Economics', 'file': 'cfa-program2025L2V2.pdf', 'pages': 172},
            3: {'name': 'Financial Statement Analysis', 'file': 'cfa-program2025L2V3.pdf', 'pages': 420},
            4: {'name': 'Corporate Issuers', 'file': 'cfa-program2025L2V4.pdf', 'pages': 232},
            5: {'name': 'Equity Investments', 'file': 'cfa-program2025L2V5.pdf', 'pages': 476},
            6: {'name': 'Fixed Income', 'file': 'cfa-program2025L2V6.pdf', 'pages': 316},
            7: {'name': 'Derivatives', 'file': 'cfa-program2025L2V7.pdf', 'pages': 162},
            8: {'name': 'Alternative Investments', 'file': 'cfa-program2025L2V8.pdf', 'pages': 274},
            9: {'name': 'Portfolio Management', 'file': 'cfa-program2025L2V9.pdf', 'pages': 388},
            10: {'name': 'Ethics & Professional Standards', 'file': 'cfa-program2025L2V10.pdf', 'pages': 286}
        }

    def process_volume(self, volume_num):
        """Process a single volume"""
        vol_info = self.volumes[volume_num]
        pdf_path = self.curriculum_dir / vol_info['file']

        if not pdf_path.exists():
            logger.error(f"File not found: {pdf_path}")
            return None

        logger.info(f"Processing Volume {volume_num}: {vol_info['name']}")

        results = {
            'volume': volume_num,
            'name': vol_info['name'],
            'source_file': vol_info['file'],
            'expected_pages': vol_info['pages'],
            'actual_pages': 0,
            'learning_modules': [],
            'learning_outcomes': [],
            'key_concepts': [],
            'formulas': [],
            'tables_count': 0,
            'extraction_date': datetime.now().isoformat()
        }

        try:
            with pdfplumber.open(pdf_path) as pdf:
                results['actual_pages'] = len(pdf.pages)

                # Process in chunks
                chunk_size = 20
                current_module = None
                formulas_found = set()

                for start in range(0, min(100, len(pdf.pages)), chunk_size):  # First 100 pages
                    end = min(start + chunk_size, len(pdf.pages))

                    for page_num in range(start, end):
                        page = pdf.pages[page_num]

                        try:
                            text = page.extract_text()
                            if not text:
                                continue

                            # Clean text
                            text = re.sub(r'© CFA Institute.*Not for distribution\.', '', text)

                            # Find Learning Modules
                            module_match = re.search(
                                r'L\s*E\s*A\s*R\s*N\s*I\s*N\s*G\s+M\s*O\s*D\s*U\s*L\s*E\s*\n\s*(\d+)\s*\n([^\n]+)',
                                text, re.MULTILINE
                            )

                            if module_match:
                                module_num = module_match.group(1)
                                module_title = module_match.group(2).strip()

                                current_module = {
                                    'number': module_num,
                                    'title': module_title,
                                    'page': page_num + 1
                                }
                                results['learning_modules'].append(current_module)
                                logger.info(f"  Found Module {module_num}: {module_title}")

                            # Find Learning Outcomes
                            if 'LEARNING OUTCOMES' in text:
                                lo_section = text.split('LEARNING OUTCOMES')[1][:500]
                                outcomes = re.findall(r'[a-z]\.\s+([^;]+);?', lo_section)
                                for outcome in outcomes[:3]:  # First 3 outcomes
                                    results['learning_outcomes'].append({
                                        'module': current_module['number'] if current_module else 'Unknown',
                                        'outcome': outcome.strip()
                                    })

                            # Extract formulas
                            formula_patterns = [
                                r'[A-Z][a-zA-Z0-9]*\s*=\s*[^\n]{5,50}',
                                r'Δ[A-Z]+',
                                r'∂[A-Z]+/∂[A-Z]+',
                            ]

                            for pattern in formula_patterns:
                                matches = re.findall(pattern, text)
                                formulas_found.update(matches)

                            # Count tables
                            tables = page.extract_tables()
                            if tables:
                                results['tables_count'] += len(tables)

                        except Exception as e:
                            logger.warning(f"  Error on page {page_num + 1}: {str(e)[:50]}")

                    if end % 50 == 0:
                        logger.info(f"  Processed {end} pages...")

                # Store unique formulas (limit to 50)
                results['formulas'] = list(formulas_found)[:50]

                # Extract key concepts from module titles
                for module in results['learning_modules']:
                    concepts = re.split(r'[,;:]', module['title'])
                    for concept in concepts:
                        concept = concept.strip()
                        if len(concept) > 5:
                            results['key_concepts'].append(concept)

        except Exception as e:
            logger.error(f"Failed to process volume {volume_num}: {str(e)}")
            results['error'] = str(e)

        # Save results
        self.save_volume_results(volume_num, results)

        return results

    def save_volume_results(self, volume_num, results):
        """Save extraction results"""
        vol_dir = self.output_dir / f'volume_{volume_num}'
        vol_dir.mkdir(parents=True, exist_ok=True)

        # Save JSON
        json_path = vol_dir / f'volume_{volume_num}_data.json'
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        # Create markdown summary
        md = f"# Volume {volume_num}: {results['name']}\n\n"
        md += f"**Pages**: {results['actual_pages']} (expected: {results['expected_pages']})\n"
        md += f"**Extracted**: {results['extraction_date'][:10]}\n\n"

        md += f"## Learning Modules ({len(results['learning_modules'])})\n\n"
        for module in results['learning_modules']:
            md += f"- **Module {module['number']}**: {module['title']} (p.{module['page']})\n"

        if results['learning_outcomes']:
            md += f"\n## Sample Learning Outcomes\n\n"
            for lo in results['learning_outcomes'][:5]:
                md += f"- {lo['outcome']}\n"

        if results['formulas']:
            md += f"\n## Sample Formulas ({len(results['formulas'])} found)\n\n"
            for formula in results['formulas'][:10]:
                md += f"- `{formula}`\n"

        md += f"\n## Statistics\n\n"
        md += f"- Tables found: {results['tables_count']}\n"
        md += f"- Key concepts: {len(results['key_concepts'])}\n"

        md_path = vol_dir / f'volume_{volume_num}_summary.md'
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md)

        logger.info(f"  Saved to {vol_dir}")

    def process_all(self):
        """Process all volumes"""
        master_index = {
            'curriculum': 'CFA Level II 2025',
            'volumes': [],
            'total_pages': 0,
            'total_modules': 0,
            'extraction_date': datetime.now().isoformat()
        }

        for volume_num in sorted(self.volumes.keys()):
            logger.info(f"\n{'='*60}")
            results = self.process_volume(volume_num)

            if results:
                master_index['volumes'].append({
                    'number': volume_num,
                    'name': results['name'],
                    'pages': results['actual_pages'],
                    'modules': len(results['learning_modules']),
                    'formulas': len(results['formulas'])
                })
                master_index['total_pages'] += results['actual_pages']
                master_index['total_modules'] += len(results['learning_modules'])

        # Save master index
        index_path = self.output_dir / 'master_index.json'
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(master_index, f, indent=2)

        # Create master summary
        self.create_master_summary(master_index)

        logger.info(f"\n{'='*60}")
        logger.info(f"✅ EXTRACTION COMPLETE")
        logger.info(f"   Total pages: {master_index['total_pages']}")
        logger.info(f"   Total modules: {master_index['total_modules']}")
        logger.info(f"   Output: {self.output_dir}")

    def create_master_summary(self, index):
        """Create master summary markdown"""
        md = "# CFA Level II 2025 - Extraction Summary\n\n"
        md += f"**Total Pages**: {index['total_pages']}\n"
        md += f"**Total Learning Modules**: {index['total_modules']}\n"
        md += f"**Extraction Date**: {index['extraction_date'][:10]}\n\n"

        md += "## Volumes\n\n"
        md += "| Vol | Name | Pages | Modules | Formulas |\n"
        md += "|-----|------|-------|---------|----------|\n"

        for vol in index['volumes']:
            md += f"| {vol['number']} | {vol['name']} | {vol['pages']} | {vol['modules']} | {vol['formulas']} |\n"

        md += "\n## Usage\n\n"
        md += "Each volume directory contains:\n"
        md += "- `volume_N_data.json` - Structured extraction data\n"
        md += "- `volume_N_summary.md` - Human-readable summary\n\n"

        md += "Use the CFA analyst agent to query this content:\n"
        md += "```bash\n"
        md += "Task cfa-analyst \"Explain currency exchange rates from Volume 2\"\n"
        md += "```\n"

        md_path = self.output_dir / 'MASTER_SUMMARY.md'
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md)


def main():
    # Run from CFA directory
    processor = CFACurriculumProcessor('/mnt/c/Users/lindo/Documents/Obsidian/profession/cfa')

    print("\n" + "="*60)
    print("CFA LEVEL II - COMPLETE CURRICULUM PROCESSOR")
    print("="*60)
    print(f"Processing {len(processor.volumes)} volumes...")
    print("This will extract learning modules, outcomes, and formulas.")
    print("="*60)

    # Process Volume 2 first as test
    print("\n📖 Starting with Volume 2 (Economics) as test...")
    processor.process_volume(2)

    response = input("\n🤔 Continue with remaining volumes? (y/n): ")
    if response.lower() == 'y':
        for vol_num in [1, 3, 4, 5, 6, 7, 8, 9, 10]:
            processor.process_volume(vol_num)

        # Create master index
        processor.process_all()

    print("\n✅ Processing complete!")
    print(f"📁 Results saved to: processed/")


if __name__ == "__main__":
    main()