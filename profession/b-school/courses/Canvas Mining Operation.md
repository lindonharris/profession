# Canvas Mining Operation

## Overview
**Canvas Mining** is the systematic process of extracting, organizing, and refactoring course information from Canvas LMS into a clean, accessible Obsidian knowledge base.

## The Problem
Canvas presents information in a scattered, chronological feed:
- Announcements buried in reverse order
- PDFs in various file folders
- Critical dates mentioned in passing
- Faculty info spread across multiple posts
- No unified view of course structure

## The Solution
Transform Canvas chaos into organized, searchable, offline-accessible course command centers in Obsidian.

## The Canvas Mining Process

### Phase 1: Discovery
**Navigate to these Canvas sections in priority order**:

1. **Syllabus** - Foundation document with course structure, grading, policies
2. **Files** - PDFs containing syllabi, course introductions, reading lists
3. **Announcements** - All communications, updates, clarifications, schedule changes
4. **Pages** - Static pages with faculty directories, resources, office locations
5. **Overview** - Course description, learning objectives, teaching philosophy
6. **Course Schedule** - Calendar view to verify dates and deadlines

**Identify high-value deposits**:
   - Course introduction/overview documents
   - Syllabus PDFs
   - Professor welcome messages
   - Schedule/calendar information
   - Grading breakdowns
   - Faculty/staff contact info

### Phase 2: Extraction
1. **Download source materials**
   - Save PDFs to course folder
   - Copy announcement text
   - Capture links and resources

2. **Read comprehensively**
   - Full read-through of major documents
   - Note all dates, deadlines, percentages
   - Identify all people mentioned
   - Map course structure/modules

### Phase 3: Refinement
1. **Create standardized structure EXACTLY per template**
   - Follow the [[Course Folder Structure]] template precisely
   - Set up Professor file using [[Professor Template]]
   - DO NOT create additional index or command center files

2. **Distill information** into ONLY these documents:
   - **[Course] Syllabus.md**: All course logistics, schedule, grading, policies
   - **Professor [Name].md**: All people, contacts, office hours, support

3. **Organize supporting materials**:
   - Original PDFs remain in folder for reference
   - Create Case Notes/ and Module Notes/ folders for future work
   - Do NOT create raw export files (.json, raw .md dumps)

## Key Principles

### 1. Completeness Over Perfection
Better to capture everything initially than to miss critical details. You can always refine later.

### 2. Separation of Concerns
- **Syllabus** = What, When, How Much (logistics)
- **Professor** = Who, Where, How to Contact (people)
- **Notes folders** = Your actual work

### 3. Preserve Sources
Keep original PDFs and materials - they're your audit trail and fallback reference.

### 4. Standardization Enables Speed
Using consistent structure across courses means you always know where to find things.

## Benefits of Canvas Mining

### Immediate
- **Everything in one place** - No more Canvas hunting
- **Offline access** - Study anywhere
- **Quick reference** - Find dates, contacts instantly
- **Clean mental model** - Know exactly where everything lives

### Long-term
- **Searchable archive** - Find anything across all courses
- **Connection building** - Link concepts between courses
- **Semester overview** - See all obligations at once
- **Knowledge persistence** - Your notes outlive Canvas access

## Tools Required

### Technical
- Canvas access with API token (stored in kymgr vault)
- `/canvas` direct access tool for downloads
- Obsidian for organization
- Template-compliant mining script: `/tmp/canvas_mine_template_compliant.py`

### Conceptual
- [[Course Folder Structure]] - Standard organization template
- [[Professor Template]] - Faculty information template

### Automated Mining Script
A template-compliant Python script is available at `/tmp/canvas_mine_template_compliant.py` that:
- Connects to Canvas API using token from vault
- Extracts course data (announcements, assignments, pages)
- Creates ONLY the template-required files:
  - Professor [Name].md
  - [Course] Syllabus.md
  - Case Notes/ folder with individual case templates
  - Module Notes/ folder (empty for future use)
- Does NOT create extra index files or raw exports
- Follows the Course Folder Structure template exactly

Example usage:
```python
mine_course(API_TOKEN, COURSE_ID, COURSE_CODE, COURSE_NAME, OUTPUT_DIR)
```

## Example: STRAT Canvas Mining

**Input**: 
- Introduction to RC Strategy PDF (8 pages)
- 4 announcement posts
- Various links and resources

**Output**:
- Strategy Syllabus.md (complete course overview)
- Professor Nanda.md (all faculty/staff info)
- Organized folder structure ready for notes

**Time**: ~20 minutes

## Quick Checklist for Canvas Mining

- Download all available PDFs
- Read all announcements (even old ones)
- Extract complete course schedule
- Identify all faculty/staff/contacts
- Note all grading components and weights
- Record all important dates
- Create syllabus document
- Create/update professor document
- Set up folder structure
- Preserve original materials

---
*Operation documented: September 1, 2025*
*Method proven with: STRAT - Strategy*