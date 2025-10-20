# Canvas Wrapper - Product Specification

**Product Name**: Canvas Wrapper (formerly Canvas Wiz)
**Status**: UI Prototype Complete (Lovable.dev) - **Continue Frontend in Lovable**
**Last Updated**: October 17, 2025
**Owner**: LinDon Harris
**Repository**: `/mnt/c/Users/lindo/Documents/Github/lovalytics-wiz` (Lovable project)

---

## 🔄 Development Workflow (Claude ↔ Lovable Process)

This is our iterative development process for building Canvas Wrapper:

### The Cycle

1. **Claude provides Lovable prompt** → Detailed, implementation-ready prompt from this spec
2. **User gives prompt to Lovable** → Copy/paste into Lovable.dev
3. **Lovable responds with plan** → Lovable analyzes code and proposes implementation
4. **User shares plan with Claude** → Paste Lovable's response back here
5. **Claude pulls latest changes** → `cd /mnt/c/Users/lindo/Documents/Github/lovalytics-wiz && git pull origin main`
6. **Claude validates plan** → Reviews against spec, checks actual code in repository
7. **Claude gives feedback** → Either "implement the plan" or specific adjustments
8. **User tells Lovable** → "Implement the plan" or provides Claude's feedback
9. **Lovable implements** → Makes code changes in real-time
10. **Claude pulls changes & validates** → Verifies implementation matches spec requirements
11. **Claude updates product spec** → Marks features complete, updates next prompts
12. **Repeat** → Move to next feature/sprint

### Key Principles

- **Claude owns the spec** - Product vision, feature requirements, workflow insights
- **Lovable owns the implementation** - Code generation, component architecture, routing
- **User is the bridge** - Copy/paste between Claude and Lovable, provides validation
- **Repository is source of truth** - Claude reviews actual code at `/mnt/c/Users/lindo/Documents/Github/lovalytics-wiz`

### When to Deviate

- If Lovable proposes a better technical approach → Accept and update spec
- If implementation reveals missing requirements → Add to spec before continuing
- If a feature proves unnecessary → Remove from sprint and document why

---

## 📍 Where We Are & What's Next

**Current State** (Updated: October 20, 2025):
- ✅ **ALL SPRINTS COMPLETE** - Frontend MVP fully functional in Lovable.dev
- ✅ Sprint 1-4: Navigation, Search, Dashboard, Courses, Files, Calendar, Settings
- ✅ Submission status system (replaced completion tracking with Canvas truth)
- ✅ Error handling with professional toast notifications
- ✅ Bloomberg Terminal aesthetic throughout (sharp corners, professional spacing)
- ✅ Centralized mock data ready for API replacement
- 🚀 **READY FOR BACKEND INTEGRATION** - Replace mock data with Canvas API

**Key Insight from Workflow Analysis**:
Your Direct Access Tools usage shows the real workflow:
1. Search for assignment ("Springfield Hospital")
2. Get embedded link (HBSP case URL)
3. View assignment details (questions, due date)
4. Mark as complete

Canvas Wrapper solves this but needs more frontend pages before backend makes sense.

**Immediate Action**: **Continue building frontend in Lovable** (4 sprints, ~8-12 features)

**Why Frontend First?**:
- Design exploration is fast in Lovable
- Clarifies what data structures backend needs
- Validates UX before expensive API integration
- Your Direct Access Tools show what's actually needed (not grades/notifications)

**Next Lovable Prompt** (Start Here ⬇️):
```
Add a global navigation bar that appears on BOTH the existing Search page and Dashboard page.
The nav should be persistent across all pages. Include:

- Logo/home link (left) - clicking should navigate to Dashboard
- Global search input (center) - focus with `/` shortcut, navigates to Search page
- Course dropdown (right) - placeholder "All Courses" for now
- Settings icon (far right) - placeholder button for now

IMPORTANT: Update the existing Search.tsx and Dashboard.tsx to include this nav bar at
the top. Make sure the search input in the nav works the same as the existing search page.

Bloomberg Terminal aesthetic: sharp corners, professional sans-serif fonts, clean grid
layout. The nav should feel like it was always part of the existing pages.
```

**Why this matters**: The nav bar needs to wrap the existing Search and Dashboard pages
you already built. When you type in the nav search bar, it should route to the Search
page. When you click the logo, it should route to Dashboard. This creates the foundation
for adding new pages later (Courses, Calendar, Settings).

---

