# Canvas Wrapper - Product Specification

**Product Name**: Canvas Wrapper (formerly Canvas Wiz)
**Status**: Product Design Phase
**Last Updated**: October 7, 2025
**Owner**: LinDon Harris

---

## Executive Summary

Canvas Wrapper solves the Canvas LMS navigation crisis that forces students to waste 10+ minutes hunting for assignments hidden across inconsistent course structures. By providing universal search, centralized dashboards, and embedded viewing of all content types, Canvas Wrapper eliminates the cognitive burden that Canvas creates through poor information architecture.

---

## Problem Statement

### The Canvas Navigation Crisis

- **Hidden assignments**: Instructors hide the Assignments link, forcing students to hunt through Modules, Pages, Announcements, Syllabus, Calendar, Files, and Discussions
- **No search functionality**: Canvas lacks course-level or global search capabilities
- **Inconsistent course structures**: Every instructor organizes content differently, requiring students to build unique mental maps for each course
- **Cognitive burden**: Stanford Teaching Commons officially acknowledges Canvas creates "unnecessary cognitive burden" through inconsistent information architecture
- **File access friction**: Students must download files to view them, creating workflow interruption and storage overhead

### Impact

- Students waste **5-10 minutes per session** locating materials across 5+ courses
- **15% higher** missed assignment rates in courses with hidden navigation
- **40% of support tickets** relate to finding content
- File downloads clutter local storage and break workflow continuity

---

## Product Vision

Canvas Wrapper provides the interface Canvas should have built:

1. **Universal Search** - Find anything across all courses instantly
2. **Sanity Dashboard** - Single authoritative view of everything that matters
3. **Embedded Viewer** - View all file types in-browser without downloads
4. **Zero Configuration** - Works immediately with existing Canvas accounts

---

## Core Features

### 1. Universal Search (Page 1)

**Purpose**: Index every piece of content across all Canvas courses, making everything instantly findable.

**Capabilities**:
- Search across assignments, files, discussions, announcements, grades, pages, modules
- Real-time results showing WHAT was found and WHERE it lives (full breadcrumb path)
- Filter by course, content type, date range, status
- Direct deep-linking to Canvas location

**Design Philosophy**: Bloomberg Terminal meets Notion
- Sharp corners, precise grid layouts
- Left-aligned titles, right-aligned metadata
- Dense information display that breathes
- Professional tool aesthetic - fast, precise, no-nonsense

**Implementation**: See `lovable-prompts/01-universal-search.md`

---

### 2. Sanity Dashboard (Page 2)

**Purpose**: Aggregate all assignments, deadlines, and updates into one authoritative view.

**Capabilities**:
- Unified view across all courses regardless of where content is hidden
- Structured zones: "Due Today," "This Week," "All Assignments"
- Location indicators showing where items are buried in Canvas
- Status tracking with minimal visual noise (vertical color bars, not badges)
- Real-time sync with Canvas API

**Design Philosophy**: Mission control center
- Rectangular zones with sharp edges
- Tabular data presentation
- Left-align labels, right-align values
- Zero ambiguity, zero anxiety

**Implementation**: See `lovable-prompts/02-sanity-dashboard.md`

---

### 3. Embedded Universal Viewer (NEW)

**Purpose**: View all Canvas file types in-browser without downloading, maintaining workflow continuity.

