# Case Digestion Procedure for AI Agent

## Overview
This procedure automates the workflow for extracting HBS cases from Canvas and creating structured case notes in Obsidian vault following the Case Digestion Guide template.

## Prerequisites
- Playwright environment activated: `source /tmp/playwright_env/bin/activate`
- Working directory: `~/.claude/direct-access-tools/canvas`
- Case Digestion Guide template at: `/mnt/c/Users/lindo/Documents/Obsidian/profession/b-school/courses/cases/templates/Case Study Template.md`

## Workflow Steps

### Step 0: Check if Case Already Exists (CRITICAL)
**Before starting any digestion**, search for existing case notes:

```bash
# Search by case name keywords
find /mnt/c/Users/lindo/Documents/Obsidian/profession/b-school/courses/ -name "*.md" -type f | xargs grep -l "Patrimonio Hoy"

# Or search in specific course folder
ls /mnt/c/Users/lindo/Documents/Obsidian/profession/b-school/courses/FIN1/case\ notes/
```

**If case exists**: Stop workflow, inform user case was already digested with date
**If case doesn't exist**: Proceed to Step 1

### Step 1: User Provides Case Information
**Input format**: `"[Case Name/Keywords]" for [COURSE_CODE]`

**Examples**:
- "Hospital for Special Surgery for TOM"
- "Hurtigruten for STRAT"
- "Tessei TOM"
- "Patrimonio Hoy FIN1"

### Step 2: Open Case in Browser & Save Assignment Context
**Script**: `python3 open-case-for-digestion.py "[Assignment Name]" [COURSE_CODE]`

**What it does**:
1. Queries Canvas API to find assignment by name in specified course
2. Extracts assignment context (questions, instructions, metadata)
3. Saves to `digestion/assignment_context.json`
4. Opens HBSP case URL in Playwright browser (non-headless)
5. Handles HBS authentication automatically
6. Keeps browser open for manual download

**Common Issues**:
- **TargetClosedError**: Script tries to fill login form but browser already closed - harmless, assignment_context.json was saved successfully
- **Assignment not found**: Try broader search terms (e.g., "Patrimonio" instead of "Patrimonio Hoy")
- **HBSP link found but Canvas opens anyway**: Script has fallback logic; if this happens, manually create script to open HBSP URL directly

**Workaround for script errors**: If `open-case-for-digestion.py` fails, create simple script in `/tmp/`:
```python
#!/usr/bin/env python3
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, downloads_path="/mnt/c/Users/lindo/Downloads")
        context = await browser.new_context(accept_downloads=True)
        page = await context.new_page()
        await page.goto("https://hbsp.harvard.edu/tu/XXXXXXXX", wait_until='domcontentloaded')
        # Login handling if needed
        print("Download PDF and close browser when done")
        try:
            await page.wait_for_event('close', timeout=0)
        except:
            pass
        await browser.close()

asyncio.run(main())
```

**Download location**:
- Playwright configured for: `/home/lindo/Downloads/` (Linux Downloads)
- PDFs download with UUID filenames (e.g., `3ac349d8-5c38-4bd5-b75b-b13fc9b7a7a1`)

### Step 3: User Downloads PDF
**User action**: Click download button in browser, close browser when done

**Agent assumption**: Once browser window is closed, assume PDF has been downloaded successfully

**Expected output**: PDF file in `/home/lindo/Downloads/`

### Step 4: Find Most Recent Download
**Command**: `ls -lt /home/lindo/Downloads/ | head -5`

**Note**: Downloads appear as UUID filenames without .pdf extension

**Alternative search patterns**:
```bash
# Find files modified in last 10 minutes
find /home/lindo/Downloads -type f -mmin -10

# Check file type of UUID download
file /home/lindo/Downloads/<UUID-filename>
```

### Step 5: VERIFY Case PDF (CRITICAL)
**IMPORTANT**: ALWAYS verify the PDF matches the expected case before proceeding

**Verification Process**:
1. Extract first 50 lines: `pdftotext /home/lindo/Downloads/<UUID> - | head -50`
2. Check case number and title match expected case from assignment_context.json
3. **If mismatch**: Search for correct PDF in recent downloads or ask user to re-download
4. **If match**: Proceed to Step 6

**Example verification**:
```bash
# Expected from assignment_context.json: "OOFOS Recovery Footwear"
# PDF shows: "OOFOS Recovery Footwear" ✅ MATCH - proceed
# PDF shows: "Ryanair: Dogfight" ❌ MISMATCH - find correct file
```

**Common causes of mismatch**:
- Multiple browser windows open simultaneously
- User downloaded different case than expected
- Old PDF still in downloads folder with recent timestamp

### Step 6: Read Case PDF
**Tool**: `Read` tool with path from VERIFIED Step 5

**Output**: Full PDF content extracted and available for analysis

### Step 6: Read Assignment Context
**File**: `digestion/assignment_context.json`

**Contains**:
- Assignment name, course, due date
- Discussion questions (HTML and plain text)
- Submission types
- Canvas URL

