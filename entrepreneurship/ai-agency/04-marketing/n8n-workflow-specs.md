# n8n Social Media Agent - Technical Workflow Specifications

**Last Updated:** October 7, 2025
**Workflow Name:** `buyanagent_social_flywheel`
**Status:** Design Phase
**Complexity:** Moderate (7-day build)

---

## Workflow Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                   CONTENT STRATEGY LAYER                    │
│  Airtable DB → Content Rotation Logic → GPT-4 Generation   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   HUMAN REVIEW GATE (OPTIONAL)              │
│        Slack Approval → Edit Modal → Bypass Logic           │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   MULTI-PLATFORM PUBLISHING                 │
│     LinkedIn API → Twitter API → Threads API (manual)       │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   ENGAGEMENT MONITORING                     │
│   Webhooks + Polling → Response Agent → Analytics Store    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   PERFORMANCE ANALYSIS                      │
│   Weekly GPT-4 Report → Strategy Iteration → Airtable Update│
└─────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Content Strategy & Generation (Nodes 1-10)

### Node 1: Schedule Trigger (Cron)

**Node Type:** `Schedule Trigger`
**Purpose:** Initiates content generation workflow daily

**Configuration:**
```json
{
  "rule": {
    "cronExpression": "0 6 * * 1-5",
    "timezone": "America/New_York"
  }
}
```

**Explanation:**
- Runs 6:00 AM EST, Monday-Friday
- Generates 1 post per platform (3 total daily)
- Weekends: Manual/curated content only

---

### Node 2: Airtable - Fetch Content Strategy

**Node Type:** `Airtable`
**Purpose:** Pull content ideas and rotation strategy

**Configuration:**
```json
{
  "operation": "list",
  "application": "buyanagent_content_db",
  "table": "Content_Ideas",
  "filterByFormula": "AND({Status} = 'Ready', {Last_Used} < DATEADD(TODAY(), -7, 'days'))",
  "maxRecords": 10,
  "sort": [
    {
      "field": "Priority_Score",
      "direction": "desc"
    }
  ]
}
```

**Output Fields:**
- `Topic` - Content subject (e.g., "Invoice automation ROI")
- `Platform` - Target platform (LinkedIn/Twitter/Threads)
- `Content_Pillar` - Which pillar (1-5)
- `Format` - Thread/Single Post/Case Study
- `Customer_Win_ID` - Link to customer data (if applicable)

---

### Node 3: Content Pillar Rotation Logic

**Node Type:** `Function`
**Purpose:** Ensure balanced content mix across 5 pillars

**JavaScript Code:**
```javascript
// Get content ideas from previous node
const contentIdeas = $input.all();

// Define pillar distribution (weekly targets)
const pillarTargets = {
  'Automation Wins': 0.30,        // 30% of content
  'Anti-Bloat Philosophy': 0.20,  // 20%
  'Founder Transparency': 0.20,   // 20%
  'AI Practicality': 0.20,        // 20%
  'Small Business Empowerment': 0.10  // 10%
};

// Get current week's published posts (from tracking table)
const publishedThisWeek = $('Airtable_Published').all();

// Calculate current distribution
const currentDistribution = {};
publishedThisWeek.forEach(post => {
  const pillar = post.json.Content_Pillar;
  currentDistribution[pillar] = (currentDistribution[pillar] || 0) + 1;
});

// Find most underrepresented pillar
let targetPillar = null;
let maxGap = 0;

Object.keys(pillarTargets).forEach(pillar => {
  const target = pillarTargets[pillar] * publishedThisWeek.length;
  const current = currentDistribution[pillar] || 0;
  const gap = target - current;

  if (gap > maxGap) {
    maxGap = gap;
    targetPillar = pillar;
  }
});

// Filter content ideas for target pillar
const selectedIdeas = contentIdeas.filter(idea =>
  idea.json.Content_Pillar === targetPillar
);

// Return top 3 ideas for this pillar
return selectedIdeas.slice(0, 3).map(idea => ({
  json: idea.json
}));
```

**Output:** 3 content ideas from underrepresented pillar

---

### Node 4: Platform Assignment Logic

**Node Type:** `Switch`
**Purpose:** Route to platform-specific generation based on today's schedule

**Routes:**
- **Route 1:** Monday/Wednesday/Friday → LinkedIn
- **Route 2:** Monday-Friday (all days) → Twitter (3-5 posts)
- **Route 3:** Tuesday/Thursday → Threads

