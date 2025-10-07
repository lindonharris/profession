# Application Tracking System

## Overview
This directory manages job application materials and tracking for recruiting efforts. It serves as the central hub for organizing application documents, templates, and outreach communications.

## Directory Structure

```
applications/
├── jds/           # Job descriptions for positions being pursued
├── outbounds/     # Outreach communications and application submissions
├── templates/     # Reusable templates for cover letters, emails, etc.
├── tracker.md     # Main tracking document for application status
└── README.md      # This file
```

## Key Files & Directories

### tracker.md
Central tracking document containing:
- Application status for each position
- Key dates (applied, interviews, decisions)
- Contact information
- Next steps and follow-ups

### jds/
Repository of job descriptions:
- Original postings saved for reference
- Annotated versions with key requirements highlighted
- Company-specific requirements and preferences

### outbounds/
Application materials sent to companies:
- Cover letters (organized by company/date)
- Tailored resumes
- Follow-up correspondence
- Thank you notes

### templates/
Reusable document templates:
- Base resume versions
- Cover letter frameworks
- Email templates (introduction, follow-up, thank you)
- Response templates for common scenarios

## Common Tasks

### Adding a New Application
1. Save JD to `jds/[Company]_[Position]_[Date].md`
2. Create tailored materials in `outbounds/[Company]/`
3. Update `tracker.md` with application details
4. Set follow-up reminders

### Checking Application Status
- Review `tracker.md` for current status
- Check `outbounds/[Company]/` for communication history
- Reference original JD in `jds/` for requirements

### Preparing for Interviews
1. Review JD in `jds/` directory
2. Check all correspondence in `outbounds/[Company]/`
3. Update tracker.md with interview details
4. Prepare questions/notes in company-specific folder

## File Naming Conventions

- JDs: `[Company]_[Position]_[YYYY-MM-DD].md`
- Cover Letters: `[Company]_CL_[YYYY-MM-DD].md`
- Resumes: `[Company]_Resume_[Version].pdf`
- Follow-ups: `[Company]_Followup_[YYYY-MM-DD].md`

## Status Codes (used in tracker.md)
- **PREP** - Preparing application
- **SENT** - Application submitted
- **ACK** - Acknowledged receipt
- **SCREEN** - Phone/initial screening scheduled
- **INT** - Interview scheduled
- **PEND** - Awaiting decision
- **REJ** - Rejected
- **OFFER** - Offer received
- **ACC** - Accepted
- **DEC** - Declined

## Integration Notes

### Related Directories
- `../firms/` - Detailed company research and insights
- `../contacts/` - Networking contacts and referrals
- `../professional-identity/` - Personal branding materials
- `../case-studies/` - Interview preparation materials

### Workflow Tips
1. Always update tracker.md immediately after any action
2. Keep copies of all submitted materials in outbounds/
3. Document all interactions (emails, calls, meetings)
4. Cross-reference with firms/ for company research
5. Link relevant contacts from ../contacts/ directory

## Quick Commands

```bash
# View current applications
cat tracker.md

# Find all applications to a company
find . -name "*CompanyName*"

# List recent submissions
ls -lt outbounds/

# Search for specific positions
grep -r "position_title" jds/
```

## Best Practices
- Maintain consistent naming across all files
- Update tracker.md in real-time
- Archive completed applications (accepted/rejected) after 6 months
- Keep templates generic and customizable
- Document lessons learned from each application cycle

---
*Last Updated: September 2024*