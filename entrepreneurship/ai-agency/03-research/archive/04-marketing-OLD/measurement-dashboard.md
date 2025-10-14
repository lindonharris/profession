# Social Media Performance Dashboard - buyanagent.ai

**Last Updated:** October 7, 2025
**Purpose:** Track social-attributed revenue and optimize content strategy
**Tech Stack:** Airtable + Retool (or internal React dashboard)

---

## Dashboard Overview

### North Star Metric: Social-Attributed Revenue (SAR)

**Definition:** Total MRR from customers who first clicked from social media

**Formula:**
```
SAR = SUM(MRR) WHERE customer.first_touch = 'social' AND status = 'active'
```

**Target Progression:**
- **Month 1:** $500 SAR (5 customers × avg $100)
- **Month 3:** $2,000 SAR (20 customers × avg $100)
- **Month 6:** $10,000 SAR (80 customers × avg $125)
- **Month 12:** $30,000 SAR (30% of total revenue from social)

---

## Dashboard Sections

### Section 1: Revenue Attribution

**Metrics Displayed:**

| Metric | Current | Last Week | Last Month | All-Time |
|--------|---------|-----------|------------|----------|
| **Social-Attributed MRR** | $2,450 | $2,100 | $1,800 | - |
| **New Customers (Social)** | 3 | 2 | 8 | 24 |
| **Avg Customer LTV** | $1,850 | $1,750 | $1,600 | $1,700 |
| **Social % of Total Revenue** | 18% | 15% | 12% | - |

**Visual:** Line chart showing SAR growth over time (weekly granularity)

---

### Section 2: Funnel Metrics

**Social Traffic → Marketplace → Signup → Customer**

| Stage | Current Week | Conversion Rate | Trend |
|-------|--------------|-----------------|-------|
| **Social Clicks** | 1,247 | - | ↑ 12% |
| **Marketplace Visits** | 1,098 | 88% | ↑ 8% |
| **Signups** | 87 | 8% | ↑ 15% |
| **Paying Customers** | 12 | 14% | ↑ 22% |

**Visual:** Funnel chart with drop-off rates at each stage

**Insight Engine:**
- Red flag if social → marketplace <80% (broken UTM tracking)
- Red flag if marketplace → signup <5% (landing page issue)
- Red flag if signup → customer <10% (activation/onboarding issue)

---

### Section 3: Platform Performance

**Compare LinkedIn vs Twitter vs Threads**

| Platform | Posts | Impressions | Engagement | Clicks | CTR | Signups | Cost/Signup |
|----------|-------|-------------|------------|--------|-----|---------|-------------|
| **LinkedIn** | 5 | 12,400 | 580 (4.7%) | 124 | 1.0% | 8 | $0 |
| **Twitter** | 12 | 8,900 | 267 (3.0%) | 89 | 1.0% | 5 | $0 |
| **Threads** | 4 | 3,200 | 192 (6.0%) | 32 | 1.0% | 2 | $0 |
| **TOTAL** | 21 | 24,500 | 1,039 (4.2%) | 245 | 1.0% | 15 | $0 |

**Visual:** Bar chart comparing CTR and Signup rate by platform

**Insight:**
- Threads has highest engagement rate but lowest reach
- LinkedIn drives most signups (professional audience = higher intent)
- Twitter has volume but lower conversion quality

**Action:** Shift 20% of Twitter effort to LinkedIn (higher ROI)

---

### Section 4: Content Performance

**Top 10 Posts (by signups attributed)**

| Rank | Post Title | Platform | Pillar | Impressions | Engagement | Clicks | Signups | Conversion |
|------|-----------|----------|--------|-------------|------------|--------|---------|------------|
| 1 | "Cut DSO 37% case study" | LinkedIn | Automation Wins | 4,200 | 280 (6.7%) | 52 | 6 | 11.5% |
| 2 | "SaaS is dying" hot take | Twitter | Anti-Bloat | 2,800 | 145 (5.2%) | 28 | 3 | 10.7% |
| 3 | "$10K MRR milestone" | LinkedIn | Transparency | 3,100 | 190 (6.1%) | 31 | 2 | 6.5% |

**Visual:** Table with sortable columns + drill-down to post text

