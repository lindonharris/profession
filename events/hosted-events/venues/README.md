# Venue Database Guide

## System Architecture

### Integrated System with Auto-Updating Map

**1. Venue Markdown Files** - Complete YAML frontmatter with all venue data
**2. Rolodex JSON** - Single source of truth synced from markdown files
**3. Interactive Map** - Auto-generated from rolodex.json
**4. Email Threads** - Track correspondence per venue

All linked via `venue_id`

## Quick Start: Adding a New Venue

1. **Create venue folder**: `mkdir venues/[City-VenueName]/`
2. **Create venue file**: `[City-VenueName]/[City-VenueName].md` (YAML-only format)
3. **Add to rolodex**: Update `rolodex.json` with venue data and coordinates
4. **Regenerate map**: Run `./UPDATE-MAP.sh` to auto-update venue-map.html
5. **Create email thread**: `[City-VenueName]/email-thread.md`

### Auto-Updating Map

The map automatically displays all venues from `rolodex.json`:
- **To update map**: Run `./UPDATE-MAP.sh` (automatically regenerates from rolodex.json)
- **Map reads from**: `rolodex.json` (single source of truth)
- **Map shows**: Orange markers with hover tooltips for all venues with coordinates
- **Map location**: `venue-map.html` (open in any browser)
- **Auto-sync script**: `~/.claude/direct-access-tools/venues/sync-rolodex.py`

**Programmatic updates**: When modifying rolodex.json via Python scripts, use the auto-update wrapper:
```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path.home() / '.claude/direct-access-tools/venues'))
from auto_update_wrapper import update_rolodex_and_sync

def add_new_venue(rolodex):
    rolodex['venues'].append(new_venue_dict)
    rolodex['total_venues'] = len(rolodex['venues'])
    return rolodex

update_rolodex_and_sync('path/to/rolodex.json', add_new_venue)
# Map automatically regenerates after rolodex is updated
```

---

## Frontmatter Schema (Verified-Only)

**Philosophy**: Only include data verified from research - no AI guesses, no subjective ratings.

```yaml
---
# Core Identifiers
venue_id: "Boston-BSMNT"                    # MUST match filename
venue_name: "BSMNT (Basement)"
rolodex_synced: true

# Location (from address)
city: "Boston"
state: "MA"
neighborhood: "Theater District"
zip_code: "02116"

# Venue Classification (only if explicitly stated)
venue_type: "nightclub"                     # nightclub, live-music, ballroom, resto-lounge, irish-pub, multi-purpose
venue_style: ["electronic", "house", "hip-hop"]  # Genres mentioned on website

# Capacity (only if explicitly stated)
capacity_min: 500
capacity_max: 600

# Management (only if confirmed)
management_group: "Big Night Entertainment Group"

# Operating Info (only if explicitly stated)
age_requirement: "21+"                      # 18+, 21+, all-ages, or null

# Metadata
date_added: "2025-10-06"
last_updated: "2025-10-07"

# Tags
tags: [venue, boston, nightclub, theater-district, electronic]
---
```

### What Goes Where

#### ✅ Frontmatter (if explicitly verified)
- Location: city, state, neighborhood, zip_code
- Type: venue_type, venue_style
- Capacity: capacity_min, capacity_max (if stated)
- Management: management_group (if confirmed)
- Age: age_requirement (if stated)
- Dates: date_added, last_updated
- Tags: for Obsidian search

#### ✅ Rolodex (rolodex.json)
- venue_id, venue_name, city
- contacts.primary_phone
- contacts.email.email_list (semicolon-separated)
- contacts.website
- contacts.social_media.*

#### ✅ Body Sections (narrative)
- Layout descriptions
- Atmosphere (subjective)
- Services details
- Operating schedules
- Dress code descriptions
- Pricing notes
- Reviews and reputation
- Event history
- Personal notes

### Use `null` for Unknown Fields
Don't guess - use `null` if data isn't explicitly stated.

---

## Query Examples (Obsidian Dataview)

### Find Nightclubs in Theater District
```dataview
TABLE venue_name AS "Venue", capacity_max AS "Capacity"
FROM "logistics/events/venues"
WHERE venue_type = "nightclub"
AND neighborhood = "Theater District"
SORT capacity_max DESC
```

### All Big Night Entertainment Venues
```dataview
TABLE venue_name AS "Venue", neighborhood AS "Location", capacity_max AS "Max"
FROM "logistics/events/venues"
WHERE management_group = "Big Night Entertainment Group"
SORT capacity_max DESC
```

### Electronic Music Venues 500+ Capacity
```dataview
TABLE venue_name AS "Venue", capacity_max AS "Max", neighborhood AS "Hood"
FROM "logistics/events/venues"
WHERE contains(venue_style, "electronic")
AND capacity_max >= 500
SORT capacity_max ASC
```