## Build Progress Tracker

### Phase 1: Frontend UI (Lovable.dev) ✅ COMPLETE

**Universal Search Page**
- [x] Search interface with instant results display
- [x] Bloomberg Terminal aesthetic (sharp corners, grid layouts)
- [x] Breadcrumb paths showing Canvas location hierarchy
- [x] Professional sans-serif typography (Arial/system fonts)
- [x] Optimized grid layout with ample space for links column

**Sanity Dashboard**
- [x] "Due Today" zone with tabular data
- [x] "This Week" zone with assignments list
- [x] "All Assignments" comprehensive view
- [x] Mission control aesthetic with rectangular zones
- [x] Status indicators (vertical color bars)

**Embedded Links Feature**
- [x] Extract multiple hyperlinks from assignment descriptions
- [x] Display links as clickable buttons (PDF, XLSX, REPO, WEB)
- [x] Links column with 3x more space (col-span-3)
- [x] Horizontal link layout with proper wrapping
- [x] Type-based styling (PDF vs XLSX vs external)

**Design System**
- [x] Sharp corners throughout (no border-radius)
- [x] Grid-based precision (8px baseline)
- [x] Left/right justification for visual rhythm
- [x] Professional typography hierarchy
- [x] Tabular data presentation (not cards)

---

## Frontend Completion Roadmap (Lovable.dev Phase 1.5)

**Context from Direct Access Tools Workflow:**

Current workflow (that Canvas Wrapper replaces):
1. Run `./canvas today` → Find "Springfield Hospital" assignment
2. Run `open-case-for-digestion.py` → Opens HBSP link in browser
3. Download PDF manually
4. Extract assignment questions from Canvas HTML

Canvas Wrapper streamlined workflow:
1. **Search "Springfield"** → See assignment with HBSP link embedded
2. **Click link** → Opens case directly (skip Canvas navigation)
3. **View questions** → Right in the interface
4. **Mark complete** → Simple checkbox

**Core Insight**: Students need fast access to embedded links and assignment details, not grades/notifications/bulk operations.

### Pages & Components To Build (Priority Order)

#### 1. Navigation & Layout Foundation
- [ ] **Global Navigation Bar** - Persistent across all pages
  - Logo/home link (left)
  - Global search bar (center, always accessible with `/` shortcut)
  - Course dropdown switcher (right)
  - Settings icon (far right)
  - Clean, Bloomberg-style header with sharp corners

- [ ] **Breadcrumb Component** - Show current location
  - Format: `Home > Courses > FRC > Assignment Details`
  - Clickable navigation back through hierarchy
  - Subtle, non-intrusive styling

- [ ] **Responsive Container Layout**
  - Desktop-first (1440px optimal)
  - Works on tablets (768px+)
  - Maintains grid precision on all sizes

#### 2. Course Management Pages
- [ ] **Course List Page** (`/courses`)
  - **Purpose**: Central hub showing all enrolled courses
  - **Layout**: Grid of course cards (3 columns on desktop)
  - **Each card shows**:
    - Course code + name (e.g., "FRC - Financial Reporting & Control")
    - Instructor name
    - Next assignment due date + time remaining
    - Assignment count (e.g., "3 due this week")
    - Recent activity indicator (green dot if updates in last 24hrs)
  - **Actions**: Click card → navigate to Individual Course View
  - **Sorting**: Recent activity, Upcoming deadlines, Alphabetical
  - **Design**: Sharp corners, tabular data within cards, course color accent bar

- [ ] **Individual Course View** (`/courses/:id`)
  - **Purpose**: Deep dive into single course materials
  - **Three-tab layout**:
    1. **Assignments Tab** (default):
       - Same table layout as dashboard
       - Shows embedded links column
       - Filter: All | Upcoming | Past Due | Completed
    2. **Files Tab**:
       - Folder tree navigation (left sidebar, collapsible)
       - File list with type icons (right main area)
       - Search within course files
       - Download + Quick View buttons
    3. **Overview Tab**:
       - Course description
       - Syllabus (if available)
       - Instructor info
       - Recent announcements (last 5)
  - **Header**: Course name, code, instructor
  - **Design**: Bloomberg aesthetic, tabular data, sharp corners

