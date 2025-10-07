# Research Execution Prompts for rsrch Agent

**Last Updated:** October 5, 2025 (Updated for $100/month pricing)
**Purpose:** Programmatic prompts for rsrch agent to validate marketplace strategy
**Pricing:** $100/month per agent (updated from $500/month based on Q2/Q3 findings)
**Usage:** Copy each prompt → Give to rsrch agent → Agent returns GO/NO-GO with evidence

---

## How to Use This Document

### Execution Method:
1. **Launch rsrch agent** for each question (parallel execution recommended)
2. **Copy the prompt exactly** from this document
3. **Agent will search** using Tavily AI-powered search
4. **Agent returns** PASS/FAIL with evidence and confidence score
5. **Track results** in a scoring sheet (15/20 minimum to proceed)

### Batch Execution:
You can run all 20 prompts in **parallel batches**:
- **Batch 1 (Pain):** Q1-Q5 simultaneously
- **Batch 2 (Market):** Q6-Q10 simultaneously
- **Batch 3 (Competition):** Q11-Q15 simultaneously
- **Batch 4 (Product):** Q16-Q18 simultaneously
- **Batch 5 (Business):** Q19-Q20 simultaneously

**Total Time:** 30-45 minutes (with parallel execution)

---

## Category 1: Pain Validation (Q1-Q5)

### Q1: Pre-Built Automation Demand

```
PROMPT FOR RSRCH AGENT:

Research Question: Do small businesses actively search for "pre-built automation" solutions?

Search Strategy:
1. Search Reddit, forums, and discussion boards for posts about "buy automation", "pre-built workflow", "ready made automation", "done for you automation"
2. Look for pain points around building automation from scratch (Zapier/Make complexity)
3. Find evidence of willingness to pay for pre-built vs DIY

Success Criteria:
- PASS: 5+ discussion threads showing desire for pre-built solutions
- FAIL: <5 threads or evidence shows people prefer DIY

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: Top 5 quotes with URLs
- Summary: 2-3 sentence conclusion
```

---

### Q2: Zapier Learning Curve Frustration

```
PROMPT FOR RSRCH AGENT:

Research Question: Are Zapier users frustrated with the DIY learning curve?

Search Strategy:
1. Search Reddit (r/Zapier, r/Entrepreneur, r/smallbusiness) for complaints about Zapier complexity
2. Look for phrases: "zapier too complicated", "zapier learning curve", "zapier takes too long", "zapier overwhelming"
3. Find time estimates for building workflows (should be 5-10+ hours)

Success Criteria:
- PASS: 10+ complaints about Zapier complexity/time investment
- FAIL: <10 complaints or users say it's easy

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: Top 10 complaint quotes with URLs
- Time Estimates: Average hours to build workflow (if mentioned)
- Summary: 2-3 sentence conclusion
```

---

### Q3: $100/Month SaaS Spending by Freelancers/SMBs

```
PROMPT FOR RSRCH AGENT:

Research Question: Do freelancers/SMBs pay for productivity SaaS at $100/month?

Search Strategy:
1. Find examples of productivity SaaS products priced at $80-120/month
2. Look for case studies, reviews, or discussions of freelancers/agencies using these tools
3. Search for "productivity software" + "freelancer" OR "agency" + pricing mentions

Success Criteria:
- PASS: 5+ comparable single-purpose SaaS products at $80-120/month with evidence of strong sales/adoption
- FAIL: No comparable products or evidence shows $100/month is too high for solo users

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: List 3-5 comparable SaaS products with pricing and customer counts
- Summary: 2-3 sentence conclusion
```

---

### Q4: Time Savings as Compelling Benefit

```
PROMPT FOR RSRCH AGENT:

Research Question: Is "30-minute setup" a compelling benefit vs "10 hours in Zapier"?

Search Strategy:
1. Find discussions about how long it takes to build Zapier workflows
2. Search for "zapier setup time", "how long to build zapier workflow", "zapier hours"
3. Look for frustration about time investment in automation setup

Success Criteria:
- PASS: Evidence that Zapier workflows take 5-10+ hours to build
- FAIL: Evidence shows workflows take <2 hours

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: Time estimates from users (quotes with URLs)
- Average Time: X hours to build typical workflow
- Summary: 2-3 sentence conclusion about time-saving value prop
```

---

### Q5: Specific Agent Use Case Demand

