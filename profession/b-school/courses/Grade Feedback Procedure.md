# Grade Feedback Procedure

## Overview
Standard process for recording midterm and final grade feedback across all courses.

## Procedure

### 1. Extract Specific Feedback
- Read full feedback letter from professor
- **Ignore boilerplate text** - focus only on feedback specific to you
- Key items to extract:
  - Grade/placement (1, 2, or 3)
  - Specific comments about your performance
  - Looking-ahead guidance

### 2. Create Feedback File

**Location**: `/profession/b-school/courses/[COURSE]/feedback/`

**Files**:
- `midterm-feedback.md` - Midterm grade feedback
- `final-feedback.md` - Final grade feedback

**Frontmatter Template**:
```yaml
---
course: [COURSE]
section: [Letter]
professor: [Full Name]
date: YYYY-MM-DD
assessment_period: [Description]
midterm_grade: [1/2/3]
placement: [Description]
---
```

### 3. Update Rocks KPI Tracker

**File**: `/active/rocks-kpi-tracker.md`

**Location**: Pebble G - Don't get any 3s

**Format**:
```markdown
**[COURSE]**
- Midterm feedback: [x] [Grade] ([Placement Description])
- Final grade: [ ] No 3
```

**Example**:
```markdown
**MKT**
- Midterm feedback: [x] 1 (Top 30%)
- Final grade: [ ] No 3
```

## Grade Mapping

| Grade | Typical Placement | Description |
|-------|------------------|-------------|
| 1 | Top 20-30% | Higher Level of Contribution |
| 2 | Middle 50% | Middle Level of Contribution |
| 3 | Bottom 20% | Lower Level of Contribution |

**Note**: Exact percentages vary by professor and course phase (midterm vs final)

## Files to Update

1. `/profession/b-school/courses/[COURSE]/feedback/midterm-feedback.md` - Create new file
2. `/active/rocks-kpi-tracker.md` - Check box and record grade

---

**Version**: 1.0
**Created**: 2025-10-20
**Purpose**: Standardize grade feedback tracking across all RC courses
