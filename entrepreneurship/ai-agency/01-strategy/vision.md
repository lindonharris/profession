# Technical Vision: buyanagent.ai Marketplace

**Last Updated:** October 6, 2025 (Tiered Pricing Strategy)
**Status:** Architecture Design Phase
**Goal:** Self-service AI agent marketplace (not boutique service)

---

## Vision Statement

**"The Shopify App Store for AI Agents"**

A two-tier self-service marketplace where entrepreneurs browse 22 pre-built AI agents, activate any agent in 15-30 minutes via simple wizard, and choose between:
- **Utility Tier:** $29-79/month per agent (invisible automation, status pages, email support)
- **Premium Tier:** $100-150/month per agent (business intelligence dashboards, analytics, priority support)

---

## What Changed (Strategic Pivot)

### OLD Vision (Archived)
- Single high-touch product (Invoice & Collections AI)
- $12K setup + $2K/month (boutique pricing)
- Sales-led with white-glove onboarding
- Target: Marketing agencies only

### NEW Vision (Current)
- Marketplace with 22 simple internal agents
- Two-tier pricing: $29-79/month (Utility Tier) or $100-150/month (Premium Tier)
- Launch Strategy: Phased rollout - Utility tier first (Weeks 1-5), Premium tier second (Weeks 6-10)
- Target: All productivity-focused small businesses
- Trojan Horse: Use low-cost Utility tier ($29-79) to capture broad market, upsell to Premium tier ($100-150) for business intelligence

**Why:** Founder constraints (no time for sales), scalability (self-service scales infinitely), product feasibility (internal agents are 10x simpler), boutique positioning through premium tier

---

## Technical Architecture

### Stack Overview

```
┌─────────────────────────────────────────────────────┐
│                    FRONTEND                         │
│  Lovable (AI-generated React + Tailwind)           │
│  - Marketplace UI                                   │
│  - Agent detail pages                               │
│  - Activation wizard                                │
│  - Customer dashboard                               │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│                    BACKEND                          │
│  Supabase (Postgres + Auth + Realtime)            │
│  - User accounts                                    │
│  - Agent templates catalog                          │
│  - User-agent activations                           │
│  - Subscription management                          │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│                   PAYMENTS                          │
│  Stripe (Checkout + Billing + Webhooks)           │
│  - Multi-subscription model                         │
│  - One subscription per agent per user              │
│  - Automatic renewals                               │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│                AGENT RUNTIME                        │
│  n8n Cloud (Workflow Automation Engine)            │
│  - Agent workflows                                  │
│  - OAuth integrations                               │
│  - GPT-4 AI processing                              │
└─────────────────────────────────────────────────────┘
```

### Technology Choices

**Frontend: Lovable**
- **Why:** AI-powered React generation (build 10x faster)
- **What:** Input natural language → Get production React + Tailwind
- **Example:** "Create product card with hover effect" → Generates component in seconds
- **Cost:** Free for prototyping, $20/month for export

**Backend: Supabase**
- **Why:** Postgres + Auth + Realtime in one platform
- **What:** Firebase alternative with SQL database
- **Features:** Row-level security, real-time subscriptions, OAuth providers
- **Cost:** Free tier (50K rows), $25/month Pro (unlimited)

**Payments: Stripe**
- **Why:** Industry standard, supports multi-subscriptions natively
- **What:** Checkout + Billing + Webhooks
- **Model:** Each activated agent = separate Stripe subscription
- **Cost:** 2.9% + $0.30 per transaction (same as all payment processors)

**Agent Runtime: n8n Cloud**
- **Why:** Visual workflow builder, 350+ integrations, affordable
- **What:** Each agent = n8n workflow template
- **Deployment:** Clone template → Inject user's OAuth tokens → Activate
- **Cost:** $50/month Pro (10K operations, scales with usage)

**Hosting: Vercel**
- **Why:** Zero-config React hosting, edge functions, fast deploys
- **What:** Hosts Lovable-generated frontend
- **Cost:** Free hobby tier, $20/month Pro (unlimited bandwidth)