```
PROMPT FOR RSRCH AGENT:

Research Question: Do people search for our specific automation use cases?

Search Strategy:
1. Find search volume data for these 5 queries:
   - "automate expense tracking"
   - "automate meeting notes"
   - "email newsletter digest"
   - "social media repurposing automation"
   - "document organization automation"
2. Use keyword research tools, Google Trends, or discussion volume as proxy
3. Look for evidence people are actively seeking these solutions

Success Criteria:
- PASS: At least 2 use cases have 500+ monthly searches or significant discussion volume
- FAIL: <2 use cases have measurable demand

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: Search volume or discussion count for each of 5 use cases
- Top 2 Winners: Which use cases have highest demand
- Summary: 2-3 sentence conclusion about agent prioritization
```

---

## Category 2: Market Sizing (Q6-Q10)

### Q6: Zapier User Count

```
PROMPT FOR RSRCH AGENT:

Research Question: How many small businesses use Zapier/Make/n8n today?

Search Strategy:
1. Search for official company stats: "Zapier number of users 2024", "Make.com customer count", "n8n users"
2. Look for press releases, investor decks, or interviews mentioning user counts
3. Find third-party estimates if official numbers unavailable

Success Criteria:
- PASS: Zapier has 2M+ users (validates large TAM)
- FAIL: <2M users (market too small)

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: User counts for Zapier, Make, n8n (with sources)
- Total Market: Combined user base across all 3 platforms
- Summary: 2-3 sentence conclusion about TAM size
```

---

### Q7: Zapier Paid User Percentage

```
PROMPT FOR RSRCH AGENT:

Research Question: What percentage of Zapier users are on paid plans ($20-600/month)?

Search Strategy:
1. Search for "Zapier revenue", "Zapier ARR", "Zapier paid users percentage"
2. Calculate paid users from revenue data (if available)
3. Look for freemium conversion rate statistics

Success Criteria:
- PASS: 10%+ conversion to paid plans (200K+ paying users if 2M total)
- FAIL: <10% conversion (not enough paying customers to target)

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: Revenue data, paid user %, conversion rate (with sources)
- Paying Users: Estimated count of paid Zapier users
- Summary: 2-3 sentence conclusion about addressable market
```

---

### Q8: US Freelancer/Agency Count

```
PROMPT FOR RSRCH AGENT:

Research Question: How many freelancers/agencies exist in the US (all industries)?

Search Strategy:
1. Search for "number of freelancers United States 2024", "gig economy statistics"
2. Search for "number of small agencies US", "small business count 1-50 employees"
3. Look for government data (Census, BLS) or reputable research firms

Success Criteria:
- PASS: 50M+ freelancers/gig workers OR 10M+ small businesses (1-50 employees)
- FAIL: <10M total addressable businesses

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: Freelancer count + small business count (with sources)
- Total TAM: Combined addressable market
- Summary: 2-3 sentence conclusion about market breadth
```

---

### Q9: Productivity SaaS Market Size

```
PROMPT FOR RSRCH AGENT:

Research Question: What is the productivity SaaS market size?

Search Strategy:
1. Search for "productivity software market size 2024", "SaaS productivity tools market report"
2. Look for reports from Gartner, IDC, Statista, or similar research firms
3. Find growth projections for 2025-2030

Success Criteria:
- PASS: $50B+ market size (validates large opportunity)
- FAIL: <$50B market (niche too small)

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: Market size data with sources
- Growth Rate: CAGR projection if available
- Summary: 2-3 sentence conclusion about market opportunity
```

---

### Q10: Small Business Automation SaaS Competitor Count

```
PROMPT FOR RSRCH AGENT:

Research Question: How many SaaS companies serve the "small business automation" niche?

Search Strategy:
1. Search for "small business automation SaaS", "zapier alternatives", "workflow automation tools"
2. Count distinct companies offering automation to SMBs
3. Look for lists like "Top 20 automation tools for small business"

Success Criteria:
- PASS: 20+ competitors (validates market demand - not too early)
- FAIL: <10 competitors (market unproven) OR >100 competitors (too crowded)

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: List of 20+ competitors with URLs
- Market Maturity: Assessment of competition level (early/growing/mature/saturated)
- Summary: 2-3 sentence conclusion about market validation
```

---

## Category 3: Competitive Positioning (Q11-Q15)

### Q11: Pre-Built Positioning Gap

```
PROMPT FOR RSRCH AGENT:

Research Question: Do Zapier alternatives position as "easier" or "pre-built"?

Search Strategy:
1. Review marketing messaging for 10-15 Zapier alternatives
2. Search for "Zapier alternative pre-built", "ready-made automation", "no-code automation marketplace"
3. Analyze positioning statements on competitor homepages

Success Criteria:
- PASS: 0-2 competitors using "pre-built" positioning (validates empty niche)
- FAIL: 3+ competitors already own "pre-built" messaging

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: List competitors and their positioning statements
- Gap Analysis: How many use "easier" vs "pre-built" vs other angles
- Summary: 2-3 sentence conclusion about positioning whitespace
```