#### 3. Enhanced Search & Filters
- [ ] **Advanced Filters Panel** (on Search page)
  - **Collapsible sidebar** (left side of search results)
  - **Filters**:
    - Courses (multi-select checkboxes)
    - Content Type (Assignments | Files | Discussions)
    - Date Range (dropdown: Today | This Week | This Month | Custom)
    - Status (Incomplete | Complete | Past Due)
  - **Sort Options**:
    - Relevance (default)
    - Due Date (nearest first)
    - Course (alphabetical)
    - Type (assignments, then files, etc.)
  - **Actions**: "Apply Filters" + "Clear All" buttons
  - **Persistence**: Filters stay active during session
  - **Design**: Clean form controls, sharp corners, no unnecessary decoration

- [ ] **Assignment Detail Modal**
  - **Trigger**: Click assignment title anywhere (search, dashboard, course view)
  - **Shows**:
    - Assignment title (large, bold)
    - Course + breadcrumb location
    - Due date + time remaining (prominent)
    - Full description (HTML rendered, proper formatting)
    - **Embedded links** (large, prominent section with link buttons)
    - Points possible
    - Submission type (online, paper, none)
  - **Actions**:
    - "Open in Canvas" button (external link icon)
    - "Mark Complete" checkbox (persists locally)
    - Close (X button + Escape key)
  - **Design**: Modal overlay (semi-transparent backdrop), centered card, Bloomberg aesthetic

#### 4. File Management
- [ ] **File Browser Component** (reusable)
  - **Layout**: Two-pane (folder tree left, file list right)
  - **Folder Tree** (left pane, 30% width):
    - Collapsible folders with indent levels
    - Root folder = course name
    - Expand/collapse with arrow icons
    - Selected folder highlighted
  - **File List** (right pane, 70% width):
    - Table view: Filename | Type | Size | Modified Date
    - Type icons (PDF, XLSX, DOCX, etc.)
    - Sort by: Name, Type, Size, Date
    - Search box (filters current folder)
  - **Actions per file**:
    - Download button
    - "Quick View" button (future: embedded viewer)
  - **Design**: Sharp grid, clear hierarchy, professional file manager aesthetic

- [ ] **Standalone Files Page** (`/files`)
  - **Purpose**: Global file browser across all courses
  - **Header**: Course filter dropdown (All Courses | FRC | LEAD | etc.)
  - **Content**: File Browser Component (described above)
  - **Recent Files Section** (top, above browser):
    - Shows last 10 accessed files
    - Quick access links
    - "See All" button → goes to full browser
  - **File Type Filters**: Buttons for PDFs | Spreadsheets | Documents | All
  - **Design**: Consistent with rest of app, tabular data

#### 5. Calendar & Timeline
- [ ] **Calendar View Page** (`/calendar`)
  - **Month View** (default):
    - Grid calendar showing current month
    - Assignments marked on due dates
    - Dots colored by course (each course gets unique color)
    - Hover over date → tooltip shows assignment names
    - Click date → opens Assignment Detail Modal
  - **Week View** (alternative):
    - Horizontal timeline showing 7 days
    - Assignments listed under each day
    - More detailed than month view
  - **Navigation**:
    - Previous/Next month arrows
    - "Today" button (jumps to current date)
    - Month/Year selector dropdown
  - **Legend**: Course color key (shows which course = which color)
  - **Design**: Professional calendar grid, sharp corners, clear date cells, Bloomberg aesthetic

#### 6. Settings & Account
- [ ] **Settings Page** (`/settings`)
  - **Three sections** (simple, no complex options):
    1. **Account**:
       - Canvas institution name
       - User name + email (read-only)
       - "Disconnect Canvas" button (red, confirmation dialog)
       - "Reconnect" button (if disconnected)
    2. **Display**:
       - Default view on load (Dashboard | Calendar | Courses)
       - Course colors (assign custom color to each course)
       - Completed items (Show | Hide from main views)
    3. **Sync**:
       - Last sync time display
       - "Sync Now" button (manual refresh)
       - Sync frequency (15min | 30min | 1hour - future feature)
  - **Design**: Clean form layout, left-aligned labels, right-aligned controls

#### 7. UI States & Feedback
- [ ] **Empty States** (contextual, varies by location)
  - **No search results**:
    - Icon + message: "No items found matching 'Springfield Hospital'"
    - Suggestion: "Try different keywords or adjust filters"
  - **No assignments today**:
    - Icon + message: "Nothing due today!"
    - CTA: "Check 'This Week' or 'All Assignments'"
  - **No files in course**:
    - Icon + message: "No files available yet"
    - Suggestion: "Check back after instructor uploads materials"
  - **Design**: Centered, subtle icon, helpful messaging, not anxiety-inducing