**Configuration:**
```json
{
  "rules": {
    "rules": [
      {
        "operation": "regex",
        "value1": "={{ $now.format('ddd') }}",
        "value2": "Mon|Wed|Fri",
        "output": 0
      },
      {
        "operation": "equal",
        "value1": "=true",
        "output": 1
      },
      {
        "operation": "regex",
        "value1": "={{ $now.format('ddd') }}",
        "value2": "Tue|Thu",
        "output": 2
      }
    ]
  }
}
```

---

### Node 5a: LinkedIn Content Generator (GPT-4)

**Node Type:** `OpenAI`
**Purpose:** Generate LinkedIn-optimized content

**Configuration:**
```json
{
  "resource": "text",
  "model": "gpt-4-turbo-preview",
  "temperature": 0.7,
  "maxTokens": 1000,
  "messages": {
    "messages": [
      {
        "role": "system",
        "content": "You are Alex Automate, Chief Automation Officer at buyanagent.ai. Your voice is direct, anti-fluff, tactical. You share real metrics and call out bloated SaaS. You build in public."
      },
      {
        "role": "user",
        "content": "=Generate a LinkedIn post on: {{ $json.Topic }}\n\nContent Pillar: {{ $json.Content_Pillar }}\nFormat: {{ $json.Format }}\nCustomer Win (if any): {{ $json.Customer_Win_Data }}\n\nGuidelines:\n- Professional but not corporate\n- Lead with the insight, not setup\n- Use specific numbers/metrics\n- 3-7 post thread if complex topic\n- End with subtle CTA (not salesy)\n- Include 3-5 relevant hashtags\n\nOutput format:\n[Post Text]\n---\n[Hashtags]\n---\n[Image suggestion]"
      }
    ]
  }
}
```

**Output Example:**
```
Spent 4 hours/week chasing invoices. Now I spend 0.

Here's the 3-email escalation sequence that cut our DSO from 45 days to 28:

1. Day +3: Friendly reminder
"Hi [Name], just checking in on Invoice #123. Let me know if you need anything!"

2. Day +7: Professional follow-up
"Hi [Name], Invoice #123 is now 7 days overdue. Can you confirm payment timeline?"

3. Day +15: Firm but respectful
"Hi [Name], we haven't received payment for Invoice #123 (now 15 days overdue). Please settle by [date] to avoid service interruption."

The result? 37% faster payment cycles. Cash flow transformed.

Built this as an n8n agent. Live on buyanagent.ai for $100/mo.

No bloated accounting platform. Just invoice automation that works.
---
#Automation #CashFlow #SmallBusiness #AIAgents #Invoicing
---
Screenshot of DSO dashboard showing 45→28 day trend
```

---

### Node 5b: Twitter Content Generator (GPT-4)

**Node Type:** `OpenAI`
**Purpose:** Generate Twitter-optimized content (hot takes, threads, engagement bait)

**Configuration:** (Similar to 5a but with Twitter-specific prompt)

**Prompt Adjustments:**
- Max 280 characters per tweet
- Thread format: 3-5 tweets max
- Start with hook (controversial or curiosity-gap)
- Use line breaks for readability
- Engagement bait (polls, questions, replies)

**Output Example:**
```
SaaS is eating itself.

Why pay $500/mo for Salesforce when an AI agent scores leads better for $100?

Here's why standalone agents > bloated platforms 🧵

[Thread continues with 4 more tweets...]
---
#AI #SaaS #Automation
---
None (text-only thread)
```

---

### Node 5c: Threads Content Generator (GPT-4)

**Node Type:** `OpenAI`
**Purpose:** Generate Threads-optimized content (casual, behind-the-scenes)

**Prompt Adjustments:**
- Casual tone (more personal than LinkedIn)
- Visual-first (always suggest image)
- Shorter format (1-3 paragraphs max)
- Aspirational lifestyle messaging

**Output Example:**
```
Automated my expense tracking this week.

Never manually entering a receipt again.

The agent scans my Gmail, extracts vendor/amount/category with GPT-4, logs to Google Sheet.

68 receipts processed this month. I saw exactly zero of them.

This is what automation should feel like.

[Image: Google Sheet screenshot showing automated expense entries]
---
#Automation #SmallBusiness #Productivity
---
Google Sheet screenshot with highlighted automated entries
```