---

### Q12: AI Agent Marketplace Competition

```
PROMPT FOR RSRCH AGENT:

Research Question: Are there existing "AI agent marketplaces" we compete with?

Search Strategy:
1. Search for "AI agent marketplace", "buy AI agents", "pre-built AI automation marketplace"
2. Look for platforms selling ready-made agents (not just tools to build agents)
3. Filter for self-service marketplaces (not consulting/agency services)

Success Criteria:
- PASS: 0-3 direct competitors (validates whitespace without being too early)
- FAIL: 5+ direct competitors (market saturated) OR 0 competitors (no demand validation)

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: List of direct competitors with URLs and offerings
- Differentiation: How they differ from our model (if any exist)
- Summary: 2-3 sentence conclusion about competitive landscape
```

---

### Q13: Zapier Net Promoter Score

```
PROMPT FOR RSRCH AGENT:

Research Question: What is Zapier's Net Promoter Score (NPS)?

Search Strategy:
1. Search for "Zapier NPS", "Zapier net promoter score", "Zapier customer satisfaction"
2. Look for third-party review sites (G2, Capterra, TrustPilot) for satisfaction ratings
3. Calculate proxy NPS from review distributions if official NPS unavailable

Success Criteria:
- PASS: NPS <50 or average rating <4.0/5.0 (room for improvement)
- FAIL: NPS >60 or average rating >4.5/5.0 (high satisfaction = harder to compete)

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: NPS score or review ratings with sources
- Common Complaints: Top 3-5 negative themes from reviews
- Summary: 2-3 sentence conclusion about customer satisfaction gap
```

---

### Q14: Zapier Pricing Frustration

```
PROMPT FOR RSRCH AGENT:

Research Question: Do users complain about Zapier's task limits and pricing tiers?

Search Strategy:
1. Search Reddit/forums for "Zapier pricing expensive", "Zapier task limits", "Zapier too expensive"
2. Look for users discussing switching away from Zapier due to cost
3. Find discussions about hitting task limits and needing to upgrade

Success Criteria:
- PASS: 10+ complaints about Zapier pricing/limits
- FAIL: <10 complaints or users say pricing is fair

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: Top 10 pricing complaint quotes with URLs
- Switching Triggers: What causes users to leave Zapier
- Summary: 2-3 sentence conclusion about pricing vulnerability
```

---

### Q15: Done-For-You Automation Services

```
PROMPT FOR RSRCH AGENT:

Research Question: Are there successful "done-for-you" automation services?

Search Strategy:
1. Search for "done for you automation service", "automation agency", "zapier consultant"
2. Find pricing for these services (should be $2K-10K for setup)
3. Look for case studies or reviews showing demand

Success Criteria:
- PASS: 5+ agencies charging $2K-10K for automation setup (validates market for not-DIY)
- FAIL: <5 agencies or pricing is <$1K (no premium for done-for-you)

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: List 5+ agencies with pricing and service descriptions
- Average Pricing: Typical cost for automation setup services
- Summary: 2-3 sentence conclusion about productized opportunity
```

---

## Category 4: Product Validation (Q16-Q18)

### Q16: Launch Agent Demand Ranking

```
PROMPT FOR RSRCH AGENT:

Research Question: Which of our 5 launch agents has the highest search demand?

Search Strategy:
1. Find search volume or discussion volume for each use case:
   - "automate expense tracking" + variations
   - "automate meeting notes" + variations
   - "email newsletter digest" + variations
   - "social media repurposing" + variations
   - "document organization automation" + variations
2. Use Google Trends, keyword tools, or Reddit discussion counts as proxy
3. Rank by demand (highest to lowest)

Success Criteria:
- PASS: At least 2 agents have 500+ monthly searches or significant demand signals
- FAIL: <2 agents have measurable demand

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: Demand metrics for all 5 agents (ranked)
- Top 2 Winners: Highest demand agents to prioritize
- Bottom 2 Losers: Consider cutting if very low demand
- Summary: 2-3 sentence conclusion about agent prioritization
```

---

### Q17: Agent Pricing Competitiveness