- [ ] **Loading States**
  - **Dashboard loading**: Skeleton rows (shimmer effect) for assignment tables
  - **Search loading**: Small spinner centered in results area
  - **File loading**: Spinner inside file list pane
  - **Nav bar sync**: Tiny spinner icon next to course dropdown during sync
  - **Design**: Never block entire UI, show partial data, subtle indicators

- [ ] **Error States**
  - **Canvas API error**: Toast notification (top-right): "Connection issue. Showing cached data." + "Retry" button
  - **Search error**: In-line message: "Search temporarily unavailable. Try again in a moment."
  - **File download error**: Toast: "Download failed. Try opening in Canvas instead."
  - **Design**: Toast notifications auto-dismiss after 5s, non-blocking, clear action CTAs

#### 8. Essential Interactions
- [ ] **Completion Tracking** (simple, local-first)
  - Checkbox next to each assignment (all views: dashboard, search, course)
  - Checked = complete (visual: subtle strikethrough + opacity fade)
  - Completed items moved to bottom of lists
  - Completion state saved in localStorage (until backend ready)
  - "Show Completed" toggle to hide/show completed items

**NOT Building** (Removed from scope):
- ❌ Grades overview page (not core workflow)
- ❌ Notifications center (announcements not critical)
- ❌ Bulk actions (students work one assignment at a time)
- ❌ Right-click context menus (keep UI simple)
- ❌ Hover tooltips (just show info directly in UI)
- ❌ Keyboard shortcuts (unnecessary complexity)
- ❌ Dark mode (polish for later, desktop light theme is fine)
- ❌ Mobile app (responsive web is sufficient)
- ❌ Social/collaboration features (not MVP)

---

### Phase 2: Backend Integration ❌ NOT STARTED

**Canvas API Connection**
- [ ] OAuth2 authentication flow setup
- [ ] Canvas API token storage (secure)
- [ ] Token refresh handling
- [ ] Multi-institution support (different Canvas instances)

**Data Fetching & Indexing**
- [ ] Course list retrieval (`/api/v1/courses`)
- [ ] Assignments fetching (`/api/v1/courses/:course_id/assignments`)
- [ ] Files indexing (`/api/v1/courses/:course_id/files`)
- [ ] Discussions retrieval (`/api/v1/courses/:course_id/discussion_topics`)
- [ ] Announcements fetching (`/api/v1/courses/:course_id/announcements`)
- [ ] Real-time sync (polling or webhooks)

**Search Index**
- [ ] Redis/PostgreSQL setup for search caching
- [ ] Full-text search implementation
- [ ] Link extraction from HTML assignment descriptions
- [ ] Metadata indexing (due dates, status, points)

**Replace Mock Data**
- [ ] Remove hardcoded assignments from Dashboard
- [ ] Remove hardcoded search results from Search page
- [ ] Connect UI components to real API data
- [ ] Handle loading states and errors

### Phase 3: Embedded File Viewer ❌ NOT STARTED

**Viewer Infrastructure**
- [ ] Modal overlay component for file viewing
- [ ] Breadcrumb navigation in viewer
- [ ] "Open in Canvas" quick link
- [ ] Escape key close functionality
- [ ] Keyboard navigation (arrow keys, vim shortcuts)

**File Type Support**
- [ ] PDF viewer (PDF.js integration)
- [ ] Excel/CSV viewer (SheetJS integration)
- [ ] DOCX viewer (Mammoth.js integration)
- [ ] PowerPoint viewer (custom or library)
- [ ] Code viewer (Highlight.js with syntax highlighting)
- [ ] Image viewer (built-in browser support)
- [ ] HTML/Web viewer (iframe or sanitized render)

**Viewer Features**
- [ ] Zoom/pan controls for PDFs
- [ ] Search within document
- [ ] Multi-page navigation (PDFs, presentations)
- [ ] Formula display (Excel sheets)
- [ ] Download option (but not required)
- [ ] Print-friendly mode

### Phase 4: Deployment & Infrastructure ❌ NOT STARTED

**Repository Setup**
- [ ] Export code from Lovable.dev to GitHub
- [ ] Set up local development environment
- [ ] Configure build system (Vite/Next.js)
- [ ] Set up environment variables management