---

## Database Schema (Supabase)

### Core Tables

```sql
-- Users (managed by Supabase Auth)
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  email TEXT UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Agent Templates (the 20+ agents we offer)
CREATE TABLE agent_templates (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  slug TEXT UNIQUE NOT NULL, -- 'expense-tracker'
  name TEXT NOT NULL, -- 'Expense Tracker & Categorizer'
  description TEXT,
  category TEXT, -- 'finance', 'productivity', 'marketing', 'operations'
  icon_emoji TEXT, -- '💰'
  setup_time_minutes INTEGER, -- 20
  integrations JSONB, -- ['gmail', 'google-sheets']
  pricing_utility INTEGER, -- 2900-7900 (in cents: $29-79)
  pricing_premium INTEGER, -- 10000-15000 (in cents: $100-150)
  build_status TEXT, -- 'live', 'beta', 'coming-soon'
  n8n_template_id TEXT, -- Reference to n8n workflow template
  created_at TIMESTAMP DEFAULT NOW()
);

-- User Agents (many-to-many: users activate multiple agents)
CREATE TABLE user_agents (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  agent_template_id UUID REFERENCES agent_templates(id),
  tier TEXT NOT NULL, -- 'self_service' or 'premium'
  status TEXT, -- 'active', 'paused', 'cancelled'
  config JSONB, -- User's configuration (categories, schedules, etc.)
  n8n_workflow_id TEXT, -- Deployed workflow ID
  stripe_subscription_id TEXT, -- Stripe subscription for this agent
  activated_at TIMESTAMP DEFAULT NOW(),
  cancelled_at TIMESTAMP,
  UNIQUE(user_id, agent_template_id) -- User can only activate each agent once
);

-- OAuth Integrations (user's connected services)
CREATE TABLE oauth_integrations (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  service TEXT NOT NULL, -- 'gmail', 'google-sheets', 'slack', etc.
  access_token TEXT, -- Encrypted
  refresh_token TEXT, -- Encrypted
  expires_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(user_id, service)
);

-- Subscriptions (mirrors Stripe subscriptions)
CREATE TABLE subscriptions (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  user_agent_id UUID REFERENCES user_agents(id),
  stripe_subscription_id TEXT UNIQUE NOT NULL,
  stripe_customer_id TEXT NOT NULL,
  status TEXT, -- 'active', 'past_due', 'cancelled'
  current_period_start TIMESTAMP,
  current_period_end TIMESTAMP,
  cancel_at_period_end BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Agent Activity Logs (for dashboard analytics)
CREATE TABLE agent_activity_logs (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_agent_id UUID REFERENCES user_agents(id),
  event_type TEXT, -- 'execution_success', 'execution_error', 'data_processed'
  metadata JSONB, -- Event-specific data
  created_at TIMESTAMP DEFAULT NOW()
);
```

### Row-Level Security (RLS)

```sql
-- Users can only see their own data
ALTER TABLE user_agents ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view own agents"
  ON user_agents FOR SELECT
  USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own agents"
  ON user_agents FOR INSERT
  WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own agents"
  ON user_agents FOR UPDATE
  USING (auth.uid() = user_id);

-- Agent templates are public (everyone can browse)
ALTER TABLE agent_templates ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone can view agent templates"
  ON agent_templates FOR SELECT
  TO PUBLIC
  USING (TRUE);
```

---

## User Flows

### Flow 1: Browse & Activate Agent

**Step 1: Marketplace Homepage**
```
User visits buyanagent.ai
→ Sees grid of 20+ agent cards
→ Filters by category (Finance, Productivity, etc.)
→ Clicks "Expense Tracker" card
```

**Step 2: Agent Detail Page**
```
User views:
- What it does (3-step visual)
- Integrations required (Gmail + Google Sheets)
- Pricing: Utility Tier ($69-79/month) or Premium Tier ($100/month) [varies by agent]
- Customer reviews (4.9/5 stars)
→ Clicks "Activate Agent" CTA
```

