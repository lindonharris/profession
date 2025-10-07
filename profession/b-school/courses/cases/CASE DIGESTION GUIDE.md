# CASE DIGESTION GUIDE
*The single source of truth for AI agents processing HBS cases*

## 🎯 Quick Start
**Your Task**: Process a marked-up PDF case placed in `/courses/cases/incoming/`

1. **Extract** annotations from the PDF
2. **Create** a case note using the template
3. **Store** the PDF in attachments
4. **Update** the index

## 📍 Folder Structure
```
courses/
├── cases/
│   ├── incoming/             # 📥 New PDFs arrive here
│   ├── attachments/          # 📎 Processed PDFs stored here
│   ├── templates/            # 📝 Case Study Template.md
│   ├── archived_docs/        # 📦 Old documentation (ignore)
│   ├── Case Studies Index.md # 🗂️ Master index
│   └── CASE DIGESTION GUIDE.md # 📖 This file
└── [course]/                 # 📂 Course-specific folders (e.g., MKT, STRAT)
    └── case notes/           # 📂 Case notes subfolder
        └── [case].md         # 📄 Individual case notes
```

## 🖊️ Annotation Processing

### What LinDon Will Provide
*LinDon will manually transcribe and provide the black and blue ink notes rather than requiring extraction from PDFs*

| Ink Color | Content Type | Destination Section |
|-----------|-------------|-------------------|
| **Black** | Pre-class prep | → "My Analysis & Recommendations" |
| **Blue** | Class insights + takeaways | → "Class Discussion Notes" + "Personal Reflections" |

### Black Ink Includes
- Initial analysis and frameworks
- Questions LinDon wrote
- Financial calculations
- Underlined text with margin notes
- Strategic assessments

### Blue Ink Includes  
- Professor's insights
- Peer perspectives
- Corrected assumptions
- Additional frameworks from class
- Key takeaways (anywhere in document)
- Applications to other situations
- Synthesis notes

## 📝 Case Note Creation

### File Naming Convention
`[Case-Number] [Company Name].md`
- Example: `9-505-078 Narayana Hrudayalaya Heart Hospital.md`
- Place in: `/courses/[course]/case notes/`
  - START cases → `/courses/START/case notes/` (orientation week, ungraded)
  - MKT cases → `/courses/MKT/case notes/`
  - STRAT cases → `/courses/STRAT/case notes/`
  - FIN cases → `/courses/FIN/case notes/`
  - etc.

### Required Metadata (from case header)
```yaml
case_number: "9-XXX-XXX"
title: "Full Case Title"
course: "STRAT/FIN1/MKT/etc"
date_read: YYYY-MM-DD
company: "Company Name"
```

### Template Sections to Fill

#### 1. Executive Summary
- 2-3 sentence overview from the case

#### 2. Case Context
- Company background
- Industry landscape
- Timeline of events

#### 3. Central Problem/Decision
- State the main decision
- List constraints
- Define success metrics

#### 4. Analysis (SWOT)
- Extract from both black and blue ink

#### 5. Financial Analysis
- Create clean tables from calculations
- Note if black ink (pre-class) or blue (corrected)

#### 6. Discussion Questions
- Copy from original case

#### 7. My Analysis & Recommendations
- **ALL black ink content goes here**
- Include options, pros/cons, recommendations

#### 8. Class Discussion Notes
- **Blue ink insights go here**
- Professor quotes
- Alternative viewpoints
- Corrections to initial analysis
- **Track participation**: Times spoken, cold calls

#### 9. Personal Reflections
- **Blue ink takeaways go here**
- Key learnings
- Applications
- Remaining questions

#### 10. Related Cases & Readings
- Links to similar cases if mentioned

## 📎 Case Materials Storage

### Location
ALL case-related materials go in central attachments folder:
- **Main PDFs**: `/courses/cases/attachments/[Case-Number] [Full Case Title].pdf`
- **Supplementary Materials**: `/courses/cases/attachments/[Case-Number] [Full Case Title] - [Descriptor].[ext]`

