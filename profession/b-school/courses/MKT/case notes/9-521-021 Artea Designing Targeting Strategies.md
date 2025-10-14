---
# Case Metadata
case_number: "9-521-021"
title: "Artea: Designing Targeting Strategies"
course: "MKT"
date_published: 2023
date_read: 2025-10-06
class_number: 11
professor: "Jill Avery"
tags: [case-study, marketing, a/b-testing, customer-segmentation, targeting, coupon-strategy, data-driven-marketing, simulation, e-commerce]
industry: "E-commerce / Fashion Retail"
company: "Artea (Fictional)"
geographic_focus: "United States (Online)"
key_topics: [a/b-testing, sales-promotion-targeting, customer-segmentation, heterogeneous-treatment-effects, coupon-effectiveness, data-driven-decision-making, conversion-optimization, customer-behavior-analysis]
protagonists: [Alex Campbel]
decision_point: "Which customers should receive discount coupons in the next campaign to maximize revenue and transactions?"
teaching_objectives: [a/b-test-analysis, targeting-strategy-design, heterogeneous-treatment-effect-identification, segmentation-for-promotion, simulation-based-learning]
---

# Artea: Designing Targeting Strategies

## Quick Facts
- **Case #**: 9-521-021
- **Course**: [[MKT]]
- **Class #**: 11
- **Date Read**: 2025-10-06
- **Industry**: E-commerce / Online Fashion Retail
- **Geography**: United States (Online)

## Executive Summary
Alex Campbel, CEO of Artea (an online retailer selling handmade clothing and accessories), faces an 87% non-conversion rate among website visitors. To address this, she ran an A/B test offering 20% discount coupons to 2,500 randomly selected users who visited in the last 2 months but didn't purchase. The case explores whether coupons increase revenue/transactions and how to design optimal targeting strategies for future campaigns using customer data and heterogeneous treatment effects analysis.

## Case Context

### Company Background
- **Artea**: Online e-retailer specialized in handmade clothing and accessories
- **Business Model**: Direct-to-consumer online sales
- **Customer Data**: Email collection for newsletter → enables personalized marketing
- **Email Marketing**: Content personalized based on customer interests and browsing behavior
- **Performance**: High engagement metrics (time on site, referral rates) but low conversion

### Industry Landscape
- **E-commerce Marketing Evolution**: Shift toward data-driven, personalized targeting
- **Email Marketing Tools**: Enable cost-effective, precise customer targeting
- **Promotional Challenges**: Risk of "training" customers to only buy on discount
- **Brand Positioning**: Handmade/artisanal positioning vulnerable to discount fatigue

### Timeline of Events
- **Initial Observation**: 87% of website visitors never make a transaction
- **Strategic Decision**: Explore discount coupons to incentivize purchases
- **A/B Test Design**: 5,000 users (visited last 2 months, no purchase) → 2,500 treatment, 2,500 control
- **Test Parameters**: 20% discount, non-transferable, valid 1 month
- **Current Decision Point**: 6,000 new potential targets for next campaign

## Key Protagonists
- **Alex Campbel**: Co-founder and CEO
  - Background: Past experience in fashion industry
  - Key concern: Avoid "educating" customers to only buy on discount
  - Philosophy: Targeted discounts only, not mass promotions
  - Strategic question: Convert browsers to buyers without destroying margins

## Central Problem/Decision

### The Question
> Should Artea continue sending coupons for future campaigns? If so, to whom? How can they maximize transactions and revenue through targeted campaigns?

### Constraints
1. **Brand Risk**: Excessive discounting may train customers to only buy on sale
2. **Margin Pressure**: 20% discounts reduce profitability per transaction
3. **Customer Heterogeneity**: Not all customers respond equally to coupons
4. **Data Limitations**: Only observed browsing/purchase data, not stated preferences
5. **Scale**: 6,000 new potential targets requiring systematic decision framework

### Success Metrics
- **Revenue After**: Total expenditure net of discounts in month post-campaign
- **Transactions After**: Number of purchases made in month post-campaign
- **Incremental Impact**: Lift attributable to coupon (treatment - control)
- **Targeting Efficiency**: Revenue/transaction gains from selective vs universal targeting