**Insight Engine:**
- "Automation Wins" pillar has 2x signup rate vs average
- Case studies with metrics outperform generic advice
- Hot takes drive engagement but lower conversion quality

**Action:** Double down on customer case studies (Pillar 1)

---

### Section 5: Content Pillar Distribution

**Actual vs Target Mix (This Week)**

| Pillar | Target % | Actual % | Performance Score | Action |
|--------|----------|----------|-------------------|--------|
| **Automation Wins** | 30% | 35% | 8.2/10 ⭐ | Keep +5% over target |
| **Anti-Bloat** | 20% | 25% | 6.5/10 | Good engagement, low conversion |
| **Transparency** | 20% | 15% | 7.1/10 | Increase to target |
| **AI Practicality** | 20% | 20% | 5.8/10 | Educational, low conversion |
| **Empowerment** | 10% | 5% | 4.2/10 ⚠️ | Underperforming, keep minimal |

**Visual:** Donut chart showing distribution + performance heatmap

**Insight:**
- Automation Wins over-indexing (good thing - keeps driving signups)
- Empowerment pillar underperforming (consider dropping to 5% permanently)
- Transparency needs boost (builds trust for later conversion)

---

### Section 6: Follower Growth

**Platform-Specific Growth Rates**

| Platform | Followers | New (7d) | Growth Rate | Target (Month 3) | On Track? |
|----------|-----------|----------|-------------|------------------|-----------|
| **LinkedIn** | 1,247 | 89 | +7.7%/week | 2,000 | ✅ Yes |
| **Twitter** | 2,103 | 156 | +8.0%/week | 3,500 | ✅ Yes |
| **Threads** | 487 | 31 | +6.8%/week | 800 | ⚠️ Slightly behind |

**Visual:** Line chart showing follower growth over time (all platforms)

**Insight:**
- LinkedIn growing fastest (professional audience sticks)
- Threads slower but highest engagement per follower
- Twitter has most followers but engagement declining

**Action:** Threads - test daily posting cadence (currently 2x/week)

---

### Section 7: Engagement Quality

**Beyond Vanity Metrics - What Drives Signups?**

| Engagement Type | Count | Signup Attribution | Quality Score |
|-----------------|-------|-------------------|---------------|
| **Comments** | 124 | 18 signups (14.5%) | ⭐⭐⭐⭐⭐ High |
| **Shares** | 67 | 8 signups (11.9%) | ⭐⭐⭐⭐ Good |
| **Likes** | 1,039 | 12 signups (1.2%) | ⭐⭐ Low |

**Insight:**
- Comments = highest-intent engagement (14.5% signup rate)
- Shares = good (11.9% signup rate from referred traffic)
- Likes = vanity metric (1.2% signup rate)

**Action:**
- Optimize for comments (ask questions, provoke discussion)
- Reply to every comment within 2 hours (drives more discussion)
- De-prioritize "like bait" content

---

### Section 8: Time-to-Convert Analysis

**How long from first social click to paying customer?**

| Timeframe | Customers | % of Total | Cumulative |
|-----------|-----------|------------|------------|
| **0-24 hours** | 4 | 16% | 16% |
| **1-7 days** | 12 | 48% | 64% |
| **8-14 days** | 6 | 24% | 88% |
| **15-30 days** | 2 | 8% | 96% |
| **30+ days** | 1 | 4% | 100% |

**Visual:** Histogram showing conversion timeline

**Insight:**
- 64% convert within 7 days (social drives fast decisions)
- 88% convert within 14 days (remarketing window = 2 weeks)
- Long tail (30+ days) rare but valuable (email nurture needed)

**Action:**
- Email drip campaign for social signups (7-day nurture)
- Retarget social traffic with specific agent ads (if we add paid later)

---

### Section 9: UTM Tracking Deep-Dive

**Granular Attribution by Source**

| UTM Source | UTM Medium | UTM Campaign | Clicks | Signups | Conv Rate | MRR |
|------------|------------|--------------|--------|---------|-----------|-----|
| linkedin | social | automation-wins | 124 | 8 | 6.5% | $650 |
| twitter | social | anti-bloat | 89 | 5 | 5.6% | $425 |
| linkedin | social | transparency | 67 | 4 | 6.0% | $400 |
| threads | social | empowerment | 32 | 2 | 6.3% | $200 |

