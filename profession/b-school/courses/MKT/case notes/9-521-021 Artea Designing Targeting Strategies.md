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
> [To be filled during/after class discussion]

### My Participation
- **Times Spoken**: 0
- **Cold Called**: No

### Key Insights from Discussion
-

### Alternative Perspectives
-

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