### Step 7: Read Case Note Template
**File**: `/mnt/c/Users/lindo/Documents/Obsidian/profession/b-school/courses/cases/templates/Case Study Template.md`

**Purpose**: Understand required structure and metadata fields

### Step 8: Create Structured Case Note
**Location**: `/mnt/c/Users/lindo/Documents/Obsidian/profession/b-school/courses/[COURSE]/case notes/[CASE_NUMBER] [CASE_TITLE].md`

**Required sections** (from template):
1. **YAML frontmatter** with metadata:
   - case_number, title, course, dates, professor
   - tags, industry, company, geographic_focus
   - key_topics, protagonists, decision_point, teaching_objectives

2. **Quick Facts** section

3. **Executive Summary** (2-3 sentences)

4. **Case Context**:
   - Company Background
   - Industry Landscape
   - Timeline of Events

5. **Key Protagonists** (name, role, background, key decisions)

6. **Central Problem/Decision**:
   - The Question
   - Constraints
   - Success Metrics

7. **Analysis** (SWOT or relevant framework)

8. **Financial Analysis** (if applicable)

9. **Key Exhibits** (list from PDF)

10. **Discussion Questions** (from assignment_context.json)

11. **My Analysis & Recommendations**:
    - Option 1-3 with Pros/Cons
    - Recommended Action
    - Implementation Plan

12. **Class Discussion Notes** (placeholder)

13. **Personal Reflections & Key Takeaways**

14. **Related Cases & Readings**

15. **Additional Resources**

**Important notes**:
- Use TBD for unknown professor (updated later based on course pattern)
- Extract case number from PDF filename or content
- Discussion questions come from assignment_context.json, not PDF
- Link to PDF: `[[CASE_NUMBER.pdf]]` at bottom

### Step 9: Move PDF to Attachments Folder
**Command**: `cp [source_path] "/mnt/c/Users/lindo/Documents/Obsidian/profession/b-school/courses/cases/attachments/[CASE_NUMBER].pdf"`

**Source paths** (check in order):
1. `/home/lindo/Downloads/` (Playwright downloads here)
2. `/mnt/c/Users/lindo/Downloads/` (Windows Downloads)

**Naming convention**: Use case number from PDF (e.g., `624-092.pdf`, `9-720-410.pdf`)

**Note**: Use `cp` instead of `mv` to avoid file loss issues with WSL/Windows filesystem operations

### Step 9a: Extract Exhibit Screenshots (Optional)
**When needed**: User requests screenshots of specific exhibits to embed in case note

**Script**: `~/.claude/forge/document/extract-pdf-page.py`

**Usage**:
```bash
python3 ~/.claude/forge/document/extract-pdf-page.py \
  "/path/to/case.pdf" \
  8 \
  "/path/to/output/exhibit-1.png" \
  --dpi 200
```

**What it does**:
1. Creates temporary virtual environment with pdf2image and poppler-utils
2. Extracts specified page number from PDF as high-resolution PNG
3. Saves to attachments folder with descriptive filename
4. Screenshot can be embedded in case note using: `![Description](attachments/filename.png)`

**Common exhibit naming**:
- `[CASE_NUMBER]-exhibit-1.png`
- `[CASE_NUMBER]-exhibit-7.png`
- `[CASE_NUMBER]-financial-summary.png`

**Example workflow**:
1. User: "include screenshot of Exhibit 1 in the case note"
2. Identify page number of Exhibit 1 from PDF
3. Extract page: `python3 ~/.claude/forge/document/extract-pdf-page.py "/mnt/c/.../9-718-419.pdf" 8 "/mnt/c/.../9-718-419-exhibit-1.png"`
4. Embed in case note: `![Exhibit 1: Strategy Diagram](attachments/9-718-419-exhibit-1.png)`

### Step 10: Update Case Studies Index
**File**: `/mnt/c/Users/lindo/Documents/Obsidian/profession/b-school/courses/cases/Case Studies Index.md`

**Updates required**:
1. **Quick Stats**: Increment "Total Cases" count
2. **By Course section**: Add case under appropriate course (START, MKT, STRAT, TOM, LEAD, FRC, FIN1)
3. **By Industry section**: Add to relevant industry category
4. **By Geographic Focus**: Add to appropriate region
5. **By Key Themes** (if applicable): Add to relevant theme section
6. **Chronological List**: Add under current month with format `- [[CASE_NUMBER CASE_TITLE]] - Read: YYYY-MM-DD (COURSE)`

**Format**: `- [[CASE_NUMBER CASE_TITLE]] - Brief description`

### Step 11: Update Professor Field (If Known)
**Pattern**: Check existing cases in same course to determine professor name

**Example**: All TOM cases show `professor: "Allison Mnookin"`

**Update**: Edit case note frontmatter to replace "TBD" with actual professor name

## Error Handling

### PDF Download Issues
- **Symptom**: Wrong PDF downloaded (e.g., FRC teaching note instead of case)
- **Solution**: Reopen case link, ensure correct PDF before downloading

