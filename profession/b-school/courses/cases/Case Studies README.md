# HBS Case Studies Post-Class Archive System

## Overview
This system provides a structured approach to archiving and organizing Harvard Business School case studies AFTER class discussion. This is a knowledge repository, not a preparation tool.

## Directory Structure

### Central Case Repository
```
courses/cases/
├── attachments/           # Original PDF files
├── templates/            # Case study templates
├── Case Studies Index.md # Master index/MOC
├── Case Studies README.md # This file
└── [Individual case notes in root]
```

### Course Integration
```
courses/[COURSE] - [Name]/
└── Case Notes/
    ├── [Course] Cases Index.md    # Links to relevant cases
    └── [Case Name] Quick Prep.md  # Brief notes linking to full analysis
```

## How Cases Connect to Courses

The system uses a **post-class archive model**:

1. **Central Archive** (`/courses/cases/`): 
   - Complete case analyses with all exhibits
   - Black ink (pre-class) and blue ink (during-class) annotations preserved
   - Final takeaways and learnings captured
   - Cross-case searchability for exam review

2. **Course Links** (`/courses/[COURSE]/Case Notes/`):
   - Simple index pointing to archived cases
   - Organized by module/topic
   - No prep materials - just archive references

### Example Structure
```
STRAT - Strategy/Case Notes/
└── Strategy Cases Index.md         # Links to archived Strategy cases

cases/
├── 9-425-009 Keurig A Return to Growth.md    # Complete post-class archive
└── 9-505-078 Narayana Heart Hospital.md      # Complete post-class archive
```

## File Naming Convention
- **Case Notes**: `[Case-Number] [Company Name].md`
  - Example: `9-505-078 Narayana Hrudayalaya Heart Hospital.md`
- **PDFs**: Same as notes but in attachments folder
  - Example: `attachments/9-505-078 Narayana Hrudayalaya.pdf`

## Post-Class Archive Workflow

### Your Manual Process:
1. **Pre-class**: Read & annotate case with black ink
2. **During class**: Add blue ink annotations for class insights
3. **After class**: Write final takeaways on back page
4. **Send to Claude**: Email marked-up PDF for archiving

### Claude's Archive Processing:
1. **Extract** all content from marked-up PDF:
   - Original case text and exhibits
   - Black ink annotations (your pre-class analysis)
   - Blue ink annotations (class insights)
   - Final page takeaways
2. **Create comprehensive case note** in `/cases/` using the template with:
   - Metadata from case header
   - Your pre-class analysis in "My Analysis"
   - Class insights in "Class Discussion Notes"
   - Your takeaways in "Personal Reflections"
3. **Update indexes**:
   - Central Case Studies Index
   - Course-specific Cases Index (if exists)
4. **Store PDF** in `/attachments/[Case-Number] [Company Name].pdf`

### Annotation Key:
- **Black ink**: Pre-class preparation
  - Initial analysis
  - Questions
  - Financial calculations
  - Framework applications
- **Blue ink**: During class
  - Professor's insights
  - Peer perspectives
  - Corrected assumptions
  - Additional frameworks
- **Final page**: Synthesis
  - Key takeaways
  - Applications
  - Links to other cases

## Template Sections Explained

### Metadata (Frontmatter)
Essential for Obsidian search, filtering, and Dataview queries:
- `case_number`: Official HBS case number
- `tags`: For grouping and searching
- `key_topics`: Main themes for cross-referencing
- `decision_point`: The core decision/problem

### Core Content
1. **Executive Summary**: 2-3 sentence overview
2. **Case Context**: Background, industry, timeline
3. **Central Problem**: Clear statement of decision
4. **Analysis**: SWOT or other frameworks
5. **Financial Analysis**: Key metrics table
6. **Discussion Questions**: From case or professor

### Personal Sections
1. **My Analysis**: Your recommendations
2. **Class Discussion Notes**: Live notes during class
3. **Personal Reflections**: Key learnings and applications

## Search & Discovery

### Using Obsidian Search
- Find by company: `company:"Nike"`
- Find by topic: `tag:merger`
- Find by course: `course:"Finance"`
- Find by date: `date_read:2025-09`

### Dataview Queries
Example queries for dynamic lists:

```dataview
TABLE course, company, decision_point
FROM "courses/cases"
WHERE contains(tags, "merger")
SORT date_read DESC
```

## Best Practices

### During Reading
1. Fill metadata immediately
2. Highlight key numbers/facts
3. Note your initial thoughts in "My Analysis"
4. Mark discussion questions

### During Class
1. Use "Class Discussion Notes" section
2. Capture alternative viewpoints
3. Note professor's emphasis points
4. Update your analysis if perspective changes

### After Class
1. Complete "Personal Reflections"
2. Add related cases/readings
3. Update Index if new themes emerged
4. Link to relevant course notes

## Advanced Features

### Cross-Linking
- Link to course notes: `[[Strategy Course Notes]]`
- Link to concepts: `[[Porter's Five Forces]]`
- Link to similar cases: `[[Related Case Name]]`

### Tags Taxonomy
Primary tags:
- `#case-study` (always)
- `#course/[name]` (e.g., #course/strategy)
- `#industry/[name]` (e.g., #industry/healthcare)
- `#theme/[name]` (e.g., #theme/innovation)

### Automation Ideas
1. Use Templater plugin for automatic date insertion
2. Create QuickAdd macros for common updates
3. Use Dataview for dynamic case lists
4. Set up periodic notes for case review sessions

## Quick Actions

### Find Cases by...
- Recent: Check chronological list in Index
- Course: Navigate via Index → By Course
- Industry: Navigate via Index → By Industry
- Theme: Use tag search or Index → By Key Themes

### Prepare for Class
1. Open case note
2. Review "Discussion Questions"
3. Complete "My Analysis"
4. Check for related cases

### Review for Exams
1. Use Index to find all cases for course
2. Review "Key Learnings" in each
3. Compare similar decision types
4. Study financial analysis patterns

## Maintenance
- Weekly: Update Index with new cases
- Monthly: Review and consolidate tags
- Semester: Archive completed course cases

---
*System created: 2025-09-02*
*Last updated: 2025-09-02*