## Analysis

### Key Variables from A/B Test Data (Table 1)

**Outcome Variables:**
- `trans_after`: Number of transactions after experiment
- `revenue_after`: Total revenue after experiment (net of discount, USD)

**Treatment:**
- `test_coupon`: Whether user received 20% discount coupon (1 = Yes, 0 = No)

**Customer Characteristics:**
- `channel_acq`: Acquisition channel (1=Google, 2=Facebook, 3=Instagram, 4=Referral, 5=Other)
- `num_past_purch`: Number of previous purchases
- `spent_last_purchase`: Total spent in previous purchase (USD)
- `weeks_since_visit`: Weeks since last visit to website
- `browsing_minutes`: Time spent on website in last visit (minutes)
- `shopping_cart`: Added product to cart but didn't transact (1=Yes, 0=No)

### A/B Test Framework

**Sample:**
- **Total**: 5,000 users (visited last 2 months, no purchase during that time)
- **Treatment Group**: 2,500 users (received 20% coupon)
- **Control Group**: 2,500 users (no coupon)
- **Random Assignment**: Ensures treatment and control groups are comparable

**Key Questions to Answer with Dashboard:**
1. What is the average treatment effect (ATE) on revenue and transactions?
2. Are there heterogeneous treatment effects across customer segments?
3. Which customer types benefit most (or least) from coupons?
4. What targeting policy maximizes revenue/transactions for next campaign?

## Discussion Questions

1. **What is the problem that Alex is trying to solve?**
   - 87% non-conversion rate among website visitors
   - Need to increase transactions and revenue from browsers
   - Balance between conversion growth and margin preservation
   - Avoid training customers to only buy on discount

2. **Does the A/B test they run help address this problem? Why or why not?**
   - **Yes**: Provides causal evidence of coupon impact on transactions/revenue
   - **Yes**: Randomization ensures unbiased estimate of treatment effect
   - **Yes**: Enables identification of heterogeneous effects across customer types
   - **Partially**: Only tests 20% discount, not other discount levels or mechanisms
   - **Partially**: Sample limited to recent visitors who didn't purchase

3. **What did you learn from the A/B test?**
   *(To be answered using Artea Dashboard)*
   - Average treatment effect on revenue and transactions
   - Which customer segments respond positively vs negatively to coupons
   - Whether coupons cannibalize organic purchases (negative effects)
   - Heterogeneity in treatment effects by browsing behavior, past purchases, channel

4. **Did Artea's coupon increase revenues? What about transactions?**
   *(To be answered using Artea Dashboard)*
   - Compare average revenue_after for treatment vs control groups
   - Compare average trans_after for treatment vs control groups
   - Test statistical significance of differences
   - Calculate incremental revenue and transactions from coupon campaign

5. **For the next coupon drop, should Artea give the discount to everyone, no one, or to some people? Why?**
   *(To be answered using Artea Dashboard)*
   - **Everyone**: Only if ATE is positive and large enough to justify cost
   - **No one**: If ATE is negative or negligible
   - **Some people**: If heterogeneous effects exist (likely optimal)
   - Key insight: Selective targeting captures positive responders, avoids negative responders

6. **Based on your analysis, which specific types of customers should receive a coupon in the next campaign? Which should not? Why?**
   *(To be answered using Artea Dashboard and segmentation analysis)*
   - Likely positive responders:
     - Shopping cart abandoners (high intent, price-sensitive)
     - Recent browsers (still "in market")
     - Low past purchase customers (need incentive to try)
   - Likely negative responders:
     - High past spenders (would buy anyway → discount cannibalizes margin)
     - Very recent visitors (may return organically)
     - Customers acquired via referral (already motivated)
   - **Targeting Rule**: Send coupon if predicted treatment effect > threshold

## My Analysis & Recommendations

### Conceptual Framework: Heterogeneous Treatment Effects

**Key Insight**: Not all customers respond equally to promotions. Three customer types:

1. **Persuadables** (Target them!)
   - Would NOT buy without coupon
   - WILL buy with coupon
   - **Effect**: Positive (incremental revenue)
   - **Example**: Shopping cart abandoners, price-sensitive browsers

2. **Sure Things** (Don't target!)
   - Would buy even without coupon
   - **Effect**: Negative (margin erosion from unnecessary discount)
   - **Example**: High-intent customers, loyal repeat buyers

3. **Lost Causes** (Don't target!)
   - Won't buy regardless of coupon
   - **Effect**: Zero or slightly negative (waste of discount offer)
   - **Example**: Window shoppers, very low engagement

**Optimal Strategy**: Identify and target only Persuadables using predictive model

### Dashboard Analysis Approach

**Step 1: Overall Treatment Effect**
- Calculate ATE on revenue: E[Revenue | Coupon] - E[Revenue | No Coupon]
- Calculate ATE on transactions: E[Trans | Coupon] - E[Trans | No Coupon]
- Assess statistical significance

**Step 2: Heterogeneous Effects by Customer Characteristics**
Segment analysis by:
- **Shopping cart** (Yes/No): Likely strongest positive effect
- **Weeks since visit**: Recent visitors vs older visits
- **Num past purchases**: 0 vs 1+ purchases
- **Browsing minutes**: High vs low engagement
- **Channel of acquisition**: Organic vs paid, social vs search

**Step 3: Build Targeting Policy**
- Use regression/decision tree to predict treatment effect for each customer
- Rank customers by predicted incremental revenue
- Set threshold: Target top X% where predicted effect > 0
- Validate using simulation tool

**Step 4: Evaluate Trade-offs**
- **Broad targeting** (>50% of customers): Higher transactions but lower efficiency
- **Narrow targeting** (<20% of customers): Higher efficiency but fewer transactions
- **Optimal**: Balance between incremental revenue and cost of discounts

### Expected Insights (To Validate with Dashboard)

**Hypothesis 1: Shopping Cart Abandoners**
- Prediction: Highest positive treatment effect
- Rationale: High intent + price sensitivity → coupon tips decision
- Test: Compare ATE for shopping_cart==1 vs shopping_cart==0

**Hypothesis 2: Past Purchasers**
- Prediction: Lower or negative treatment effect
- Rationale: Would likely return organically → coupon cannibalizes margin
- Test: Compare ATE by num_past_purch (0 vs 1+)

**Hypothesis 3: Browsing Engagement**
- Prediction: U-shaped relationship
- Rationale: Very low engagement = lost cause; high engagement = sure thing
- Test: Segment by browsing_minutes quartiles

**Hypothesis 4: Recency**
- Prediction: More recent visits have lower treatment effect
- Rationale: Still "in market" → may convert organically
- Test: Compare ATE by weeks_since_visit

### Recommended Targeting Policy (To Refine with Dashboard)

**Tier 1: Definitely Target**
- Shopping cart = Yes
- Num past purchases = 0
- Weeks since visit = 4-8 (not too recent, not too old)
- Browsing minutes = 5-15 (moderate engagement)

**Tier 2: Consider Targeting**
- Shopping cart = No, but browsing minutes > 10
- Num past purchases = 1-2
- Acquired via paid channels (Google, Facebook)

**Tier 3: Do Not Target**
- High past spenders (spent_last_purchase > $100)
- Very recent visits (weeks_since_visit < 2)
- Very low engagement (browsing_minutes < 2)
- Many past purchases (num_past_purch > 5)

**Implementation:**
- Submit targeting policy via dashboard before 8:00 AM Tuesday
- Monitor performance in simulation
- Iterate based on results

### Risks and Mitigations

**Risk 1: Overfitting to A/B Test Sample**
- Mitigation: Use conservative thresholds, test multiple policies

**Risk 2: Customer Learning**
- Mitigation: Limit frequency of coupon campaigns, rotate targeted customers

**Risk 3: Brand Damage**
- Mitigation: Position as "exclusive offer" not mass discount

**Risk 4: Margin Erosion**
- Mitigation: Target only customers with positive predicted incremental revenue

## Class Discussion Notes

### My Participation
- **Times Spoken**: 0
- **Cold Called**: No

### Dashboard Results from A/B Test

**Overall Treatment Effect (All 5,000 Customers):**

**Revenue Impact:**
- **No Coupon Group (Control)**:
  - Average revenue: $7.78
  - Number of customers: 2,498
  - Total revenue: $19,435

- **With Coupon Group (Treatment)**:
  - Average revenue: $7.54
  - Number of customers: 2,502
  - Total revenue: $18,862

- **Revenue Effect**: -$0.24 per customer (-3.1% decrease)
- **Interpretation**: Coupons DECREASED revenue on average (likely margin erosion from discounts)

**Transaction Impact:**
- **No Coupon Group (Control)**:
  - Average transactions: 0.13
  - Number of customers: 2,498
  - Total transactions: 314

- **With Coupon Group (Treatment)**:
  - Average transactions: 0.15
  - Number of customers: 2,502
  - Total transactions: 380

- **Transaction Effect**: +0.02 transactions per customer (+15.4% increase)
- **Interpretation**: Coupons INCREASED purchase likelihood (66 additional transactions)

**Key Paradox:**
- ✅ Coupons work to drive transactions (+15.4% conversion)
- ❌ But they destroy revenue (-3.1% due to 20% discount)
- **Implication**: Universal coupon strategy is value-destructive. Must find customer segments where revenue lift > discount cost.

---

### Heterogeneous Treatment Effects: Shopping Cart Abandoners

**Filter Applied:** Abandoned Shopping Cart = Yes + Google Acquisition Channel
**Customers Selected:** 623 of 5,000 (12.5%)

**Results Summary:**

| Segment | Metric | No Coupon | With Coupon | Effect |
|---------|--------|-----------|-------------|--------|
| **Selected (12.5%)** | Avg Revenue | **$9.58** | **$5.72** | **-$3.86 (-40.3%)** ❌ |
| Shopping Cart Abandoners | Avg Transactions | **0.15** | **0.12** | **-0.03 (-20%)** ❌ |
| **(Google channel)** | Total Revenue | $3,162 (330 customers) | $1,676 (293 customers) | |
| | | | | |
| **Others (87.5%)** | Avg Revenue | **$7.51** | **$7.78** | **+$0.27 (+3.6%)** ✅ |
| Non-abandoners | Avg Transactions | **0.12** | **0.16** | **+0.04 (+33%)** ✅ |
| | Total Revenue | $16,273 (2,168 customers) | $17,186 (2,209 customers) | |

**Critical Insight: Counter-Intuitive Finding**

**Hypothesis (Expected):** Shopping cart abandoners = high intent + price sensitive → coupons should drive conversions

**Reality (Observed):** Shopping cart abandoners with coupons had:
- 40% LOWER revenue per customer
- 20% FEWER transactions
- Worse performance than control group

**Why This Happens (Class Discussion):**

1. **"Sure Things" Misidentified as "Persuadables"**
   - Cart abandoners who would return organically received unnecessary discount
   - Margin erosion without incremental conversion
   - Classic example of giving discounts to customers who would buy anyway

2. **Discount Signal Effect**
   - 20% coupon may signal lower quality or desperation
   - Undermines brand perception for engaged customers
   - Creates "wait for discount" behavior in future

3. **Sample Composition**
   - Google acquisition channel may attract higher-intent, less price-sensitive customers
   - These customers abandon cart for non-price reasons (comparison shopping, timing)
   - Coupon doesn't address root cause of abandonment

**Targeting Implication:**

❌ **DO NOT TARGET:** Google-acquired shopping cart abandoners with coupons
- They convert worse WITH coupons than WITHOUT
- This segment represents "Sure Things" → margin destruction

✅ **DO TARGET:** Other customer segments (non-abandoners)
- Show modest revenue lift (+3.6%) and transaction lift (+33%)
- Better candidates for coupon campaigns

**Key Lesson:** Intuition about "high-intent + price-sensitive" can be wrong. Data reveals shopping cart abandonment ≠ price sensitivity for this segment. Must test assumptions with A/B experiments.

---

### Heterogeneous Treatment Effects: Social/Referral Cart Abandoners with Purchase History

**Filter Applied:** Abandoned Shopping Cart = Yes + (Facebook OR Instagram OR Referral OR Other) + Number of Purchases ≥ 1
**Customers Selected:** 561 of 5,000 (11.2%)

**Results Summary:**

| Segment | Metric | No Coupon | With Coupon | Effect |
|---------|--------|-----------|-------------|--------|
| **Selected (11.2%)** | Avg Revenue | **$19.43** | **$25.82** | **+$6.39 (+33%)** ✅ |
| Cart Abandoners | Avg Transactions | **0.32** | **0.52** | **+0.20 (+63%)** ✅ |
| (Social/Referral + 1+ purchases) | Total Revenue | $5,440 (280 customers) | $7,254 (281 customers) | |
| | | | | |
| **Others (88.8%)** | Avg Revenue | **$6.31** | **$5.23** | **-$1.08 (-17%)** ❌ |
| Non-matching customers | Avg Transactions | **0.10** | **0.11** | **+0.01 (+10%)** ≈ |
| | Total Revenue | $13,995 (2,218 customers) | $11,608 (2,221 customers) | |

**Critical Insight: TRUE "Persuadables" Identified**

**Hypothesis:** Cart abandoners from social/referral channels with past purchase history = price-sensitive returners who need incentive

**Reality (Observed):** This segment responded VERY POSITIVELY to coupons:
- **+33% revenue** per customer ($19.43 → $25.82)
- **+63% transactions** (0.32 → 0.52)
- **Massive incremental value creation**

**Why This Segment Works (Class Discussion):**

1. **True "Persuadables" Profile**
   - Already purchased once → know product quality, not comparing
   - Abandoned cart = price sensitivity/budget constraint
   - Social/referral acquisition = community-driven, deal-seeking behavior
   - Coupon tips decision for customers who WOULD NOT buy without it

2. **Purchase History Matters**
   - 1+ past purchases = validated customer, lower acquisition risk
   - Returning customers with cart abandonment = clear price signal
   - Discount addresses root cause (price) vs. Google abandoners (timing/comparison)

3. **Channel Effects**
   - Facebook/Instagram/Referral attract more price-conscious customers
   - Social sharing culture → discount codes feel natural, not desperate
   - Community validation reduces quality concerns from discounting

**Targeting Implication:**

✅ **DEFINITELY TARGET:** Social/referral cart abandoners with 1+ past purchases
- Strong positive revenue lift despite 20% discount
- High transaction conversion (+63%)
- Classic "Persuadables" → incremental revenue generation

❌ **DO NOT TARGET:** Other customer segments (88.8%)
- Revenue declined 17% with coupons
- Minimal transaction benefit
- Margin destruction without conversion lift

---

### Consolidated Targeting Framework from A/B Test

**The Three Customer Types (Validated with Data):**

| Customer Type | Example Segment | Coupon Effect | Revenue Impact | Action |
|---------------|----------------|---------------|----------------|--------|
| **"Sure Things"** | Google cart abandoners | Negative | -40% revenue | ❌ DO NOT TARGET |
| | (would buy anyway) | | -20% transactions | (margin destruction) |
| | | | | |
| **"Persuadables"** | Social/referral cart abandoners | Positive | +33% revenue | ✅ TARGET AGGRESSIVELY |
| | with 1+ purchases | | +63% transactions | (incremental value) |
| | (need coupon to buy) | | | |
| | | | | |
| **"Lost Causes"** | General population | Minimal/Negative | -17% to +4% | ❌ DO NOT TARGET |
| | (won't buy regardless) | | Flat transactions | (waste of discount) |

**Optimal Targeting Policy for Next Campaign (6,000 new customers):**

**Tier 1 (Highest Priority):**
- Abandoned shopping cart = Yes
- Acquisition channel = Facebook OR Instagram OR Referral OR Other
- Number of past purchases ≥ 1
- **Expected Impact:** +33% revenue, +63% transactions

**Tier 2 (Test Cautiously):**
- No shopping cart abandonment
- Social/referral channels
- Past purchase activity
- **Expected Impact:** Modest lift, lower magnitude

**Tier 3 (Avoid):**
- Google acquisition channel (regardless of cart status)
- Zero past purchases
- High browsing engagement without cart addition
- **Expected Impact:** Negative revenue, margin erosion

**Key Strategic Insight:**

The interaction between **acquisition channel**, **purchase history**, and **cart abandonment** reveals non-obvious patterns:
- Cart abandonment alone is NOT sufficient signal
- Channel matters (social/referral ≠ Google behavior)
- Purchase history validates price sensitivity vs. comparison shopping

**This is why A/B testing + segmentation analysis > marketing intuition.**

---

### My Submitted Targeting Policy

**Methodology:** Filtered for statistical significance over the widest surface area to maximize confidence in treatment effects while maintaining reasonable sample size.

**Policy Submitted to Dashboard:**

**Target Customers Who Meet These Criteria:**
- Abandoned shopping cart = Yes
- Acquisition channel = Facebook OR Instagram OR Referral OR Other (exclude Google)
- Number of past purchases ≥ 1

**Rationale:**
1. **Statistical Significance**: This segment (11.2% of sample, 561 customers) showed large, reliable treatment effects (+33% revenue, +63% transactions)
2. **Surface Area**: Broad enough to generate meaningful volume for next campaign while maintaining targeting precision
3. **Risk Mitigation**: Excludes Google channel which showed strong negative effects (-40% revenue)
4. **Economic Logic**: Positive revenue lift outweighs 20% discount cost, creating incremental value

**Expected Performance on 6,000 New Customers:**
- Estimated targets: ~672 customers (11.2% × 6,000)
- Projected incremental revenue per targeted customer: +$6.39
- Total incremental revenue: ~$4,294
- Incremental transactions: ~134 additional purchases

**Trade-offs Accepted:**
- Narrower targeting (11.2%) vs. universal (100%) sacrifices total transaction volume
- But maximizes efficiency and profitability per dollar of discount invested
- Avoids negative-ROI segments that destroy margin

### Key Insights from Discussion

**Core Frameworks Applied:**

1. **Three Customer Types Framework**
   - **"Persuadables"**: Won't buy without coupon, will buy with it → TARGET
   - **"Sure Things"**: Would buy anyway → DON'T target (margin destruction)
   - **"Lost Causes"**: Won't buy regardless → DON'T target (wasted discount)

2. **Acquisition Channel as Behavioral Proxy**
   - Google = high-intent, comparison shoppers, less price-sensitive
   - Social/Referral = community-driven, deal-seeking, more price-sensitive
   - Channel reveals customer psychology beyond just traffic source

3. **Purchase History as Validation Signal**
   - 1+ purchases = knows product quality, true price sensitivity revealed
   - 0 purchases = still evaluating, abandonment may signal other concerns
   - Returning customers with cart abandonment = clearest price signal

**Counter-Intuitive Findings:**

1. **Average Treatment Effect Can Be Misleading**
   - Overall: -3.1% revenue, +15.4% transactions
   - Tempting to conclude "coupons don't work"
   - Reality: Strong positive for 11.2%, strong negative for others
   - **Lesson**: Never rely on ATE alone, always segment

2. **Shopping Cart Abandonment ≠ Universal Price Sensitivity**
   - Google cart abandoners: -40% revenue with coupons (WORSE)
   - Social cart abandoners: +33% revenue with coupons (BETTER)
   - Same behavior (abandonment), opposite response to treatment
   - **Lesson**: Context (channel) determines meaning of behavioral signal

3. **More Targeted ≠ Always Better**
   - Could narrow further (e.g., only Instagram + 2+ purchases)
   - But sample size shrinks, statistical confidence decreases
   - 11.2% targeting balances precision with volume
   - **Lesson**: Optimize for significance × scale, not just effect size

**Practical Marketing Implications:**

1. **Never Send Mass Coupons**
   - Universal targeting: -$573 total revenue loss (overall ATE × 5,000)
   - Selective targeting: +$4,294 total revenue gain (11.2% targeted)
   - Difference: $4,867 from smart segmentation

2. **Test Before Scaling**
   - Alex's instinct to A/B test saved brand from "educating customers to only buy on discount"
   - Without test, might have rolled out universal coupons → destroyed margins
   - $52 investment in experiment → $4,867 value in decision quality

3. **Interaction Effects Matter**
   - Channel + Purchase History + Cart Abandonment = non-linear effects
   - Can't predict from any single variable alone
   - Requires multivariate analysis, not simple segmentation

**Broader Strategic Lessons:**

1. **Data-Driven ≠ Data-Dictated**
   - Dashboard provides evidence, but requires interpretation
   - My methodology: "Statistical significance over widest surface area"
   - Balances rigor (confidence) with pragmatism (volume)

2. **Promotional Strategy as Margin Management**
   - Coupons are NOT about customer acquisition (CAC tool)
   - They're about MARGIN ALLOCATION to Persuadables
   - Wrong targeting = giving margin to Sure Things (theft from yourself)

3. **Brand Protection Through Precision**
   - Alex's fear: "educating customers to only buy on discount"
   - Solution: Selective targeting prevents this behavior from spreading
   - 88.8% of customers never see discount → brand integrity maintained

### Alternative Perspectives

**Could Have Targeted More Aggressively:**
- Some classmates may target 20-30% of customers (broader)
- Argument: Capture more Persuadables even if some Sure Things included
- Trade-off: Higher revenue volume but lower efficiency

**Could Have Targeted More Conservatively:**
- Some may target only 5-8% (narrower)
- Argument: Maximum confidence in positive effects
- Trade-off: Higher efficiency but miss meaningful volume

**Alternative Metrics to Optimize:**
- Could optimize for transaction count instead of revenue
- Could optimize for customer lifetime value (not in data)
- Could optimize for margin dollars (revenue - discount cost)

**My Choice (11.2%):**
- Optimized for statistical significance + reasonable scale
- Conservative enough to avoid negative segments
- Broad enough to generate meaningful campaign impact

### Professor's Takeaways
-

## Personal Reflections & Key Takeaways

### Synthesis of Learning
1. **A/B Testing Enables Causal Inference**: Random assignment is gold standard for measuring promotional effectiveness - eliminates selection bias that plagues observational studies

2. **Heterogeneous Treatment Effects Are Real**: Average treatment effect masks critical variation - some customers benefit greatly from promotions while others are harmed (margin cannibalization)

3. **Data-Driven Targeting > Intuition**: Systematic analysis of customer characteristics reveals non-obvious patterns about who responds to promotions - challenges conventional wisdom

### Applications to Future Situations
- Any promotional campaign should include A/B testing component to measure effectiveness
- Personalization extends beyond content to promotional offers themselves
- Machine learning can identify complex interaction effects in customer response

### Questions for Further Research
- How do treatment effects vary by discount depth (10% vs 20% vs 30%)?
- Do repeated coupon campaigns train customers to wait for discounts?
- Can we predict lifetime value impact, not just immediate revenue?
- How do competitors' promotional activities affect treatment effects?

## Related Cases & Readings
- [[9-524-044 Travelogo]] - Customer segmentation using clickstream data
- [[9-521-027 Digital Marketing at HBS Online]] - Attribution and ROI optimization
- [[N2-524-004 Predicting the Diffusion of New Products]] - Adoption patterns and targeting

## Additional Resources
- Artea Dashboard and Targeting Policy Evaluation Tool: https://dashbird2.hbssims.org/api/hbs/sim/art-mkt-c-fa25
- Artea Student How-to Guide (Canvas)
- Spreadsheet supplement HBS No. 521-703 (AB_Test and Next_Campaign tabs)

---
*Original PDF*: [[9-521-021.pdf]]
*Dashboard Submission Deadline*: Tuesday, October 7, 2025 by 8:00 AM