**UTM Format:**
```
https://buyanagent.ai?utm_source={platform}&utm_medium=social&utm_campaign={pillar}&utm_content={post_id}
```

**Insight:**
- LinkedIn "automation-wins" campaign = best ROI
- Twitter "anti-bloat" has volume but lower conversion
- Threads small sample but promising conversion rate

**Action:** Build more "automation-wins" content for LinkedIn

---

### Section 10: Weekly Performance Summary (GPT-4 Generated)

**Auto-Generated Every Sunday 8pm**

**Sample Output:**
```
📊 Social Performance Summary - Week of Oct 7, 2025

🎯 North Star Metric:
Social-Attributed MRR: $2,450 (+16% vs last week)
New customers from social: 3 (target: 5/week) ⚠️

✅ What Worked:
1. LinkedIn case study ("Cut DSO 37%") - 6 signups, 11.5% conv rate
2. Engagement rate up to 4.7% (target: 5%) - almost there!
3. Comments driving 14.5% signup rate (focus here)

⚠️ What Didn't:
1. Threads engagement down 15% (test daily posting)
2. Empowerment pillar underperforming (4.2/10 score)
3. Twitter volume high but conversion quality declining

📈 Recommended Actions:
1. Double down on LinkedIn case studies (Automation Wins pillar)
2. Reduce Empowerment content from 10% → 5%
3. Test Threads daily posting (currently 2x/week)
4. Reply to every comment within 2 hours (boosts engagement)

🎯 Next Week Goals:
- 5 new social customers (vs 3 this week)
- 5% engagement rate on LinkedIn
- 100+ comments across all platforms
```

**Delivered via:** Slack #marketing channel + Email to founder

---

## Data Pipeline Architecture

### Data Sources

**1. Social Platform APIs**
- **LinkedIn API:** Post impressions, engagement, follower growth
- **Twitter API v2:** Tweet analytics, profile stats
- **Threads API:** (manual scraping until API available)

**2. Website Analytics**
- **Plausible/Fathom:** UTM-tracked traffic, page views, session duration
- **Supabase:** Signup events, customer creation events

**3. Stripe**
- **Subscription data:** MRR, customer LTV, churn rate

**4. Airtable**
- **Content database:** Post text, pillar assignment, publishing schedule
- **Engagement tracking:** Manual log of comments/shares (until API automation)

---

### Data Flow

```
Social APIs → n8n Webhook → Postgres (raw events)
   ↓
Nightly ETL Job (n8n cron) → Transform & aggregate
   ↓
Postgres Analytics Tables → Dashboard queries
   ↓
Retool/React Dashboard → Real-time display
```

**Update Frequency:**
- **Real-time:** Social clicks (UTM tracking)
- **Hourly:** Engagement metrics (API polling)
- **Daily:** Follower growth, content performance
- **Weekly:** GPT-4 summary report

---

## Key Dashboard Queries

### Query 1: Social-Attributed MRR

```sql
SELECT
  SUM(s.mrr) as total_sar,
  COUNT(DISTINCT c.id) as customer_count,
  AVG(s.mrr) as avg_mrr_per_customer
FROM customers c
JOIN subscriptions s ON c.id = s.customer_id
WHERE c.utm_source IN ('linkedin', 'twitter', 'threads')
  AND c.utm_medium = 'social'
  AND s.status = 'active';
```

---

### Query 2: Funnel Conversion Rates

```sql
SELECT
  COUNT(*) FILTER (WHERE event_type = 'social_click') as clicks,
  COUNT(*) FILTER (WHERE event_type = 'page_view') as visits,
  COUNT(*) FILTER (WHERE event_type = 'signup') as signups,
  COUNT(*) FILTER (WHERE event_type = 'subscription_created') as customers,

  -- Conversion rates
  ROUND(100.0 * COUNT(*) FILTER (WHERE event_type = 'page_view') /
    NULLIF(COUNT(*) FILTER (WHERE event_type = 'social_click'), 0), 2) as visit_rate,

  ROUND(100.0 * COUNT(*) FILTER (WHERE event_type = 'signup') /
    NULLIF(COUNT(*) FILTER (WHERE event_type = 'page_view'), 0), 2) as signup_rate,

  ROUND(100.0 * COUNT(*) FILTER (WHERE event_type = 'subscription_created') /
    NULLIF(COUNT(*) FILTER (WHERE event_type = 'signup'), 0), 2) as customer_rate

FROM analytics_events
WHERE created_at >= NOW() - INTERVAL '7 days'
  AND utm_medium = 'social';
```

