#!/usr/bin/env python3
"""
Extract Mermaid diagrams from Markdown and convert to images/PDF
"""

import re
import os
import subprocess
import tempfile
from pathlib import Path

def extract_mermaid_diagrams(markdown_file):
    """Extract all Mermaid code blocks from a Markdown file"""
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all Mermaid blocks
    pattern = r'```mermaid\n(.*?)\n```'
    diagrams = re.findall(pattern, content, re.DOTALL)
    
    return diagrams

def convert_mermaid_to_image(mermaid_code, output_file, format='png'):
    """Convert Mermaid code to image using mmdc CLI"""
    
    # Create temporary .mmd file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.mmd', delete=False) as tmp:
        tmp.write(mermaid_code)
        tmp_path = tmp.name
    
    try:
        # Run mermaid CLI
        cmd = ['mmdc', '-i', tmp_path, '-o', output_file, '-s', '2']
        if format == 'pdf':
            cmd.extend(['-f', 'pdf'])
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error converting diagram: {result.stderr}")
            return False
        
        return True
    finally:
        # Clean up temp file
        os.unlink(tmp_path)

def process_markdown_file(md_file):
    """Process a Markdown file and create a PDF with rendered Mermaid diagrams"""
    
    base_name = Path(md_file).stem
    base_dir = Path(md_file).parent
    
    print(f"\n📄 Processing: {md_file}")
    
    # Extract diagrams
    diagrams = extract_mermaid_diagrams(md_file)
    print(f"   Found {len(diagrams)} Mermaid diagram(s)")
    
    if not diagrams:
        print("   No Mermaid diagrams found!")
        return
    
    # Create output directory
    output_dir = base_dir / f"{base_name}_diagrams"
    output_dir.mkdir(exist_ok=True)
    
    # Convert each diagram
    image_files = []
    for i, diagram in enumerate(diagrams, 1):
        # Determine diagram type from first line
        first_line = diagram.strip().split('\n')[0] if diagram else ""
        
        if 'flowchart' in first_line:
            diagram_name = f"flowchart_{i}"
        elif 'graph' in first_line:
            if 'TD' in first_line:
                diagram_name = f"vertical_flow_{i}"
            elif 'LR' in first_line:
                diagram_name = f"horizontal_flow_{i}"
            else:
                diagram_name = f"graph_{i}"
        else:
            diagram_name = f"diagram_{i}"
        
        # Convert to PNG
        png_file = output_dir / f"{diagram_name}.png"
        print(f"   Converting diagram {i}: {diagram_name}")
        
        if convert_mermaid_to_image(diagram, str(png_file), 'png'):
            print(f"   ✅ Created: {png_file.name}")
            image_files.append(png_file)
        else:
            print(f"   ❌ Failed to convert diagram {i}")
    
    # Also create individual PDFs
    for i, diagram in enumerate(diagrams, 1):
        pdf_file = output_dir / f"diagram_{i}.pdf"
        if convert_mermaid_to_image(diagram, str(pdf_file), 'pdf'):
            print(f"   📊 Created PDF: {pdf_file.name}")
    
    # Create an HTML file that combines everything
    create_combined_html(md_file, image_files, output_dir)
    
    print(f"\n✨ All diagrams saved to: {output_dir}")
    
    return output_dir

def create_combined_html(md_file, image_files, output_dir):
    """Create an HTML file with all diagrams for easy viewing/printing"""
    
    base_name = Path(md_file).stem
    
    html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        .diagram-container {{
            background: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .diagram-title {{
            font-size: 18px;
            font-weight: bold;
            color: #34495e;
            margin-bottom: 15px;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border: 1px solid #ddd;
            border-radius: 4px;
        }}
        .print-break {{
            page-break-after: always;
        }}
        @media print {{
            body {{
                background: white;
            }}
            .diagram-container {{
                box-shadow: none;
                border: 1px solid #ddd;
            }}
        }}
    </style>
</head>
<body>
    <h1>{title} - Mermaid Diagrams</h1>
    {content}
    <div style="margin-top: 40px; padding: 20px; background: #e8f4f8; border-radius: 8px;">
        <p><strong>💡 Tip:</strong> Use Ctrl+P (or Cmd+P on Mac) to print this page to PDF with all diagrams.</p>
    </div>
</body>
</html>"""
    
    content = ""
    for i, img_file in enumerate(image_files, 1):
        img_name = img_file.name
        content += f"""
    <div class="diagram-container {'' if i == len(image_files) else 'print-break'}">
        <div class="diagram-title">Diagram {i}: {img_name.replace('.png', '').replace('_', ' ').title()}</div>
        <img src="{img_name}" alt="Diagram {i}">
    </div>"""
    
    html_file = output_dir / f"{base_name}_all_diagrams.html"
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html.format(title=base_name.replace('_', ' ').title(), content=content))
    
    print(f"   🌐 Created HTML viewer: {html_file.name}")

if __name__ == "__main__":
    # Process both files
    base_path = "/mnt/c/Users/lindo/Documents/Obsidian/profession/b-school/courses/TOM/case notes"
    
    files = [
        "Donner Process Flow - Three Versions.md"
    ]
    
    for file in files:
        file_path = os.path.join(base_path, file)
        if os.path.exists(file_path):
            output_dir = process_markdown_file(file_path)
            
            # Open the HTML file for viewing
            html_file = output_dir / f"{Path(file).stem}_all_diagrams.html"
            print(f"\n📂 To view all diagrams, open:")
            print(f"   {html_file}")
        else:
            print(f"❌ File not found: {file}")