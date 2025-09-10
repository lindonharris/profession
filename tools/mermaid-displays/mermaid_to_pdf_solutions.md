	# Mermaid to PDF Solutions

## Option 1: Use Obsidian's Built-in Export (BEST)
**Steps:**
1. Open the .md file in Obsidian
2. Click the three dots menu (⋮) or right-click the tab
3. Select "Export to PDF"
4. Obsidian will render Mermaid diagrams properly

**Pros:** Works immediately, renders perfectly
**Cons:** Manual process for each file

## Option 2: Mermaid CLI Tool (Automated)
```bash
# Install Mermaid CLI globally
npm install -g @mermaid-js/mermaid-cli

# Extract and convert Mermaid diagrams
mmdc -i input.mmd -o output.svg -t dark
mmdc -i input.mmd -o output.png -s 2  # Scale 2x
mmdc -i input.mmd -o output.pdf
```

## Option 3: Use Playwright (Python Script)
```python
import asyncio
from playwright.async_api import async_playwright
import os

async def convert_with_playwright(md_file, pdf_file):
    """Convert Markdown with Mermaid to PDF using real browser"""
    
    # Read markdown
    with open(md_file, 'r') as f:
        content = f.read()
    
    # HTML with proper Mermaid setup
    html = f"""<!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css/github-markdown.min.css">
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <style>
            body {{ padding: 20px; max-width: 900px; margin: 0 auto; }}
            .markdown-body {{ box-sizing: border-box; min-width: 200px; max-width: 980px; }}
        </style>
    </head>
    <body class="markdown-body">
        <div id="content"></div>
        <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
        <script>
            document.getElementById('content').innerHTML = marked.parse(`{content.replace('`', '\\`')}`);
            mermaid.initialize({{ startOnLoad: true }});
            mermaid.init();
        </script>
    </body>
    </html>"""
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(html)
        await page.wait_for_load_state('networkidle')
        await page.wait_for_timeout(2000)  # Extra time for Mermaid
        await page.pdf(path=pdf_file, format='A4')
        await browser.close()

# Usage
asyncio.run(convert_with_playwright('input.md', 'output.pdf'))
```

## Option 4: Pre-render to Images First
```bash
# Step 1: Extract Mermaid blocks to separate files
grep -Pzo '(?s)```mermaid.*?```' "Donner Process Flow - Three Versions.md" | \
  awk 'BEGIN{n=0} /```mermaid/{n++; next} /```/{next} {print > "diagram_"n".mmd"}'

# Step 2: Convert each to PNG/SVG
for file in diagram_*.mmd; do
  mmdc -i "$file" -o "${file%.mmd}.png" -s 2
done

# Step 3: Replace in markdown and convert
# (Script would replace mermaid blocks with image references)
```

## Option 5: VS Code with Markdown Preview Enhanced
1. Install VS Code
2. Install "Markdown Preview Enhanced" extension
3. Open .md file
4. Right-click preview → "Chrome (Puppeteer) → PDF"

## Quick Test Script
Save as `test_mermaid.html` and open in browser, then print to PDF:

```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({ startOnLoad: true });</script>
</head>
<body>
    <h1>Test Mermaid Rendering</h1>
    <div class="mermaid">
    graph TD
        A[Start] --> B{Decision}
        B -->|Yes| C[Do this]
        B -->|No| D[Do that]
    </div>
</body>
</html>
```

## Recommended Approach

For your immediate needs:
1. **Use Obsidian's Export** for quick, perfect results
2. **Install Mermaid CLI** for automation:
   ```bash
   npm install -g @mermaid-js/mermaid-cli
   ```

The Obsidian export is the most reliable since it already renders your Mermaid diagrams correctly in the app.