**Step 3: Authentication (if not logged in)**
```
Supabase Auth modal:
- Sign up with Google (OAuth)
- Or email + password
→ Account created in `users` table
```

**Step 4: Activation Wizard (5 steps)**
```
Step 1: Connect Integrations
- Click "Connect Gmail" → OAuth popup → Token stored in `oauth_integrations`
- Click "Connect Google Sheets" → OAuth popup → Token stored

Step 2: Configure Rules
- Select expense categories (Travel, Meals, etc.) → Checkboxes
- Choose notification preferences → Toggles
→ Config saved to `user_agents.config` (JSONB)

Step 3: Test Agent
- Backend: Clones n8n template
- Backend: Injects OAuth tokens
- Backend: Runs test execution with sample data
- Frontend: Shows test results ("Found 1 receipt, extracted $42.50")
→ User confirms accuracy

Step 4: Subscribe via Stripe
- User selects tier: Utility Tier (agent-specific pricing $29-79) or Premium Tier ($100-150)
- Stripe Checkout modal opens
- Price varies by agent and tier (e.g., Expense Manager: $69 Utility / $100 Premium)
- User enters payment info
→ Stripe webhook creates subscription
→ Row inserted into `subscriptions` table
→ Row inserted into `user_agents` table (status: 'active', tier: 'utility' or 'premium')

Step 5: Activation Complete
- n8n workflow activated (status changed to 'active')
- Success screen: "Agent is live! Check your dashboard."
→ Redirect to dashboard
```

**Database State After Activation:**
```sql
-- users table
{
  id: 'uuid-123',
  email: 'user@example.com'
}

-- user_agents table
{
  id: 'uuid-456',
  user_id: 'uuid-123',
  agent_template_id: 'uuid-expense-tracker',
  tier: 'utility', -- or 'premium'
  status: 'active',
  config: {
    categories: ['Travel', 'Meals', 'Office Supplies'],
    notifications: true
  },
  n8n_workflow_id: 'n8n-workflow-789',
  stripe_subscription_id: 'sub_abc123'
}

-- subscriptions table
{
  id: 'uuid-789',
  user_id: 'uuid-123',
  user_agent_id: 'uuid-456',
  stripe_subscription_id: 'sub_abc123',
  status: 'active',
  current_period_end: '2025-11-05'
}

-- oauth_integrations table
{
  user_id: 'uuid-123',
  service: 'gmail',
  access_token: 'encrypted_token_xyz'
},
{
  user_id: 'uuid-123',
  service: 'google-sheets',
  access_token: 'encrypted_token_abc'
}
```

---

### Flow 2: Manage Agent (Dashboard)

**User visits `/dashboard`**

**View Active Agents:**
```
┌────────────────────────────────────┐
│ My Agents (3 active)               │
├────────────────────────────────────┤
│ 💰 Expense Tracker                 │
│ Tier: Utility | $69/month          │
│ Last run: 2 hours ago              │
│ [Pause] [Settings] [Upgrade] [Cancel] │
├────────────────────────────────────┤
│ 📝 Meeting Notes                   │
│ Tier: Premium | $150/month         │
│ Last run: 30 min ago               │
│ [Pause] [Settings] [Cancel]        │
└────────────────────────────────────┘
```

**Click "Settings" on Expense Tracker:**
```
→ Modal opens with current config
→ User changes categories (add "Software")
→ Click "Save"
→ UPDATE user_agents SET config = {...} WHERE id = 'uuid-456'
→ Backend: Updates n8n workflow with new config
→ Success message: "Settings saved"
```

**Click "Pause":**
```
→ Confirmation modal: "Pause Expense Tracker?"
→ User confirms
→ UPDATE user_agents SET status = 'paused' WHERE id = 'uuid-456'
→ Backend: Deactivates n8n workflow (doesn't delete, just stops running)
→ Stripe subscription continues (still charged, but agent inactive)
→ Success message: "Agent paused. You can resume anytime."
```