---

### Node 6: Airtable - Log Generated Content

**Node Type:** `Airtable`
**Purpose:** Store generated content for review/tracking

**Configuration:**
```json
{
  "operation": "create",
  "table": "Generated_Content",
  "fields": {
    "Topic": "={{ $json.Topic }}",
    "Platform": "={{ $json.Platform }}",
    "Post_Text": "={{ $('GPT4_Generator').item.json.choices[0].message.content }}",
    "Hashtags": "={{ $('GPT4_Generator').item.json.hashtags }}",
    "Image_Suggestion": "={{ $('GPT4_Generator').item.json.image_suggestion }}",
    "Status": "Pending_Review",
    "Generated_At": "={{ $now.toISO() }}"
  }
}
```

---

### Node 7: Slack - Send for Approval

**Node Type:** `Slack`
**Purpose:** Human review gate before publishing

**Configuration:**
```json
{
  "channel": "#social-review",
  "text": "New {{ $json.Platform }} post ready for review:",
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Topic:* {{ $json.Topic }}\n*Pillar:* {{ $json.Content_Pillar }}"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "{{ $json.Post_Text }}"
      }
    },
    {
      "type": "actions",
      "elements": [
        {
          "type": "button",
          "text": "✅ Approve",
          "style": "primary",
          "action_id": "approve_post",
          "value": "{{ $json.record_id }}"
        },
        {
          "type": "button",
          "text": "✏️ Edit",
          "action_id": "edit_post",
          "value": "{{ $json.record_id }}"
        },
        {
          "type": "button",
          "text": "🗑️ Reject",
          "style": "danger",
          "action_id": "reject_post",
          "value": "{{ $json.record_id }}"
        }
      ]
    }
  ]
}
```

---

### Node 8: Wait for Approval (Webhook)

**Node Type:** `Webhook` (listening for Slack button clicks)
**Purpose:** Pause workflow until human decision

**Configuration:**
```json
{
  "httpMethod": "POST",
  "path": "social-approval",
  "responseMode": "lastNode"
}
```

**Expected Payload:**
```json
{
  "action": "approve|edit|reject",
  "record_id": "rec123456",
  "edited_text": "..." // if action=edit
}
```

---

### Node 9: Approval Router

**Node Type:** `Switch`
**Purpose:** Route based on approval decision

**Routes:**
- **Approved** → Proceed to scheduling
- **Edited** → Update Airtable, proceed to scheduling
- **Rejected** → Log reason, end workflow

---

### Node 10: Airtable - Update Status

**Node Type:** `Airtable`
**Purpose:** Mark content as approved/edited/rejected

**Configuration:**
```json
{
  "operation": "update",
  "table": "Generated_Content",
  "id": "={{ $json.record_id }}",
  "fields": {
    "Status": "={{ $json.action === 'approve' ? 'Approved' : ($json.action === 'edit' ? 'Edited' : 'Rejected') }}",
    "Edited_Text": "={{ $json.edited_text || '' }}",
    "Reviewed_At": "={{ $now.toISO() }}"
  }
}
```

---

## Phase 1 Summary

**Nodes Built:** 10
**Capabilities:**
✅ Daily content generation (platform-optimized)
✅ Content pillar rotation (balanced mix)
✅ GPT-4 drafting (3 platform variants)
✅ Airtable storage (tracking/history)
✅ Slack approval gate (human oversight)

**What's Next:** Phase 2 - Multi-Platform Publishing (Nodes 11-20)

---

## Technical Dependencies

**n8n Cloud Requirements:**
- Plan: Pro ($50/month for 10K operations)
- Estimated operations/month: ~3,000 (well under limit)

**External Services:**
- **Airtable:** Free tier (1,200 records/base - sufficient)
- **OpenAI API:** GPT-4 Turbo (~$0.01/post × 100 posts/month = $1)
- **Slack:** Free tier (webhook integrations included)

**Total Phase 1 Cost:** $51/month

---

## Next Phase Preview

**Phase 2 will add:**
- LinkedIn API publishing (OAuth + post creation)
- Twitter API v2 integration (thread posting)
- Threads manual posting workflow (until API available)
- Optimal scheduling logic per platform
- UTM tracking for all links

**Estimated Phase 2 Build Time:** 3 days