**Backend Services**
- [ ] Node.js/Express server setup (or Next.js API routes)
- [ ] Database setup (PostgreSQL for user data, Redis for caching)
- [ ] Environment configuration (dev/staging/prod)

**Deployment**
- [ ] Choose hosting platform (Vercel/Netlify/Railway)
- [ ] Set up CI/CD pipeline
- [ ] Configure domain and SSL
- [ ] Performance monitoring setup

### Phase 5: Polish & Testing ❌ NOT STARTED

**Functionality**
- [ ] Error handling for API failures
- [ ] Loading states for all async operations
- [ ] Empty states (no assignments, no search results)
- [ ] Rate limiting for Canvas API calls
- [ ] Offline mode (cached data)

**UX Enhancements**
- [ ] Filter/sort controls on search results
- [ ] Saved searches functionality
- [ ] Custom dashboard layouts
- [ ] Keyboard shortcuts (global search, navigation)
- [ ] Mobile-responsive design

**Quality Assurance**
- [ ] Cross-browser testing (Chrome, Firefox, Safari, Edge)
- [ ] Performance optimization (code splitting, lazy loading)
- [ ] Accessibility compliance (WCAG 2.1 AA)
- [ ] Security audit (XSS, CSRF, token storage)
- [ ] User testing with HBS students

### Phase 6: Advanced Features ⏸️ FUTURE

**Collaboration**
- [ ] Share search results via link
- [ ] Collaborative assignment tracking
- [ ] Group study features

**Analytics & Insights**
- [ ] Assignment completion tracking
- [ ] Time management analytics
- [ ] Course workload visualization

**Integrations**
- [ ] Browser extension for quick search
- [ ] Notion/Obsidian integration
- [ ] Calendar sync (Google/Outlook)
- [ ] Mobile app (iOS/Android)

---

## Current Blockers

1. **Code Export**: Need to download code from Lovable.dev to local/GitHub repo
2. **Canvas API Access**: Need to set up OAuth2 app in Canvas developer console
3. **Backend Infrastructure**: Need to choose and set up backend stack
4. **Link Extraction Logic**: Need to parse HTML assignment descriptions to extract embedded links

## Immediate Next Steps (Frontend-First Approach)

### Sprint 1: Navigation & Core Pages ✅ COMPLETE
1. [x] **Global Navigation Bar** - Add to existing Search and Dashboard pages
   - Update Search.tsx and Dashboard.tsx to include nav at top
   - Logo → routes to Dashboard
   - Search input → routes to Search page
   - Course dropdown → routes to Courses page
   - Settings icon → placeholder for now

2. [x] **Course List Page** - New page accessible from course dropdown
   - Create `/courses` route
   - Grid of course cards (3 columns)
   - Each card: code, name, instructor, next due date, assignment count
   - Click card → navigate to Individual Course View (Sprint 2)
   - Course dropdown in nav links to this page

3. [x] **Update Routing** - Connect pages together
   - Dashboard = `/` (home/default)
   - Search = `/search`
   - Courses = `/courses`
   - Navigation works between all pages

4. [x] **Empty States** - Add to existing pages
   - Search page: "No results found" message
   - Dashboard: "Nothing due today" message

**Lovable Prompt** (Copy this):
```
Add a global navigation bar to the existing Search and Dashboard pages. The nav should:

1. Update Search.tsx and Dashboard.tsx to include nav at top
2. Logo/home icon (left) - routes to Dashboard (/)
3. Search input (center) - routes to Search page (/search) when user types
4. Course dropdown (right) - shows "All Courses" placeholder
5. Settings icon (far right) - placeholder for now

Then create a NEW Courses page (/courses) that shows a grid of course cards.
Each card shows: course code, name, instructor, next deadline, assignment count.
Make the course dropdown in the nav link to this new Courses page.

Bloomberg aesthetic: sharp corners, professional sans-serif, clean grids.
```

### Sprint 2: Course Deep Dive & Filters ✅ COMPLETE
5. [x] **Individual Course View** - Accessible by clicking course card from Courses page
   - Create `/courses/:id` route (e.g., `/courses/cs-3410`)
   - Three tabs: Assignments | Files | Overview
   - Header shows: Course code, name, instructor, back to Courses link
   - Assignments tab: Same table as Dashboard with embedded links
   - Files tab: Placeholder "Files browser coming soon"
   - Overview tab: Course description, instructor info, announcements

