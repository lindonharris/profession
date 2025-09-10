# Course Folder Structure

## Standard Directory Template

Every course follows this exact structure:

```
[COURSE]/                         # Course code only (e.g., MKT, STRAT, FIN1)
├── Professor [Name].md           # Professor info and teaching team
├── [COURSE] Syllabus.md         # Official syllabus document
├── case notes/                  # Individual case analyses
│   └── [Case Number] [Company].md
├── modules/                     # Module-specific notes and frameworks
│   └── [Module Name].md
├── exercises/                   # Practice problems and worksheets
│   └── [Exercise Name].md
└── resources/                   # Supplementary materials
    ├── [Resource].pdf
    └── [Reference].md
```

## Folder Definitions

### Core Folders (Required)

**case notes/**
- Individual case preparation and discussion notes
- File naming: `[Case Number] [Company Name].md`
- Example: `9-723-430 On (A).md`

**modules/**
- Conceptual frameworks and module summaries
- Organized by course module or topic
- Cross-referenced with cases

### Supporting Folders (As Needed)

**exercises/**
- Quantitative problems
- Practice sets
- Formula sheets
- Quick reference cards

**resources/**
- Course PDFs
- Reading materials
- External references
- Supplementary documents

## File Naming Conventions

### Required Files

1. **Professor File**: `Professor [Full Name].md`
   - Teaching team contacts
   - Office hours
   - Communication preferences

2. **Syllabus**: `[COURSE] Syllabus.md`
   - Course overview
   - Schedule and assignments
   - Grading policies

### Case Files

Format: `[Case Number] [Company Name].md`
- Keep official case numbers
- Use full company names
- Maintain consistent formatting

### Module Files

Format: `[Module Name].md`
- Descriptive module titles
- Match syllabus module names
- Number if sequential (e.g., `Module 1 - Strategy Fundamentals.md`)

## Content Organization Principles

1. **Flat hierarchy** - Maximum two levels deep
2. **Lowercase folders** - All folder names in lowercase
3. **Consistent naming** - Follow exact patterns above
4. **Single source** - One location per document type
5. **Clear purpose** - Each folder has distinct content type

## File Templates

### Professor Template
```markdown
# Professor [Name]

## Contact Information
- Email: 
- Office: 
- Office Hours: 

## Teaching Team
### Teaching Fellow
- Name: 
- Email: 
- Office Hours: 

### Course Assistant
- Name: 
- Email: 
```

### Case Note Template
```markdown
# [Case Number] [Company Name]

## Quick Facts
- Course: [[COURSE]]
- Date: YYYY-MM-DD
- Industry: 

## Key Decision


## Analysis


## Class Discussion


## Takeaways

```

### Module Note Template
```markdown
# [Module Name]

## Overview


## Key Frameworks


## Related Cases
- [[Case 1]]
- [[Case 2]]

## Application

```

---
*Standard established: September 2025*
*Version: 2.0*