### File Location Issues
- **Symptom**: Can't find downloaded PDF
- **Check**: Playwright downloads to Linux home (`/home/lindo/Downloads/`), not Windows Downloads
- **Search**: `find /home/lindo/Downloads -name "*.pdf" -mmin -10`

### Assignment Not Found
- **Symptom**: "Assignment not found" error
- **Solutions**:
  1. Try different search terms (case name vs assignment title)
  2. Check course code (TOM vs STRAT vs FRC)
  3. Use `./assignment-details "[keyword]"` to search

### Case Without HBSP Link
- **Symptom**: "No direct HBSP link found" or "No HBSP cases found"
- **Behavior**: Script now opens Canvas assignment page instead of exiting
- **Action**: Click the case link manually on the Canvas page to navigate to HBSP
- **Note**: Links may be hidden behind "external site" text in Canvas HTML
- **Alternative**: May be Canvas-hosted PDF or reading instead of HBSP case

## Todo List Pattern

**Initialize**:
```json
[
  {"content": "Open [Case] case in browser", "status": "in_progress", "activeForm": "Opening [Case] case in browser"},
  {"content": "Download PDF and save assignment context", "status": "pending", "activeForm": "Downloading PDF and saving assignment context"},
  {"content": "Read [Case] PDF", "status": "pending", "activeForm": "Reading [Case] PDF"},
  {"content": "Create structured case note from template", "status": "pending", "activeForm": "Creating structured case note from template"},
  {"content": "Move PDF to attachments folder", "status": "pending", "activeForm": "Moving PDF to attachments folder"},
  {"content": "Update Case Studies Index", "status": "pending", "activeForm": "Updating Case Studies Index"}
]
```

**Update** after each step completion, exactly one task `in_progress` at a time

## File Naming Conventions

### Case Notes
**Pattern**: `[CASE_NUMBER] [CASE_TITLE].md`

**Examples**:
- `624-092 Hospital for Special Surgery.md`
- `9-720-410 Hurtigruten.md`
- `N9-602-040 Donner Company.md`

### PDF Attachments
**Pattern**: `[CASE_NUMBER].pdf`

**Examples**:
- `624-092.pdf`
- `9-720-410.pdf`
- `N9-602-040.pdf`

## Quality Checklist

Before completing case digestion, verify:

- [ ] Case note has complete YAML frontmatter
- [ ] Discussion questions from assignment_context.json included
- [ ] Executive summary is 2-3 sentences
- [ ] All template sections present (even if marked "[To be filled]")
- [ ] PDF moved to attachments folder with correct naming
- [ ] Case Studies Index updated in all relevant sections
- [ ] Professor field updated (not "TBD") if determinable from course pattern
- [ ] Todo list shows all tasks completed

## Common Mistakes to Avoid

1. **Do not** use assignment description text as case content (it's just the questions)
2. **Do not** skip reading the actual PDF - it contains the case content
3. **Do not** forget to move PDF from Linux Downloads to Windows Obsidian attachments folder
4. **Do not** use placeholder values in case note metadata (extract from PDF)
5. **Do not** create multiple case notes for same case (check if exists first)
6. **Do not** forget to update Case Studies Index (required for every case)

## Future Enhancements

### Potential Improvements:
1. Automate PDF download (currently requires manual click)
2. Auto-detect case number from PDF content
3. Auto-populate professor from course pattern
4. Generate first-pass SWOT analysis from PDF content
5. Link related cases automatically based on tags
6. Create financial analysis tables automatically from exhibits

### Process Optimizations:
1. Batch multiple cases in single session
2. Pre-populate "Related Cases" from course syllabus
3. Auto-update "Last Updated" timestamp in Index
4. Generate case summary for quick reference

---

## Testing History

### 2025-10-05: Full Workflow Validation
**Test Cases**: Hilti Fleet Management (STRAT), Patrimonio Hoy (FIN1), Progyny (FIN1)

**Results**:
- ✅ Step 0: Duplicate detection working (prevented re-digesting Patrimonio Hoy)
- ✅ Step 2: Script execution with Linux Downloads path (`/home/lindo/Downloads/`)
- ✅ Step 4: UUID filename detection successful
- ✅ Browser close detection: Automatic exit when browser closes (polling method)
- ✅ Screenshot extraction: `~/.claude/forge/document/extract-pdf-page.py` created and tested
- ✅ All components verified end-to-end

**Key Fixes Applied**:
1. Changed download path from Windows to Linux (`/home/lindo/Downloads/`)
2. Implemented polling-based browser close detection (checks browser alive every 1 second)
3. Added Step 0 duplicate detection to prevent re-work
4. Created optional screenshot extraction tool for exhibits

**Scripts Status**:
- **Active**: `open-case-for-digestion.py` (fully tested and working)
- **Supporting**: `extract-pdf-page.py` (in forge/document, optional use)
- **Deprecated**: All temporary test scripts removed from /tmp

---

**Version**: 1.1
**Last Updated**: 2025-10-05
**Maintained by**: LinDon Harris
**Purpose**: Standardize HBS case digestion workflow for AI agent automation
**Status**: Fully tested and operational