6. [x] **Advanced Filters Panel** - Add to existing Search page
   - Collapsible sidebar on left of search results
   - Filters: Courses (multi-select checkboxes), Content Type, Date Range, Status
   - "Apply Filters" and "Clear All" buttons
   - Filters affect search results in real-time
   - Filter state persists during session

7. [x] **Assignment Detail Modal** - Click assignment title anywhere to open
   - Works on Dashboard, Search, and Course View pages
   - Shows: title, course, due date, location, full description, embedded links
   - "Open in Canvas" button + "Mark Complete" checkbox
   - Close with X or Escape key
   - Modal uses shadcn Dialog component

8. [x] **Shared Types & Utilities** - Infrastructure for consistency
   - Created `src/types/index.ts` with Assignment, Course, SearchFilters interfaces
   - Created `src/lib/filters.ts` with filter helper functions
   - Updated routing in App.tsx for all new pages

**Lovable Prompt** (Copy this):
```
Create an Individual Course View page (/courses/:id) that opens when clicking a course
card from the Courses page. Include:

1. Header: Course code + name, instructor, "← Back to Courses" link
2. Three tabs: Assignments | Files | Overview (Assignments is default)
3. Assignments tab: Same table layout as Dashboard with embedded links
4. Files tab: Placeholder text "Files browser coming soon"
5. Overview tab: Course description + instructor info + recent announcements

Also add an Advanced Filters sidebar to the existing Search page (collapsible on left).
Include filters for: Courses (multi-select), Content Type, Date Range, Status.

Finally, create an Assignment Detail Modal that opens when clicking any assignment title
(on Dashboard, Search, or Course pages). Show full description with embedded links,
"Open in Canvas" button, and "Mark Complete" checkbox.

Bloomberg aesthetic throughout.
```

### Sprint 3: File Management & Calendar ✅ COMPLETE
9. [x] **File Browser Component** - Two-pane layout with folder tree and file list
   - Created `src/components/FileTree.tsx` with recursive folder rendering
   - Collapsible folders with expand/collapse arrows (12px indentation per level)
   - Selected folder highlighting with accent color and border
   - File count badges per folder

10. [x] **Standalone Files Page** - Global file browser across all courses
   - Created `src/pages/Files.tsx` with complete two-pane layout
   - Course filter dropdown (All Courses | CS 3410 | MATH 2210, etc.)
   - File type filters (All | PDFs | Spreadsheets | Documents)
   - Recent Files section with localStorage persistence
   - Sortable file table (Name, Type, Size, Modified Date)
   - Search within current folder
   - Download + Quick View buttons per file

11. [x] **Supporting Infrastructure**
   - Created `src/lib/mockFiles.ts` with 50+ mock files across courses
   - Created `src/lib/fileUtils.ts` with formatting, sorting, filtering utilities
   - Added file types to `src/types/index.ts` (FileItem, FolderNode, etc.)
   - Updated Navigation component with Files button
   - Added `/files` route to App.tsx

12. [ ] **Calendar View** - Month/week views with color-coded assignments (moved to Sprint 4)
13. [ ] **Error States** - Toast notifications for errors (moved to Sprint 4)

**Lovable Prompt**: "Build a professional file browser with two panes: folder tree (left, collapsible) and file list table (right). Show file type icons, download buttons, and search within folder. Bloomberg Terminal aesthetic."

### Sprint 4: Calendar, Settings & Final Polish ✅ COMPLETE
12. [x] **Calendar View** - Month grid with color-coded assignments
   - Created `src/pages/Calendar.tsx` (333 lines) with complete calendar page
   - Created `src/lib/calendarUtils.ts` (107 lines) with date utilities
   - Month view grid showing current month (7×6 = 42 cells)
   - Assignments marked on due dates with course color dots (max 3 visible + overflow)
   - Click date → opens DateAssignmentsModal (multiple assignments) or AssignmentDetailModal (single)
   - Previous/Next month navigation with chevron buttons
   - "Today" button to jump to current date
   - Course legend showing all course colors
   - Bloomberg aesthetic: sharp grid, clear date cells, professional spacing
   - Uses centralized mock data from `src/lib/mockData.ts`
   - Added Calendar button to Navigation component
   - Added `/calendar` route to App.tsx

13. [x] **Settings Page** - Account, Display, Sync sections
   - Created `src/pages/Settings.tsx` with three clean sections
   - Account: Canvas connection status, institution, user info, disconnect button
   - Display: Default view dropdown, course color pickers, localStorage persistence
   - Sync: Last sync time, manual sync button with error simulation
   - Clean form layout, left-aligned labels, right-aligned controls
   - Bloomberg aesthetic: sharp corners, professional spacing

