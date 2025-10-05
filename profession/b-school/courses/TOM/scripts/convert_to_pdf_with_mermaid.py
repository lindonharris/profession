#!/usr/bin/env python3
"""
Convert Markdown files with Mermaid diagrams to PDF
Requires: pip install markdown2 pdfkit
Note: Also requires wkhtmltopdf installed on system
"""

import markdown2
import pdfkit
import re
import os

def convert_mermaid_to_html(markdown_content):
    """Convert Markdown with Mermaid blocks to HTML with proper rendering"""
    
    # HTML template with Mermaid CDN
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <script>
            mermaid.initialize({{ startOnLoad: true, theme: 'default' }});
        </script>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
            h2 { color: #34495e; margin-top: 30px; }
            h3 { color: #7f8c8d; }
            code { 
                background: #f4f4f4; 
                padding: 2px 6px; 
                border-radius: 3px;
                font-family: 'Courier New', monospace;
            }
            pre { 
                background: #f4f4f4; 
                padding: 15px; 
                border-radius: 5px; 
                overflow-x: auto;
            }
            blockquote { 
                border-left: 4px solid #3498db; 
                padding-left: 15px; 
                color: #666;
                margin: 15px 0;
            }
            ul, ol { margin: 15px 0; padding-left: 30px; }
            li { margin: 5px 0; }
            strong { color: #2c3e50; }
            table {
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }
            th {
                background-color: #3498db;
                color: white;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            .mermaid {
                margin: 20px 0;
                text-align: center;
            }
        </style>
    </head>
    <body>
        {content}
    </body>
    </html>
    """
    
    # Convert Mermaid code blocks to div elements
    def replace_mermaid(match):
        mermaid_code = match.group(1)
        return f'<div class="mermaid">\n{mermaid_code}\n</div>'
    
    # Replace ```mermaid blocks
    markdown_content = re.sub(
        r'```mermaid\n(.*?)\n```',
        replace_mermaid,
        markdown_content,
        flags=re.DOTALL
    )
    
    # Convert Markdown to HTML
    html_content = markdown2.markdown(
        markdown_content,
        extras=['tables', 'fenced-code-blocks', 'header-ids']
    )
    
    # Insert into template (replace placeholder)
    final_html = html_template.replace('{content}', html_content)
    
    return final_html

def convert_to_pdf(markdown_file, output_pdf=None):
    """Convert a Markdown file to PDF"""
    
    if not os.path.exists(markdown_file):
        print(f"Error: File {markdown_file} not found")
        return False
    
    # Read Markdown content
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Set output filename if not provided
    if output_pdf is None:
        output_pdf = markdown_file.replace('.md', '.pdf')
    
    # Convert to HTML with Mermaid support
    html_content = convert_mermaid_to_html(markdown_content)
    
    # Save temporary HTML file
    temp_html = markdown_file.replace('.md', '_temp.html')
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # PDF options for better rendering
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': None,
        'javascript-delay': 2000,  # Wait for Mermaid to render
        'no-stop-slow-scripts': None
    }
    
    try:
        # Convert HTML to PDF
        pdfkit.from_file(temp_html, output_pdf, options=options)
        print(f"✅ Successfully converted: {output_pdf}")
        
        # Clean up temporary HTML file
        os.remove(temp_html)
        return True
        
    except Exception as e:
        print(f"❌ Error converting to PDF: {e}")
        # Clean up temporary HTML file
        if os.path.exists(temp_html):
            os.remove(temp_html)
        return False

if __name__ == "__main__":
    # Convert the two documents
    base_path = "/mnt/c/Users/lindo/Documents/Obsidian/profession/b-school/courses/TOM/case notes"
    
    files_to_convert = [
        "Donner Process Flow.md",
        "Donner Process Flow - Three Versions.md"
    ]
    
    for file in files_to_convert:
        file_path = os.path.join(base_path, file)
        print(f"\nConverting: {file}")
        convert_to_pdf(file_path)