**Supported Formats**:
- **Spreadsheets**: `.xlsx`, `.xls`, `.csv`
- **Documents**: `.docx`, `.doc`, `.pdf`, `.txt`, `.rtf`
- **Presentations**: `.pptx`, `.ppt`
- **Web**: `.html`, `.htm`
- **Images**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`
- **Code**: `.py`, `.js`, `.java`, `.cpp`, `.md` (syntax highlighted)

**Viewer Capabilities**:
- **In-browser rendering** - No downloads required
- **Full-featured viewing** - Spreadsheet formulas, multi-page PDFs, presentation slides
- **Keyboard navigation** - Arrow keys for slides/pages, vim-style shortcuts
- **Zoom/pan controls** - Especially for PDFs and large spreadsheets
- **Search within document** - Find text across PDF pages, spreadsheet cells
- **Download option** - Available but not required
- **Print-friendly** - Direct browser print without download

**Technical Implementation**:
- **PDF**: PDF.js or similar open-source renderer
- **Office formats**: Office Online integration or SheetJS/Mammoth.js
- **Presentations**: Reveal.js or custom slide renderer
- **Code**: Highlight.js or Monaco Editor (view-only)

**UX Integration**:
- Viewer opens in modal overlay from search results or dashboard
- Breadcrumb navigation remains visible
- Quick access to "Open in Canvas" for editing
- Escape key closes viewer, returns to previous view

---

## Technical Architecture

### Stack (Proposed)

**Frontend**:
- React + TypeScript
- Tailwind CSS (for precise grid layouts)
- TanStack Query (data fetching/caching)
- Zustand (state management)

**Backend**:
- Node.js + Express (or Next.js API routes)
- Canvas API integration
- Redis (search index caching)
- PostgreSQL (user preferences, search index)

**File Viewing Libraries**:
- PDF.js (PDF rendering)
- SheetJS (Excel/CSV)
- Mammoth.js (DOCX)
- Highlight.js (code syntax)

### Canvas API Integration

**Required Scopes**:
- `url:GET|/api/v1/courses` - List courses
- `url:GET|/api/v1/courses/:course_id/assignments` - Assignments
- `url:GET|/api/v1/courses/:course_id/files` - Files
- `url:GET|/api/v1/courses/:course_id/discussion_topics` - Discussions
- `url:GET|/api/v1/courses/:course_id/announcements` - Announcements
- `url:GET|/api/v1/users/:user_id/courses` - User courses

**Authentication**:
- OAuth2 flow with Canvas
- API token stored securely
- Token refresh handling

---

## Design System

### Typography Hierarchy

- **Primary headings**: Bold, larger size (not color)
- **Secondary text**: Regular weight, smaller size
- **Metadata**: Right-aligned, muted but readable
- **Emphasis**: Weight and size, not color

### Layout Principles

1. **Sharp corners everywhere** - No border-radius
2. **Grid-based precision** - 8px baseline grid
3. **Left/right justification** - Creates visual rhythm
4. **Whitespace discipline** - Generous between sections, tight within
5. **Tabular data** - Aligned columns, scannable rows

### Color Palette

- **Primary**: High-contrast text on neutral backgrounds
- **Accent**: Minimal - vertical bars for status, not decorative
- **States**: Subtle background changes, not color shifts
- **Focus**: Clear keyboard navigation indicators

---

## User Flows

### First-Time Setup

1. Land on homepage
2. "Connect Canvas Account" CTA
3. OAuth flow to Canvas institution
4. Automatic course sync begins
5. Dashboard appears with all courses indexed
6. Optional: Brief tooltip tour (dismissible)

### Daily Usage

1. Open Canvas Wrapper dashboard
2. See "Due Today" and "This Week" at a glance
3. Search for specific assignment/file if needed
4. Click result → Embedded viewer opens
5. Review content in-browser
6. Close viewer or "Open in Canvas" to submit

### Search Flow

1. Type query in universal search
2. See instant results across all courses
3. Results show: Title, Course, Type, Location (breadcrumb)
4. Click result → Opens embedded viewer (if file) or deep-links to Canvas
5. Breadcrumb shows exact location in Canvas hierarchy

---

## Success Metrics

### User Engagement

- **Time to find content**: Target <30 seconds (vs. 5-10 minutes baseline)
- **Search usage**: 80%+ of sessions include search
- **Dashboard views**: Daily active usage >70% of student base
- **Viewer engagement**: 90%+ of file views use embedded viewer vs. download

### Problem Resolution

- **Support ticket reduction**: 40% decrease in "where is..." tickets
- **Missed assignments**: 15% reduction in late/missing submissions
- **Student satisfaction**: NPS >50 (Canvas baseline: ~20)

### Technical Performance

- **Search latency**: <200ms from keystroke to results
- **File viewer load**: <2s for typical documents
- **API reliability**: 99.5% uptime
- **Canvas sync**: Real-time updates within 5 minutes

---

## Roadmap

### Phase 1: MVP (Months 1-3)

- [ ] Canvas OAuth integration
- [ ] Basic dashboard with assignments aggregation
- [ ] Universal search (assignments, files only)
- [ ] PDF embedded viewer
- [ ] Basic file viewer (images, text)

### Phase 2: Enhanced Viewing (Months 4-6)

- [ ] Excel/spreadsheet viewer
- [ ] DOCX viewer
- [ ] PowerPoint viewer
- [ ] Code syntax highlighting
- [ ] Search within documents

### Phase 3: Advanced Features (Months 7-9)

- [ ] Mobile-responsive design
- [ ] Keyboard shortcuts
- [ ] Saved searches
- [ ] Custom dashboard layouts
- [ ] Browser extension (quick search)

### Phase 4: Scale & Polish (Months 10-12)

- [ ] Multi-institution support
- [ ] Collaboration features (share links)
- [ ] Offline mode
- [ ] Performance optimization
- [ ] Accessibility compliance (WCAG 2.1 AA)

---

## Competitive Landscape

### Existing Solutions

**Canvas Native**:
- ❌ No search
- ❌ Inconsistent navigation
- ❌ Files require download
- ✅ Official integration

**Browser Extensions** (various):
- ⚠️ Limited search capabilities
- ❌ No centralized dashboard
- ❌ No embedded viewing
- ❌ Fragile (break with Canvas updates)

**Student-Built Tools**:
- ⚠️ Institution-specific
- ❌ Poor UX
- ❌ No maintenance
- ❌ Security concerns

### Canvas Wrapper Advantages

- ✅ **Comprehensive search** across all content types
- ✅ **Unified dashboard** regardless of course structure
- ✅ **Universal file viewer** - no downloads needed
- ✅ **Professional design** - not a student hack
- ✅ **Official API** - secure and maintained
- ✅ **Zero configuration** - works immediately

---

## Business Model (Future Consideration)

### Potential Revenue Streams

1. **Freemium SaaS**
   - Free: Basic search + dashboard
   - Premium ($5-10/month): Advanced features, unlimited history, mobile app

2. **Institutional Licensing**
   - University-wide deployment
   - Custom branding
   - SSO integration
   - Analytics dashboard for admins

3. **API Access**
   - Developer tier for building on top of Canvas Wrapper
   - Integration with study tools (Notion, Obsidian, etc.)

---

## Open Questions

- [ ] Should we support guest/observer accounts (parents, TAs)?
- [ ] How to handle Canvas course archives after semester ends?
- [ ] Should we cache file content or proxy real-time?
- [ ] Mobile app vs. mobile-responsive web?
- [ ] Should we support Canvas Studio videos?
- [ ] How to handle private/restricted files?
- [ ] Should search index include discussion comments?
- [ ] Do we need version control for edited files?

---

## Resources

- **Lovable Prompts**: `/lovable-prompts/` folder
- **Canvas API Docs**: https://canvas.instructure.com/doc/api/
- **Related Research**: `/mnt/c/Users/lindo/Downloads/canvas_lms_navigation_crisis_2024.md`
- **Canvas Direct Access Tools**: `~/.claude/direct-access-tools/canvas/`

---

## Next Steps

1. [ ] Validate embedded viewer technical feasibility (library testing)
2. [ ] Create wireframes for viewer modal/overlay
3. [ ] Build Canvas API authentication prototype
4. [ ] Design search index schema
5. [ ] Create Lovable prompts for embedded viewer page
6. [ ] User research: Validate problem severity with HBS students
7. [ ] Competitive analysis: Deep dive on existing tools
8. [ ] Technical spike: PDF.js + SheetJS integration

---

**Document Version**: 1.0
**Created**: October 7, 2025
**Author**: LinDon Harris