14. [x] **Submission Status System** (Replaced "Completion Tracking")
   - **Removed**: Local "mark complete" checkboxes (confusing duplicate state)
   - **Added**: Submission status from Canvas (submitted/not-submitted/overdue)
   - Left-edge colored status bars (primary indicator): green=submitted, red=overdue, blue=upcoming
   - Subtle metadata text: "Submitted Oct 14" in assignment lists
   - Modal status line: small icon + text (no boxed badges)
   - Updated `Assignment` type with `status` and `submittedAt` fields
   - Sharp corners removed from toast notifications (line 26 in toast.tsx)

15. [x] **Error States** - Toast notifications with sharp corners
   - **Settings sync error**: 30% random failure, destructive toast with Retry button (10s duration)
   - **Search error**: Inline message (NOT toast) for empty queries, red styling with AlertCircle
   - **File download error**: 20% random failure, destructive toast "Download failed" (5s duration)
   - Success toasts for confirmation (3-5s duration)
   - Toast UI updated: removed `rounded-md` for Bloomberg aesthetic

16. [x] **Responsive Layout** - Works on tablets and desktops
   - Two-pane layouts with collapsible left panes (Files, Search filters)
   - Grid layouts adapt properly (courses grid, assignment tables)
   - Navigation responsive with proper breakpoints
   - Tested at 768px+ breakpoint

**Lovable Prompt**: "Create a Settings page with three clean sections: Account (Canvas connection), Display (default view, course colors), and Sync (last sync time, manual sync button). Simple form layout, left-aligned labels, right-aligned controls."

### Phase 5: Backend Integration (NEXT PHASE) 🚀

**Goal**: Replace ALL mock data with Canvas API while preserving frontend functionality.

**Reference Implementation**: `~/.claude/direct-access-tools/canvas/` (working Canvas API client)

#### Step 1: Export & Environment Setup
17. [ ] Export Lovable project to local GitHub repository
   - Download full codebase from Lovable.dev
   - Initialize git repository if needed
   - Verify build works locally (`npm run dev`)
   - Document environment requirements

18. [ ] Set up development environment
   - Node.js + npm/yarn
   - Environment variables (`.env` file)
   - Canvas API credentials (developer key + secret)
   - Local database (PostgreSQL for caching, optional Redis)

#### Step 2: Canvas OAuth2 Setup
19. [ ] Create Canvas Developer Application
   - Log into Canvas as admin/developer
   - Navigate to Account → Developer Keys
   - Create new OAuth2 key for Canvas Wrapper
   - Configure redirect URI (e.g., `http://localhost:3000/auth/callback`)
   - Note Client ID and Client Secret
   - **Required Scopes**:
     - `url:GET|/api/v1/courses`
     - `url:GET|/api/v1/courses/:course_id/assignments`
     - `url:GET|/api/v1/courses/:course_id/files`
     - `url:GET|/api/v1/users/self/todo`
     - `url:GET|/api/v1/users/:user_id/courses`

20. [ ] Implement OAuth2 Flow
   - Create `/api/auth/canvas` endpoint (initiates OAuth)
   - Create `/api/auth/callback` endpoint (receives code, exchanges for token)
   - Secure token storage (encrypted, httpOnly cookies or secure session)
   - Token refresh logic (Canvas tokens expire)
   - Multi-institution support (Canvas URL as parameter)

#### Step 3: Canvas API Integration Layer
21. [ ] Build Canvas API Client (`src/lib/canvas-api.ts`)
   - Base API client with authentication
   - Error handling and retry logic
   - Rate limiting (Canvas API limits: ~3000 requests/hour)
   - Response caching (reduce API calls)
   - **Reference**: Mirror structure from `~/.claude/direct-access-tools/canvas/`

22. [ ] Implement Data Fetching Functions
   - `getCourses()` - Replace `mockCourses`
   - `getAssignments(courseId?)` - Replace `mockAssignments`
   - `getAssignmentDetails(assignmentId)` - Full assignment data
   - `getFiles(courseId?)` - Replace `mockFiles`
   - `getSubmissionStatus(assignmentId)` - Get real submission state
   - `getUserInfo()` - For Settings page
   - Link extraction from HTML descriptions (parse `assignment.description`)