### Venues by City and Neighborhood
```dataview
TABLE venue_name AS "Venue", venue_type AS "Type", capacity_max AS "Max"
FROM "logistics/events/venues"
WHERE city = "Boston"
GROUP BY neighborhood
SORT neighborhood, venue_name
```

### Find Venues with Specific Capacity Range
```dataview
TABLE venue_name AS "Venue", capacity_max AS "Capacity", neighborhood
FROM "logistics/events/venues"
WHERE capacity_max >= 400 AND capacity_max <= 700
SORT capacity_max ASC
```

### All Venues by Management Group
```dataview
TABLE rows.file.link AS "Venues", length(rows) AS "Count"
FROM "logistics/events/venues"
WHERE management_group != null AND management_group != "TBD"
GROUP BY management_group
SORT length(rows) DESC
```

### Venues by Venue Type
```dataview
TABLE rows.file.link AS "Venues"
FROM "logistics/events/venues"
WHERE venue_type != null
GROUP BY venue_type
```

### Cambridge/Somerville Venues Only
```dataview
TABLE venue_name AS "Venue", neighborhood, capacity_max AS "Max"
FROM "logistics/events/venues"
WHERE city = "Cambridge" OR city = "Somerville"
SORT city, venue_name
```

---

## Rolodex Structure

**File**: `rolodex.json`
**Purpose**: Single source of truth for contact information

### JSON Schema
```json
{
  "venue_id": "Boston-BSMNT",
  "venue_name": "BSMNT (Basement)",
  "city": "Boston",
  "contacts": {
    "primary_phone": "(617) 778-0089",
    "email": {
      "email_list": "info@bsmntboston.com; events@bsmntboston.com; vip@bsmntboston.com",
      "general": "info@bsmntboston.com",
      "events_private_bookings": "events@bsmntboston.com"
    },
    "website": "https://www.bsmntboston.com",
    "social_media": {
      "instagram": "@bsmntboston",
      "facebook": "facebook.com/bsmntboston"
    }
  },
  "metadata": {
    "synced_from": "Boston-BSMNT.md",
    "last_verified": "2025-10-07",
    "status": "active"
  }
}
```

### Current Stats
- **18 venues** total
- **29 unique email addresses**
- **100% sync** with markdown files

---

## Rules & Best Practices

### DO
✅ Only populate frontmatter with verified facts
✅ Use `null` for unknown/unverified fields
✅ Keep rolodex as single source for contacts
✅ Put subjective assessments in body text
✅ Link everything via `venue_id`

### DON'T
❌ Guess or estimate frontmatter values
❌ Duplicate contact info in multiple places
❌ Put narrative descriptions in frontmatter
❌ Use subjective ratings in frontmatter
❌ Include "TBD" in arrays (use empty array or null)

---

## Example: Right vs Wrong

### ❌ Wrong (Guessing in Frontmatter)
```yaml
price_tier: "premium"              # Subjective
sound_system_quality: "high"       # Subjective
has_vip_sections: true            # Not verified
operating_days: ["fri", "sat"]    # Guessing
```

### ✅ Right (Facts in Frontmatter, Details in Body)
```yaml
venue_type: "nightclub"           # Stated on website
capacity_max: 600                 # Explicitly stated
age_requirement: "21+"            # Stated on website
management_group: "Big Night Entertainment Group"  # Confirmed
```

**Put subjective/detailed info in body:**
```markdown
## Pricing & Booking
**Pricing**: Premium pricing - expect $15-20 cocktails,
$500+ bottle service minimums.

## Venue Specifications
**Technical Capabilities**: Professional sound system with
high-quality speakers. State-of-the-art lighting suitable
for major DJ performances.

**Operating Schedule**: Primarily Thursday-Saturday nights
```

---

## File Structure

```
venues/
├── _TEMPLATE.md               # Template for new venues
├── README.md                  # This guide
├── rolodex.json              # Contact database
├── Boston-BSMNT.md           # Example venue (migrated)
├── Boston-BigNightLive.md    # Venue files...
├── [17 more venue files]
└── ...
```

---

## Current Status

- ✅ Schema designed (verified-only, 16 fields)
- ✅ Template updated
- ✅ Boston-BSMNT migrated (example)
- ✅ Rolodex complete (18 venues, 29 emails)
- ⏳ Pending: Migrate remaining 17 venues to new frontmatter

---

## Benefits

1. **100% Accurate**: No AI guesses in structured fields
2. **Clear Boundaries**: Each system has distinct purpose
3. **No Duplication**: venue_id links everything
4. **Maintainable**: Facts change less than opinions
5. **Queryable**: Powerful filtering on verified facts
6. **Flexible**: Body text handles nuance
