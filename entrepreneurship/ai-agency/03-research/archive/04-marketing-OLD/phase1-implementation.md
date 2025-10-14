# Phase 1 Implementation Checklist - Social Media Flywheel

**Timeline:** 7 days (assumes 2-3 hours/day founder time)
**Goal:** Launch automated content generation + publishing for 1 platform (LinkedIn)
**Success Criteria:** 5 AI-generated posts published, 1 manual approval workflow working

---

## Pre-Launch Preparation (Day 0)

### Strategic Decisions

- [ ] **Choose anonymous persona name**
  - Options: "Alex Automate", "The Agent Builder", "Sam Standalone", custom
  - Decision: _______________

- [ ] **Select LinkedIn profile photo**
  - AI-generated avatar (Midjourney/DALL-E)
  - Stock photo (professional headshot)
  - Abstract logo/icon
  - Decision: _______________

- [ ] **Finalize brand voice guidelines**
  - Review 10 example posts in `/inbound-social-flywheel.md`
  - Write 3 "Do" and 3 "Don't" rules specific to your voice
  - Save to Airtable "Voice Guidelines" table

---

## Day 1: Infrastructure Setup

### n8n Cloud Account

- [ ] **Sign up for n8n Cloud** (https://n8n.io)
  - Plan: Pro ($50/month - 10K operations)
  - Payment method added
  - Email confirmation completed

- [ ] **Create first workflow**
  - Name: `buyanagent_social_flywheel_v1`
  - Tags: `marketing`, `social`, `linkedin`

### Airtable Database

- [ ] **Create Airtable account** (free tier sufficient)

- [ ] **Create base: "BuyAnAgent Social Strategy"**

- [ ] **Create tables:**

**Table 1: Content_Ideas**
```
Fields:
- Topic (single line text)
- Platform (single select: LinkedIn, Twitter, Threads, All)
- Content_Pillar (single select: Automation Wins, Anti-Bloat, Transparency, AI Practicality, Empowerment)
- Format (single select: Thread, Single Post, Case Study, Hot Take)
- Customer_Win_ID (link to Customer_Wins table)
- Priority_Score (number, 1-10)
- Status (single select: Idea, Ready, Used, Archived)
- Last_Used (date)
- Notes (long text)
```

**Table 2: Customer_Wins**
```
Fields:
- Customer_Name (single line text, anonymized)
- Agent_Used (single select: Invoice Chaser, Lead Qualification, Expense Manager, etc.)
- Metric_Before (single line text, e.g., "DSO 45 days")
- Metric_After (single line text, e.g., "DSO 28 days")
- Improvement_Percentage (number)
- Testimonial_Quote (long text)
- Approval_Status (single select: Pending, Approved, Denied)
- Approval_Date (date)
```

**Table 3: Generated_Content**
```
Fields:
- Post_ID (autonumber)
- Topic (single line text)
- Platform (single select)
- Content_Pillar (single select)
- Post_Text (long text)
- Hashtags (single line text)
- Image_Suggestion (long text)
- Status (single select: Pending_Review, Approved, Edited, Rejected, Published)
- Generated_At (date)
- Reviewed_At (date)
- Published_At (date)
- Edited_Text (long text)
```

**Table 4: Published_Content**
```
Fields:
- Post_ID (link to Generated_Content)
- Platform (single select)
- Published_Date (date)
- Post_URL (URL)
- Impressions (number)
- Engagement_Count (number)
- Engagement_Rate (formula: Engagement_Count / Impressions)
- Clicks (number)
- CTR (formula: Clicks / Impressions)
- Signups_Attributed (number)
- MRR_Attributed (currency)
- Performance_Tier (formula: based on engagement_rate)
```

- [ ] **Populate 10 initial content ideas**
  - 3 Automation Wins (use existing customer data or create hypothetical)
  - 2 Anti-Bloat (competitor analysis from `/competitive-analysis.md`)
  - 2 Transparency (founder journey, build progress)
  - 2 AI Practicality (how agents work, prompt examples)
  - 1 Empowerment (small business wins)

### Slack Workspace

- [ ] **Create Slack channel: `#social-review`**
  - Purpose: Content approval workflow
  - Members: Founder only (for now)

- [ ] **Create Slack channel: `#social-analytics`**
  - Purpose: Automated performance reports
  - Members: Founder + future marketing contractor

---

## Day 2: n8n Workflow - Content Generation (Nodes 1-6)

### Node 1: Schedule Trigger

- [ ] **Add "Schedule Trigger" node**
  - Cron expression: `0 6 * * 1-5` (6am weekdays)
  - Timezone: America/New_York
  - Test: Click "Execute Node" to verify trigger works

### Node 2: Airtable - Fetch Content Ideas

- [ ] **Add "Airtable" node**
  - Operation: List
  - Connect Airtable account (OAuth)
  - Base: BuyAnAgent Social Strategy
  - Table: Content_Ideas
  - Filter: `AND({Status} = 'Ready', {Platform} = 'LinkedIn')`
  - Sort: Priority_Score (descending)
  - Max records: 10
  - Test: Execute node, verify 10 ideas returned

### Node 3: Function - Content Pillar Rotation

- [ ] **Add "Function" node**
  - Copy JavaScript code from `/n8n-workflow-specs.md` (Node 3)
  - Requires: Second Airtable node to fetch published content (add before this node)
  - Test: Execute, verify 3 ideas from underrepresented pillar returned

**Substep: Add Airtable "Published This Week" node**
- [ ] Operation: List
- [ ] Table: Published_Content
- [ ] Filter: `{Published_Date} >= DATEADD(TODAY(), -7, 'days')`
- [ ] Test: Execute (will be empty initially)

### Node 4: LinkedIn Content Generator (GPT-4)

- [ ] **Sign up for OpenAI API** (https://platform.openai.com)
  - Add payment method
  - Generate API key
  - Save to password manager

- [ ] **Add "OpenAI" node to n8n**
  - Connect OpenAI credentials
  - Model: gpt-4-turbo-preview
  - Temperature: 0.7
  - Max tokens: 1000
  - System message: Copy from `/n8n-workflow-specs.md` (Node 5a)
  - User message: Include Topic, Pillar, Format, Customer_Win_Data from previous node
  - Test: Execute with sample content idea

- [ ] **Validate GPT-4 output format**
  - Contains post text
  - Contains hashtags
  - Contains image suggestion
  - Tone matches brand voice

### Node 5: Airtable - Log Generated Content

- [ ] **Add "Airtable" node**
  - Operation: Create
  - Table: Generated_Content
  - Fields mapping:
    - Topic → `{{ $json.Topic }}`
    - Platform → `LinkedIn`
    - Content_Pillar → `{{ $json.Content_Pillar }}`
    - Post_Text → `{{ $('OpenAI').item.json.choices[0].message.content }}`
    - Status → `Pending_Review`
    - Generated_At → `{{ $now.toISO() }}`
  - Test: Execute, verify record created in Airtable

### Node 6: Slack - Send for Approval

- [ ] **Add "Slack" node**
  - Operation: Send Message
  - Connect Slack workspace
  - Channel: #social-review
  - Message: Copy template from `/n8n-workflow-specs.md` (Node 7)
  - Include interactive buttons:
    - ✅ Approve (action_id: `approve_post`)
    - ✏️ Edit (action_id: `edit_post`)
    - 🗑️ Reject (action_id: `reject_post`)
  - Test: Execute, verify message appears in Slack

**Note:** Interactive buttons require Slack app setup (next step)

---

## Day 3: Slack Interactive Approvals

### Slack App Setup

- [ ] **Create Slack App** (https://api.slack.com/apps)
  - Name: "Social Review Bot"
  - Workspace: Your workspace
  - Features: Interactive Components enabled

- [ ] **Configure Interactive Components**
  - Request URL: `https://YOUR_N8N_INSTANCE.app.n8n.cloud/webhook/social-approval`
  - (Will generate this URL in next step)

- [ ] **Add Bot Scopes**
  - `chat:write` (send messages)
  - `channels:read` (read channel info)
  - Install app to workspace

### n8n Approval Webhook

- [ ] **Add "Webhook" node** (new workflow branch)
  - HTTP Method: POST
  - Path: `social-approval`
  - Response Mode: Last Node
  - Copy webhook URL
  - Paste into Slack App "Request URL"

- [ ] **Add "Function" node** (parse Slack payload)
```javascript
// Extract action and record_id from Slack payload
const payload = JSON.parse($input.item.json.body.payload);

return {
  json: {
    action: payload.actions[0].action_id.replace('_post', ''),
    record_id: payload.actions[0].value,
    user_id: payload.user.id
  }
};
```

- [ ] **Test Slack button click**
  - Click "Approve" button in #social-review
  - Verify webhook receives payload in n8n

### Approval Router

- [ ] **Add "Switch" node**
  - Routes:
    - Route 1: `{{ $json.action }} === 'approve'` → Proceed to publishing
    - Route 2: `{{ $json.action }} === 'edit'` → Open edit modal (future)
    - Route 3: `{{ $json.action }} === 'reject'` → Log and end

- [ ] **For "Approve" route:**
  - Add Airtable "Update" node
  - Table: Generated_Content
  - ID: `{{ $json.record_id }}`
  - Fields: `Status = 'Approved'`, `Reviewed_At = NOW()`

- [ ] **For "Reject" route:**
  - Add Airtable "Update" node
  - Fields: `Status = 'Rejected'`, `Reviewed_At = NOW()`
  - End workflow

---

## Day 4: LinkedIn API Integration

### LinkedIn Developer Account

- [ ] **Create LinkedIn Developer account** (https://www.linkedin.com/developers/)
  - Agree to API Terms of Service

- [ ] **Create LinkedIn App**
  - App name: "BuyAnAgent Social Manager"
  - LinkedIn Page: Create company page for "buyanagent.ai" first (if not exists)
  - App logo: Use brand logo
  - Privacy policy URL: `https://buyanagent.ai/privacy` (create basic page)

- [ ] **Request API Access**
  - Products: "Share on LinkedIn" + "Marketing Developer Platform"
  - Use case: "Automated social media posting for brand account"
  - Wait for approval (usually 24-48 hours)

**⚠️ Blocker:** LinkedIn API approval may take 1-2 days. Continue with Day 5-6 while waiting.

### OAuth Setup (Once Approved)

- [ ] **Configure OAuth 2.0**
  - Authorized redirect URLs: `https://YOUR_N8N_INSTANCE.app.n8n.cloud/oauth/callback`
  - Copy Client ID and Client Secret

- [ ] **Connect LinkedIn in n8n**
  - Add LinkedIn credentials
  - OAuth flow: Authorize app to post on behalf of page

---

## Day 5: Publishing Workflow (Manual Alternative)

**While waiting for LinkedIn API approval, build manual publishing workflow:**

### Manual Publishing Bridge

- [ ] **Add "Slack" node** (after approval)
  - Channel: #social-review
  - Message:
```
📝 *APPROVED POST - READY TO PUBLISH*

Platform: LinkedIn
Pillar: {{ $json.Content_Pillar }}

--- POST TEXT ---
{{ $json.Post_Text }}
---

📋 MANUAL STEPS:
1. Copy text above
2. Go to LinkedIn (https://linkedin.com)
3. Create new post, paste text
4. Add hashtags: {{ $json.Hashtags }}
5. Publish post
6. Click ✅ below when published
```

- [ ] **Add interactive button:**
  - "✅ Published" → Updates Airtable with Published_At timestamp

**This manual bridge lets you start posting while API approval pending.**

---

## Day 6: Testing & Dry Run

### End-to-End Test

- [ ] **Manually trigger workflow**
  - n8n workflow: Click "Execute Workflow"
  - Verify each node executes successfully

- [ ] **Check Airtable logs**
  - Generated_Content table: 1 new record with status "Pending_Review"

- [ ] **Check Slack approval**
  - Message appears in #social-review
  - Buttons work (click Approve)

- [ ] **Check manual publishing prompt**
  - Slack shows formatted post text
  - Copy/paste to LinkedIn works

- [ ] **Update Airtable manually**
  - Mark post as "Published"
  - Add Published_Date
  - Add Post_URL

### Create 5 Test Posts

- [ ] **Generate 5 posts over 5 days** (one per day)
  - Monday: Automation Win (customer case study)
  - Tuesday: AI Practicality (how it works)
  - Wednesday: Transparency (build update)
  - Thursday: Anti-Bloat (competitor critique)
  - Friday: Automation Win (metric-heavy thread)

- [ ] **Track performance manually**
  - After 24 hours: Record impressions, engagement from LinkedIn analytics
  - Add to Published_Content table in Airtable

---

## Day 7: Launch & Monitor

### Official Launch

- [ ] **Switch to daily automated triggers**
  - Change cron from manual to `0 6 * * 1-5`
  - Workflow now generates content every weekday 6am

- [ ] **Set up monitoring**
  - Slack alerts: Workflow failures
  - Email digest: Weekly performance summary (manual for now)

### First Week Goals

- [ ] **Publish 5 LinkedIn posts** (1 per weekday)
- [ ] **Achieve 3% avg engagement rate** (LinkedIn organic avg: 1-2%)
- [ ] **Generate 50+ website clicks** (10 clicks/post avg)
- [ ] **Gain 50+ new LinkedIn followers**

### Daily Routine (Founder)

**Morning (15 min):**
- [ ] Check #social-review channel
- [ ] Review AI-generated post
- [ ] Approve/edit/reject (one click)

**Evening (10 min):**
- [ ] Check LinkedIn analytics for today's post
- [ ] Update Airtable with engagement numbers
- [ ] Reply to comments (2-5 per day expected)

---

## Phase 1 Success Criteria

### ✅ Launch is successful if:

1. **Workflow runs daily without manual intervention**
   - No broken nodes
   - Content generated every weekday 6am
   - Approval notifications arrive in Slack

2. **Content quality is high**
   - 80%+ posts approved without edits
   - Brand voice consistent
   - Zero major factual errors

3. **Engagement beats LinkedIn organic average**
   - >2% engagement rate (LinkedIn avg: 1-2%)
   - >10 clicks per post
   - >3 comments per post

4. **Founder time investment sustainable**
   - <30 min/day on social media
   - No burnout from manual work
   - Clear ROI on time spent

### ⚠️ Pivot if:

- Engagement <1% for 2 consecutive weeks
- Founder spending >1 hour/day on approvals/edits
- GPT-4 quality degrading (>50% posts need major edits)
- Zero website traffic from LinkedIn after 2 weeks

---

## Phase 2 Preview (Weeks 2-4)

**Once LinkedIn working smoothly:**

- [ ] Add Twitter/X integration (same workflow, different platform)
- [ ] Add Threads integration (manual initially, API later)
- [ ] Build engagement monitoring (scrape LinkedIn analytics via n8n)
- [ ] Add GPT-4 response agent (auto-reply to comments)
- [ ] Create weekly performance dashboard (Retool or Airtable Interface)

**Goal:** 3-platform automated posting by end of Month 1

---

## Resources & Links

**Documentation:**
- n8n workflow specs: `/04-marketing/n8n-workflow-specs.md`
- Content pillar framework: `/04-marketing/content-pillar-framework.md`
- Measurement dashboard: `/04-marketing/measurement-dashboard.md`
- Overall strategy: `/04-marketing/inbound-social-flywheel.md`

**Tools:**
- n8n Cloud: https://app.n8n.cloud
- Airtable: https://airtable.com
- OpenAI API: https://platform.openai.com
- LinkedIn Developers: https://www.linkedin.com/developers/

**Support:**
- n8n Community: https://community.n8n.io
- n8n Documentation: https://docs.n8n.io

---

## Daily Checklist Template (Print This)

**Day X: _______________**

Morning:
- [ ] Check #social-review (1 new post)
- [ ] Review & approve/edit (5 min)
- [ ] Manual publish to LinkedIn (2 min)

Evening:
- [ ] Check post analytics (impressions, engagement)
- [ ] Update Airtable Published_Content table (3 min)
- [ ] Reply to 2-5 comments (5-10 min)

**Total time: ~20-25 min/day**

---

**Phase 1 complete when:**
✅ 5 posts published
✅ Workflow stable (no errors 5 days straight)
✅ Avg engagement >2%
✅ First social signup to marketplace

**Then → Proceed to Phase 2: Multi-platform expansion**