**Click "Cancel":**
```
→ Confirmation modal: "Cancel Expense Tracker? This will:"
  - Stop the agent immediately
  - Cancel your $69/month subscription
  - Delete all configuration
→ User confirms
→ Backend: Calls Stripe API to cancel subscription
→ Stripe webhook receives cancellation event
→ UPDATE subscriptions SET status = 'cancelled' WHERE stripe_subscription_id = '...'
→ UPDATE user_agents SET status = 'cancelled', cancelled_at = NOW()
→ Backend: Deletes n8n workflow
→ Success message: "Agent cancelled. No further charges."
```

---

### Flow 3: Stripe Webhook Handling

**Webhook: `customer.subscription.created`**
```javascript
// Stripe sends this when user subscribes via checkout

async function handleSubscriptionCreated(event) {
  const subscription = event.data.object;

  // Create subscription record in Supabase
  await supabase.from('subscriptions').insert({
    stripe_subscription_id: subscription.id,
    stripe_customer_id: subscription.customer,
    user_id: subscription.metadata.user_id, // Passed during checkout
    user_agent_id: subscription.metadata.user_agent_id,
    status: subscription.status,
    current_period_start: subscription.current_period_start,
    current_period_end: subscription.current_period_end
  });

  // Update user_agent status to 'active'
  await supabase
    .from('user_agents')
    .update({ status: 'active' })
    .eq('id', subscription.metadata.user_agent_id);
}
```

**Webhook: `customer.subscription.deleted`**
```javascript
// Stripe sends this when subscription cancelled

async function handleSubscriptionDeleted(event) {
  const subscription = event.data.object;

  // Update subscription status
  await supabase
    .from('subscriptions')
    .update({ status: 'cancelled' })
    .eq('stripe_subscription_id', subscription.id);

  // Update user_agent status
  await supabase
    .from('user_agents')
    .update({
      status: 'cancelled',
      cancelled_at: new Date()
    })
    .eq('stripe_subscription_id', subscription.id);

  // Delete n8n workflow
  const { data: userAgent } = await supabase
    .from('user_agents')
    .select('n8n_workflow_id')
    .eq('stripe_subscription_id', subscription.id)
    .single();

  await n8nAPI.deleteWorkflow(userAgent.n8n_workflow_id);
}
```

**Webhook: `invoice.payment_succeeded`**
```javascript
// Stripe sends this every month when renewal succeeds

async function handlePaymentSucceeded(event) {
  const invoice = event.data.object;

  // Log successful payment
  await supabase.from('agent_activity_logs').insert({
    user_agent_id: invoice.subscription.metadata.user_agent_id,
    event_type: 'payment_succeeded',
    metadata: {
      amount: invoice.amount_paid,
      invoice_id: invoice.id
    }
  });

  // Send confirmation email via Resend
  await resend.sendEmail({
    to: invoice.customer_email,
    subject: 'Payment Confirmed - buyanagent.ai',
    template: 'payment-success',
    data: {
      amount: invoice.amount_paid / 100,
      agent_name: '...'
    }
  });
}
```

**Webhook: `invoice.payment_failed`**
```javascript
// Stripe sends this if card declined

async function handlePaymentFailed(event) {
  const invoice = event.data.object;

  // Update subscription status
  await supabase
    .from('subscriptions')
    .update({ status: 'past_due' })
    .eq('stripe_subscription_id', invoice.subscription);

  // Pause agent (don't delete, give them chance to fix payment)
  await supabase
    .from('user_agents')
    .update({ status: 'paused' })
    .eq('stripe_subscription_id', invoice.subscription);

  // Send urgent email
  await resend.sendEmail({
    to: invoice.customer_email,
    subject: '⚠️ Payment Failed - Action Required',
    template: 'payment-failed',
    data: {
      update_payment_url: `${process.env.APP_URL}/dashboard/billing`
    }
  });
}
```

---

## Agent Deployment System

### n8n Workflow Template Structure