```
PROMPT FOR RSRCH AGENT:

Research Question: Do existing solutions for our 5 agents cost more or less than $500/month?

Search Strategy:
1. For each of the 5 use cases, find existing SaaS solutions:
   - Expense tracking automation tools
   - Meeting transcription/summary tools (Otter.ai, Fireflies.ai)
   - Email digest/newsletter tools
   - Social media scheduling/repurposing tools (Buffer, Hootsuite)
   - Document management/organization tools
2. Record pricing for each competitor
3. Calculate average pricing per category

Success Criteria:
- PASS: Comparable tools priced at $200-800/month (our $500 is competitive)
- FAIL: Most tools priced at <$100/month (we're too expensive)

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: List competitors for each agent category with pricing
- Pricing Range: Min-Max for each category
- Our Position: Are we high/mid/low relative to competition
- Summary: 2-3 sentence conclusion about pricing competitiveness
```

---

### Q18: Easy Setup Demand

```
PROMPT FOR RSRCH AGENT:

Research Question: Are people searching for "1-click activation" or "easy setup" for automation?

Search Strategy:
1. Search for automation + "easy setup", "one click", "no code", "simple setup", "plug and play"
2. Look for frustration with complex setup processes
3. Find demand for low-friction activation

Success Criteria:
- PASS: High search volume or discussion volume for ease-of-use terms
- FAIL: Little evidence people prioritize easy setup

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: Search volume or discussion quotes emphasizing setup simplicity
- Summary: 2-3 sentence conclusion about setup as differentiator
```

---

## Category 5: Business Model Validation (Q19-Q20)

### Q19: SaaS Marketplace Conversion Rates

```
PROMPT FOR RSRCH AGENT:

Research Question: Do SaaS marketplaces (like Shopify App Store) have high conversion rates?

Search Strategy:
1. Search for "Shopify App Store conversion rate", "SaaS marketplace install rate", "app marketplace statistics"
2. Look for data on browse-to-install conversion
3. Find industry benchmarks for marketplace models

Success Criteria:
- PASS: 5-10%+ conversion from browse to install (validates marketplace model)
- FAIL: <5% conversion (marketplace model inefficient)

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: Conversion rate data with sources
- Benchmark: Industry average for SaaS marketplaces
- Summary: 2-3 sentence conclusion about marketplace viability
```

---

### Q20: $100/Month Impulse Purchase for Solo Users

```
PROMPT FOR RSRCH AGENT:

Research Question: Is $100/month considered "impulse purchase" for solo freelancers?

Search Strategy:
1. Search for "small business purchase approval threshold", "impulse purchase limit SaaS", "credit card limit small business"
2. Look for discussions about what dollar amount requires manager approval vs autonomous purchase
3. Find data on average SaaS spending per employee or per business

Success Criteria:
- PASS: $100/month = impulse purchase territory for solo users (no approval needed, self-service viable)
- FAIL: $100/month typically requires approval process (would need sales team)

Output Format:
- Verdict: PASS/FAIL
- Confidence: High/Medium/Low
- Evidence: Purchase threshold data with sources
- Approval Triggers: At what $ amount do SMBs require manager signoff
- Summary: 2-3 sentence conclusion about self-service feasibility
```

---

## Execution Checklist

### Before Starting:
- [ ] Ensure rsrch agent is available and configured
- [ ] Create results tracking spreadsheet (20 rows for questions)
- [ ] Allocate 30-45 minutes for parallel execution

### During Execution:
- [ ] Copy each prompt EXACTLY as written
- [ ] Launch prompts in parallel batches (5 categories)
- [ ] Record PASS/FAIL + Confidence for each question
- [ ] Save evidence/quotes for documentation

### After Execution:
- [ ] Count total PASS results (need 15/20 minimum)
- [ ] Calculate confidence score (High = 3, Med = 2, Low = 1)
- [ ] Document findings in `phase2-validation-results.md`
- [ ] Make GO/NO-GO decision

---

## Scoring Rubric

**GO Decision Criteria:**
- ✅ Minimum: 15/20 PASS (75% confidence)
- ✅ Strong: 18/20 PASS (90% confidence)
- ✅ All Category 1 (Pain) must pass (critical)
- ✅ At least 3/5 Category 2 (Market) must pass
- ✅ At least 3/5 Category 3 (Competition) must pass

**NO-GO Decision Criteria:**
- ❌ <15/20 PASS (insufficient validation)
- ❌ Category 1 (Pain) has 2+ failures (no market need)
- ❌ Category 2 (Market) has 3+ failures (TAM too small)
- ❌ Category 3 shows 5+ direct competitors with "pre-built" positioning

---

**Ready to execute:** Copy prompts and run rsrch agent in parallel for fastest results.