### Naming Standard
**Main case PDFs:**
- Format: `[case_number] [Full Title].pdf`
- Example: `9-505-078 Narayana Hrudayalaya Heart Hospital.pdf`

**Supplementary materials (exhibits, templates, slides, etc.):**
- Format: `[case_number] [Full Title] - [Descriptor].[ext]`
- Examples:
  - `9-509-049 HubSpot - Exhibits.xls`
  - `9-120-126 Mira's Microbrewery Inc - Part 1 Takeaway Slides.pdf`
  - `114-024 University of Phoenix - Excel Template.xlsx`
  - `N2-713-470 Cola Wars Continue - 5 Forces Analysis.pdf`

### Key Rules
- **Always include full case title** (not just case number)
- **Use space-dash-space (` - `) separator** for supplementary materials
- **Match case note filename exactly** for main PDF
- **Be consistent** across all materials for same case

### Important
- Do NOT store case materials in individual course folders (e.g., /MKT/resources/)
- ALL exhibits, spreadsheets, and supplementary materials stay with the main case PDF
- This centralized approach ensures all case materials are findable in one location

## 🗂️ Index Updates

### Update Case Studies Index.md
Add entry under ALL relevant sections:

1. **By Date** (Chronological)
   ```markdown
   - 2025-09-03: [[9-XXX-XXX Company Name]] (COURSE)
   ```

2. **By Course**
   ```markdown
   ### STRAT
   - [[9-XXX-XXX Company Name]]
   ```

3. **By Industry** (if clear)
   ```markdown
   ### Healthcare
   - [[9-XXX-XXX Company Name]]
   ```

4. **By Geographic Focus** (if relevant)
   ```markdown
   ### India
   - [[9-XXX-XXX Company Name]]
   ```

5. **By Key Themes** (based on discussion)
   ```markdown
   ### Innovation
   - [[9-XXX-XXX Company Name]]
   ```

## ✅ Quality Checklist

Before marking complete:
- [ ] Both ink types extracted (black & blue)
- [ ] Case number matches filename exactly
- [ ] PDF moved to attachments folder
- [ ] All template sections populated
- [ ] Index updated in all relevant sections
- [ ] Metadata frontmatter complete
- [ ] Original PDF removed from incoming folder

## 🚫 Common Mistakes to Avoid

1. **Don't mix ink types** - Keep black and blue separate
2. **Don't create prep materials** - This is post-class only
3. **Don't skip index updates** - Add to ALL relevant sections
4. **Don't leave PDFs in incoming** - Move to attachments
5. **Don't create new sections** - Use template structure only

## 💡 Special Handling

### Financial Data
- Black ink calculations = LinDon's pre-class work
- Blue ink calculations = Class corrections/additions
- Create clean formatted tables

### Multiple Professors/Sections
- Note if case used across different sections
- Capture section-specific insights

### Exhibits
- Reference specific exhibit numbers in analysis
- Note which exhibits have heavy annotations

## 🔄 Workflow Summary

```mermaid
graph LR
    A[PDF in /incoming/] --> B[Extract Annotations]
    B --> C[Create Case Note]
    C --> D[Move PDF to /attachments/]
    D --> E[Update Index]
    E --> F[Delete from /incoming/]
```

## 📚 Template Location
`/courses/cases/templates/Case Study Template.md`

## ❓ Quick Reference

**Input**: `/courses/cases/incoming/[case].pdf`  
**Output**: `/courses/[course]/case notes/[case].md` + `/courses/cases/attachments/[case].pdf`  
**Index**: `/courses/cases/Case Studies Index.md`  
**Template**: `/courses/cases/templates/Case Study Template.md`

---
*System Version 2.0 - Simplified on 2025-09-02*  
*This guide supersedes all previous documentation*