#### Step 4: Replace Mock Data (Page by Page)
23. [ ] **Dashboard** (`src/pages/Dashboard.tsx`)
   - Replace hardcoded `todayAssignments`, `thisWeekAssignments`, `allAssignments`
   - Use `getAssignments()` filtered by due date
   - Add loading state (skeleton rows)
   - Handle empty state ("No assignments due today")
   - Real submission status from API

24. [ ] **Courses** (`src/pages/Courses.tsx`, `src/pages/CourseDetail.tsx`)
   - Replace `mockCourseDetails` with `getCourses()`
   - Fetch course-specific assignments with `getAssignments(courseId)`
   - Real instructor info, announcements
   - Course color persistence (localStorage + user preferences)

25. [ ] **Search** (`src/pages/Search.tsx`)
   - Build search index from API data
   - Option 1: Client-side search (filter all fetched data)
   - Option 2: Server-side search endpoint (better for scale)
   - Real-time results with loading state
   - Maintain filter functionality

26. [ ] **Files** (`src/pages/Files.tsx`)
   - Replace `mockFiles` and `mockFolderTree`
   - Fetch files with `getFiles(courseId)`
   - Build folder hierarchy from Canvas file structure
   - Real file downloads (proxy through Canvas API or direct links)
   - Handle Canvas file permissions

27. [ ] **Calendar** (`src/pages/Calendar.tsx`)
   - Use real assignment due dates from `getAssignments()`
   - Group by date using actual Canvas data
   - Real course colors
   - Update `parseAssignmentDate()` for Canvas date formats (ISO 8601)

28. [ ] **Settings** (`src/pages/Settings.tsx`)
   - Replace mock user data with `getUserInfo()`
   - Real institution name from Canvas
   - "Disconnect" actually clears tokens
   - "Sync Now" triggers fresh API calls, clears cache

29. [ ] **Assignment Modal** (`src/components/AssignmentDetailModal.tsx`)
   - Fetch full assignment details on open (if not already cached)
   - Parse HTML description for embedded links
   - Real submission status and timestamp
   - "Open in Canvas" uses real `assignment.html_url`

#### Step 5: Data Caching & Sync
30. [ ] Implement Caching Layer
   - localStorage for offline access (assignments, courses)
   - Cache expiration (e.g., 15 minutes)
   - Background refresh (update cache without blocking UI)
   - "Last synced" timestamp in Settings

31. [ ] Sync Strategy
   - Initial load: Fetch all courses + assignments
   - Periodic refresh: Every 15-30 minutes (user preference)
   - Manual sync: "Sync Now" button
   - Incremental updates: Only fetch changed data (use `updated_at` params)

#### Step 6: Production Readiness
32. [ ] Error Handling & Edge Cases
   - Network failures: Show cached data + toast
   - API rate limiting: Queue requests, show warning
   - Invalid tokens: Redirect to login
   - Missing data: Graceful fallbacks

33. [ ] Testing with Real Data
   - Test with actual HBS Canvas account
   - Verify all assignment types render correctly
   - Test file downloads across different types
   - Validate submission status accuracy
   - Check performance with real course load (5-7 courses)

34. [ ] Deployment
   - Choose hosting (Vercel/Netlify/Railway)
   - Set up production Canvas OAuth app
   - Environment variables for prod
   - SSL certificates
   - Monitoring & error tracking (Sentry)

---

**Key Technical Decisions**:

1. **Canvas Instance URL**: User provides on login (e.g., `canvas.harvard.edu`)
2. **Token Storage**: Secure httpOnly cookies or encrypted session storage
3. **Caching**: localStorage (client) + Redis (server, optional)
4. **Link Extraction**: Regex/parser for HTML descriptions to find embedded URLs
5. **File Downloads**: Proxy through app or direct Canvas links with auth token
6. **Sync Frequency**: User preference (15min/30min/1hr) or manual only

**Reference Implementation**:
- Your working Canvas API client: `~/.claude/direct-access-tools/canvas/canvas_api.py`
- Study authentication, request patterns, error handling
- Translate Python logic to TypeScript/JavaScript

**Estimated Timeline**:
- Steps 17-20 (Setup + OAuth): 2-3 days
- Steps 21-22 (API Client): 2-3 days
- Steps 23-29 (Replace Mock Data): 4-5 days
- Steps 30-34 (Caching + Production): 2-3 days
- **Total**: 10-14 days of focused development

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