**Template: Expense Tracker Agent**
```json
{
  "name": "Expense Tracker - {{user_id}}",
  "nodes": [
    {
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "credentials": {
        "gmailOAuth2": "{{gmail_credentials_id}}"
      },
      "parameters": {
        "filters": {
          "hasAttachment": true,
          "labelIds": ["INBOX"]
        }
      }
    },
    {
      "name": "Filter Receipts",
      "type": "n8n-nodes-base.filter",
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json.subject}}",
              "operation": "contains",
              "value2": "receipt|invoice"
            }
          ]
        }
      }
    },
    {
      "name": "Extract with GPT-4",
      "type": "n8n-nodes-base.openai",
      "credentials": {
        "openAiApi": "platform_credentials"
      },
      "parameters": {
        "model": "gpt-4",
        "prompt": "Extract vendor, amount, date, and category from this receipt: {{$json.body}}"
      }
    },
    {
      "name": "Categorize",
      "type": "n8n-nodes-base.function",
      "parameters": {
        "functionCode": "const categories = {{user_config.categories}};\n// Logic to match category..."
      }
    },
    {
      "name": "Log to Google Sheets",
      "type": "n8n-nodes-base.googleSheets",
      "credentials": {
        "googleSheetsOAuth2": "{{sheets_credentials_id}}"
      },
      "parameters": {
        "operation": "append",
        "sheetId": "{{user_config.sheet_id}}",
        "range": "A:E",
        "values": [
          "={{$json.date}}",
          "={{$json.vendor}}",
          "={{$json.amount}}",
          "={{$json.category}}",
          "={{$json.notes}}"
        ]
      }
    }
  ]
}
```

### Deployment Process

**When user activates agent:**

```javascript
async function deployAgent(userId, agentTemplateId, config, oauthTokens) {
  // 1. Fetch template from database
  const { data: template } = await supabase
    .from('agent_templates')
    .select('n8n_template_id')
    .eq('id', agentTemplateId)
    .single();

  // 2. Clone n8n template
  const workflow = await n8nAPI.cloneTemplate(template.n8n_template_id);

  // 3. Inject OAuth credentials
  workflow.credentials = {
    gmail_credentials_id: await n8nAPI.createCredential('gmail', oauthTokens.gmail),
    sheets_credentials_id: await n8nAPI.createCredential('google-sheets', oauthTokens.sheets)
  };

  // 4. Inject user config
  workflow.nodes.forEach(node => {
    if (node.name === 'Categorize') {
      node.parameters.functionCode = node.parameters.functionCode.replace(
        '{{user_config.categories}}',
        JSON.stringify(config.categories)
      );
    }
  });

  // 5. Save workflow
  const deployed = await n8nAPI.createWorkflow(workflow);

  // 6. Activate workflow
  await n8nAPI.activateWorkflow(deployed.id);

  // 7. Return workflow ID
  return deployed.id;
}
```

---

## Scalability Architecture

### Multi-Tenancy Strategy

**Current: Shared n8n Instance**
- All users' workflows run on same n8n Cloud account
- Workflows are isolated (separate credentials per user)
- Pros: Simple, cheap ($50/month for all users)
- Cons: Hit limits at ~1,000 active agents

**Future: Dedicated n8n Instances**
- 1-100 users: Shared instance
- 100-500 users: 2-3 dedicated instances (load balanced)
- 500+ users: Kubernetes cluster with auto-scaling

**Migration Path:**
1. Start with n8n Cloud (Month 1-6)
2. Self-host on AWS/GCP when hit 1,000 agents (Month 6-12)
3. Kubernetes cluster for 10K+ agents (Year 2+)

---

### Performance Optimization

**Database:**
- Index on `user_agents.user_id` for fast dashboard queries
- Index on `subscriptions.stripe_subscription_id` for webhook lookups
- Partitioning on `agent_activity_logs` by month (archive old logs)

**Caching:**
- Redis for agent template catalog (rarely changes, cache 1 hour)
- Cloudflare CDN for static assets (agent icons, images)