---

### Query 3: Top Performing Posts

```sql
SELECT
  p.post_id,
  p.post_text,
  p.platform,
  p.content_pillar,
  p.impressions,
  p.engagement_count,
  ROUND(100.0 * p.engagement_count / NULLIF(p.impressions, 0), 2) as engagement_rate,
  COUNT(DISTINCT c.id) as signups_attributed,
  SUM(s.mrr) as mrr_attributed

FROM published_content p
LEFT JOIN customers c ON c.utm_content = p.post_id
LEFT JOIN subscriptions s ON c.id = s.customer_id

WHERE p.published_at >= NOW() - INTERVAL '30 days'

GROUP BY p.post_id, p.post_text, p.platform, p.content_pillar, p.impressions, p.engagement_count

ORDER BY signups_attributed DESC, engagement_rate DESC

LIMIT 10;
```

---

## Alert System

### Critical Alerts (Immediate Slack Notification)

**1. High-Performing Post**
- **Trigger:** Post exceeds 100 likes within first 2 hours
- **Action:** Auto-boost via reply thread + cross-post to other platforms

**2. Negative Sentiment**
- **Trigger:** Comment with keywords: "scam", "doesn't work", "waste of money"
- **Action:** Human escalation for immediate response

**3. Conversion Drop**
- **Trigger:** Social → signup rate <3% for 3 consecutive days
- **Action:** Check landing page, review recent content quality

---

### Weekly Alerts (Sunday Summary)

**1. Performance vs Target**
- **Green:** SAR growth ≥10% week-over-week
- **Yellow:** SAR growth 0-10%
- **Red:** SAR decline

**2. Content Pillar Imbalance**
- **Alert if:** Any pillar >15% over/under target for 2 weeks

**3. Platform Health**
- **Alert if:** Engagement rate <2% on any platform for 2 weeks

---

## Dashboard Access & Permissions

**Founder (Full Access):**
- View all metrics
- Edit content strategy
- Export raw data
- Modify alert thresholds

**Marketing Contractor (View Only):**
- View metrics dashboard
- Cannot edit strategy
- Cannot export customer data

**Public (Transparency Page - Optional Future):**
- Follower counts
- SAR (aggregate only, no customer details)
- Top 5 performing posts (no revenue data)

---

## Implementation Timeline

### Week 1: Data Infrastructure
- [ ] Set up Postgres analytics tables
- [ ] Build UTM tracking (Plausible/Fathom integration)
- [ ] Create n8n data pipeline (API → Postgres)

### Week 2: Dashboard Build
- [ ] Design dashboard mockup (Figma)
- [ ] Build Retool dashboard (or custom React app)
- [ ] Connect queries to live data

### Week 3: Testing & Refinement
- [ ] Validate data accuracy (compare to platform native analytics)
- [ ] Set up alert system (Slack webhooks)
- [ ] Train GPT-4 weekly summary generator

### Week 4: Launch
- [ ] Daily monitoring begins
- [ ] First weekly summary report
- [ ] Iterate based on insights

---

## Success Metrics for Dashboard

**Dashboard is successful if:**
1. ✅ Founder checks it 3x/week minimum
2. ✅ Weekly insights drive 2+ content strategy changes/month
3. ✅ SAR attribution accuracy ≥90% (validated against customer interviews)
4. ✅ Dashboard load time <2 seconds
5. ✅ Zero manual data entry required (full automation)

**Dashboard fails if:**
1. ❌ Founder stops checking it (not actionable)
2. ❌ Data staleness >24 hours (pipeline broken)
3. ❌ Too complex to understand at a glance (needs simplification)

---

## Next Steps

1. **Review with founder:** Confirm metrics priority
2. **Choose tech stack:** Retool vs custom React dashboard
3. **Build data pipeline:** n8n → Postgres (Week 1)
4. **Launch MVP dashboard:** Basic metrics only (Week 2)
5. **Iterate:** Add advanced sections weekly

**The goal: Make social marketing 100% data-driven within 4 weeks.**