**API Rate Limiting:**
- 100 requests/minute per user (prevent abuse)
- 1 activation per 5 seconds (prevent duplicate subscriptions)

---

## Security & Compliance

### OAuth Token Storage

**Encryption at Rest:**
```javascript
// Store tokens encrypted in Supabase
const encrypted = await crypto.subtle.encrypt(
  { name: 'AES-GCM', iv: randomIV },
  encryptionKey,
  JSON.stringify(oauthToken)
);

await supabase.from('oauth_integrations').insert({
  user_id,
  service: 'gmail',
  access_token: Buffer.from(encrypted).toString('base64'),
  refresh_token: '...'
});
```

**Decryption for Agent Use:**
```javascript
// Decrypt only when needed for workflow execution
const { data } = await supabase
  .from('oauth_integrations')
  .select('access_token')
  .eq('user_id', userId)
  .eq('service', 'gmail')
  .single();

const decrypted = await crypto.subtle.decrypt(
  { name: 'AES-GCM', iv: storedIV },
  encryptionKey,
  Buffer.from(data.access_token, 'base64')
);

const token = JSON.parse(Buffer.from(decrypted).toString());
```

### Data Privacy

**User Data Isolation:**
- Each user's data in separate rows (enforced by RLS)
- No cross-user data access possible
- Audit logs for all data access

**GDPR Compliance:**
- User can delete account → CASCADE deletes all data
- Export all user data (JSON download from dashboard)
- Privacy policy page (required before launch)

---

## Cost Structure (Monthly)

**Fixed Costs:**
- Vercel Pro: $20
- Supabase Pro: $25
- n8n Cloud Pro: $50
- Domain + SSL: $2
- **Total: $97/month**

**Variable Costs:**
- Stripe fees: 2.9% + $0.30 per transaction
  - Utility Tier: $29-79/month avg $60 = $2.04 per transaction
  - Premium Tier: $100-150/month avg $115 = $3.64 per transaction
- GPT-4 API: ~$0.01 per agent execution
  - 1,000 executions/month = $10
- Email (Resend): $20/month (50K emails)

**Total Cost for 250 Customers (Year 1 Mix):**
Scenario: 150 Utility + 100 Premium customers
- Fixed: $97
- Utility Stripe fees: (150 × 2 agents × $2.04) = $612
- Premium Stripe fees: (100 × 1.5 agents × $3.64) = $546
- GPT-4: $525 (52.5K executions for 450 total agents)
- Email: $20
- **Total: $1,800/month**

**Revenue from 250 Customers (Year 1 Mix):**
- Utility: 150 users × 2 agents avg × $60 = $18,000/month
- Premium: 100 users × 1.5 agents avg × $115 = $17,250/month
- **Total: $35,250/month ($423K ARR)**

**Gross Margin:** 94.9% ($33,450 profit on $35.25K revenue)

---

## Build Timeline (10 Weeks to MVP - Phased Rollout)

**Weeks 1-4: Marketplace Foundation**
- Lovable UI Generation (marketplace, agent pages, dashboards)
- Supabase + Stripe Integration (tier-based pricing)
- Activation wizard
- OAuth integration system

**Weeks 1-5: Phase 1A - Utility Tier Validation**
- Build Expense Manager + Newsletter Digester (n8n workflows)
- Launch Utility tier ($49-79 pricing)
- Goal: 30-50 customers, validate status page UX

**Week 5: Phase 1B - Utility Tier Completion**
- Build Email Sweeper ($29-39 entry price)
- Complete Utility tier portfolio (3 agents)
- Test multi-agent adoption

**Weeks 6-10: Phase 2 - Premium Tier Launch**
- Build Invoice Chaser + Lead Qualification (with full dashboards)
- Launch Premium tier ($100-150 pricing)
- Goal: 50+ Premium customers, validate dashboard value prop

---

## Next Steps

**This Week:**
1. Purchase domain (buyanagent.ai)
2. Create Lovable account
3. Generate marketplace homepage
4. Set up Supabase project

**See build-overview.md for complete step-by-step build plan.**
