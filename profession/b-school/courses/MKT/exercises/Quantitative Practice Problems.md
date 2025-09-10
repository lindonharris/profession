# Marketing Quantitative Analysis - Practice Problems & Solutions

**Based on:** HBS Note N2-525-014  
**Created for:** MKT Course - Professor Chip Bergh  
**Difficulty Levels:** ⭐ Basic | ⭐⭐ Intermediate | ⭐⭐⭐ Advanced

---

## 📊 MARKET SIZING PROBLEMS

### Problem 1: Food Delivery App ⭐
You're launching a food delivery app in Boston. Given:
- Boston population: 700,000
- 60% are adults
- 40% of adults order food delivery
- Average 2 orders/month
- Average order value: $35
- Your commission: 20%
- Target market share: 5%

**Calculate:** Annual revenue potential

<details>
<summary>Solution</summary>

**Bottom-up approach:**
- Adult population: 700,000 × 0.60 = 420,000
- Food delivery users: 420,000 × 0.40 = 168,000
- Annual orders: 168,000 × 2 × 12 = 4,032,000
- Gross merchandise value: 4,032,000 × $35 = $141,120,000
- Total commission pool: $141,120,000 × 0.20 = $28,224,000
- Your revenue (5% share): $28,224,000 × 0.05 = **$1,411,200**

</details>

### Problem 2: Electric Scooter Market ⭐⭐
Estimate the TAM for electric scooters in the US using top-down approach:
- US urban population: 250M
- Daily commuters: 60%
- Commute < 5 miles: 30%
- Would consider scooter: 10%
- Average scooter price: $500
- Replacement every 3 years

**Calculate:** Annual market size

<details>
<summary>Solution</summary>

**Top-down approach:**
- Urban population: 250M
- Commuters: 250M × 0.60 = 150M
- Short commuters: 150M × 0.30 = 45M
- Potential buyers: 45M × 0.10 = 4.5M
- Annual buyers (3-year cycle): 4.5M / 3 = 1.5M
- Annual market: 1.5M × $500 = **$750M**

</details>

---

## 💰 CUSTOMER VALUE PROBLEMS

### Problem 3: SaaS vs. On-Premise Software ⭐⭐
Compare TEV for a company choosing between:

**Option A: On-Premise**
- License: $50,000
- Annual maintenance: $10,000
- IT staff cost: $30,000/year
- Lifespan: 5 years

**Option B: SaaS**
- Monthly subscription: $2,000
- No maintenance or IT costs
- 5-year comparison

**Calculate:** Which has better TEV?

<details>
<summary>Solution</summary>

**Option A (On-Premise) - 5 years:**
- Initial license: $50,000
- Maintenance: $10,000 × 5 = $50,000
- IT costs: $30,000 × 5 = $150,000
- Total: $250,000

**Option B (SaaS) - 5 years:**
- Monthly: $2,000 × 12 × 5 = $120,000
- Total: $120,000

**TEV of SaaS** = $250,000 - $120,000 = **$130,000**
SaaS provides $130,000 in value over 5 years.

</details>

---

## 📈 CUSTOMER ACQUISITION PROBLEMS

### Problem 4: Instagram Advertising ⭐⭐
Your DTC jewelry brand runs Instagram ads:
- Monthly budget: $20,000
- CPM: $12
- CTR: 1.5%
- Conversion rate: 3%
- AOV: $150
- Variable cost: $50

**Calculate:** CAC, ROAS, ROI, and profitability

<details>
<summary>Solution</summary>

**Step 1: Calculate metrics**
- Impressions: ($20,000/$12) × 1,000 = 1,666,667
- Clicks: 1,666,667 × 0.015 = 25,000
- Orders: 25,000 × 0.03 = 750
- Revenue: 750 × $150 = $112,500
- Gross profit: 750 × ($150-$50) = $75,000

**Step 2: Key metrics**
- CAC = $20,000 / 750 = **$26.67**
- ROAS = $112,500 / $20,000 = **5.63**
- ROI = ($75,000 - $20,000) / $20,000 = **275%**
- Net profit = $75,000 - $20,000 = **$55,000**

</details>

### Problem 5: Breakeven for Free Shipping ⭐⭐⭐
Your e-commerce store considers offering free shipping:
- Current conversion rate: 2%
- Average order: $80
- Margin: 40%
- Shipping cost: $8
- Marketing cost to promote: $5,000/month
- Current monthly visitors: 50,000

**Question:** What conversion rate is needed to breakeven?

<details>
<summary>Solution</summary>

**Current situation:**
- Orders: 50,000 × 0.02 = 1,000
- Margin per order: $80 × 0.40 = $32
- Monthly profit: 1,000 × $32 = $32,000

**With free shipping:**
- New margin: $32 - $8 = $24
- Need to maintain $32,000 profit + cover $5,000 marketing
- Target profit: $37,000
- Orders needed: $37,000 / $24 = 1,542
- Conversion needed: 1,542 / 50,000 = **3.08%**

**Increase needed:** From 2% to 3.08% = **54% improvement**

</details>

---

## 🔄 CUSTOMER LIFETIME VALUE PROBLEMS

### Problem 6: Subscription Box LTV ⭐⭐
A beauty subscription box has:
- Monthly price: $25
- Monthly COGS: $12
- Monthly retention: 90%
- CAC: $45

**Calculate:** LTV, LTV/CAC ratio, and months to payback

<details>
<summary>Solution</summary>

**Monthly calculations:**
- Monthly margin: $25 - $12 = $13
- Monthly churn: 1 - 0.90 = 0.10
- LTV = $13 / 0.10 = **$130**
- LTV/CAC = $130 / $45 = **2.89**
- Payback = $45 / $13 = **3.5 months**

</details>

### Problem 7: Improving Unit Economics ⭐⭐⭐
Your SaaS company has:
- Monthly revenue per user: $100
- Gross margin: 80%
- Annual retention: 85%
- CAC: $500

You can either:
A) Reduce CAC by 20% (optimize marketing)
B) Improve retention to 90% (better onboarding)
C) Increase price 10% (lose 5% of customers)

**Question:** Which option maximizes LTV/CAC?

<details>
<summary>Solution</summary>

**Current state:**
- Annual margin: $100 × 12 × 0.80 = $960
- LTV = $960 / (1-0.85) = $6,400
- LTV/CAC = $6,400 / $500 = 12.8

**Option A (Reduce CAC 20%):**
- New CAC: $400
- LTV/CAC = $6,400 / $400 = **16.0**

**Option B (Retention to 90%):**
- New LTV = $960 / (1-0.90) = $9,600
- LTV/CAC = $9,600 / $500 = **19.2**

**Option C (Price +10%, Volume -5%):**
- New revenue: $110 × 0.95 = $104.50
- New margin: $104.50 × 12 × 0.80 = $1,003.20
- LTV = $1,003.20 / 0.15 = $6,688
- LTV/CAC = $6,688 / $500 = **13.4**

**Best option: B (Improve retention) with LTV/CAC of 19.2**

</details>

---

## 🏪 CHANNEL ECONOMICS PROBLEMS

### Problem 8: Retail vs. DTC Decision ⭐⭐
Your sustainable water bottle company evaluates channels:

**Retail channel:**
- MSRP: $40
- Retailer margin: 40%
- Your COGS: $8

**DTC channel:**
- Sell at MSRP: $40
- COGS: $8
- Shipping: $5
- CAC: $15

**Question:** Which channel is more profitable per unit?

<details>
<summary>Solution</summary>

**Retail channel:**
- Retailer takes: $40 × 0.40 = $16
- You receive: $40 - $16 = $24
- Your margin: $24 - $8 = **$16**

**DTC channel:**
- Revenue: $40
- Total costs: $8 + $5 + $15 = $28
- Your margin: $40 - $28 = **$12**

**Retail is more profitable by $4 per unit**

</details>

### Problem 9: Trade Promotion Pass-Through ⭐⭐⭐
Coca-Cola offers retailers $2 off per 12-pack case:
- Current retail price: $6.00
- Retailer margin: 25%
- Retailer's current margin per case: $1.50

**Question:** What sales increase does retailer need to justify passing the full discount to consumers?

<details>
<summary>Solution</summary>

**Current state:**
- Margin: $6.00 × 0.25 = $1.50
- COGS: $6.00 - $1.50 = $4.50

**With $2 manufacturer discount:**
- New COGS: $4.50 - $2.00 = $2.50

**Option 1: Keep price, pocket discount**
- Margin: $6.00 - $2.50 = $3.50
- Margin increase: $3.50/$1.50 = 133% increase

**Option 2: Pass full discount**
- New price: $4.00
- New margin: $4.00 - $2.50 = $1.50 (same)
- Price reduction: $2/$6 = 33%

**Retailer needs 133% volume increase to justify passing discount**
(Unlikely, so retailer will probably pocket most of it)

</details>

---

## 💲 PRICING STRATEGY PROBLEMS

### Problem 10: Price Elasticity Calculation ⭐
Last month you sold 10,000 units at $50. This month you raised price to $55 and sold 8,500 units.

**Calculate:** Price elasticity and interpret

<details>
<summary>Solution</summary>

- Price change: ($55-$50)/$50 = 10%
- Volume change: (8,500-10,000)/10,000 = -15%
- Elasticity = -15% / 10% = **-1.5**

**Interpretation:** For every 1% price increase, volume decreases 1.5%

</details>

### Problem 11: Optimal Pricing Decision ⭐⭐⭐
Your premium coffee brand has:
- Current price: $20/bag
- Current volume: 100,000 bags/month
- Variable cost: $8/bag
- Fixed costs: $500,000/month
- Price elasticity: -2.0

You're considering a 15% price cut to gain share.

**Question:** Should you cut price? What's the profit impact?

<details>
<summary>Solution</summary>

**Current profit:**
- Revenue: $20 × 100,000 = $2,000,000
- Variable costs: $8 × 100,000 = $800,000
- Contribution: $1,200,000
- Profit: $1,200,000 - $500,000 = **$700,000**

**With 15% price cut:**
- New price: $20 × 0.85 = $17
- Volume increase: 15% × 2.0 = 30%
- New volume: 100,000 × 1.30 = 130,000
- Revenue: $17 × 130,000 = $2,210,000
- Variable costs: $8 × 130,000 = $1,040,000
- Contribution: $1,170,000
- Profit: $1,170,000 - $500,000 = **$670,000**

**Decision: Don't cut price. Profit decreases by $30,000**

</details>

---

## 📊 MARKET SHARE PROBLEMS

### Problem 12: Diagnosing Low Market Share ⭐⭐
Your protein bar brand has 2% market share. Research shows:
- Awareness: 40%
- Trial (among aware): 20%
- Repeat (among trial): 25%

**Questions:** 
1. Calculate theoretical market share
2. What's the biggest opportunity?
3. If you double trial rate, what's new share?

<details>
<summary>Solution</summary>

1. **Theoretical share** = 0.40 × 0.20 × 0.25 = **2%** (matches actual)

2. **Biggest opportunity:** 
   - Awareness is lowest at 40%
   - If doubled to 80%: Share = 0.80 × 0.20 × 0.25 = **4%**

3. **Double trial rate (to 40%):**
   - New share = 0.40 × 0.40 × 0.25 = **4%**

**Both awareness and trial offer equal opportunity to double share**

</details>

---

## 🎯 COMPREHENSIVE CASE PROBLEM

### Problem 13: New Product Launch Decision ⭐⭐⭐
You're launching a smart home security system. Analyze the opportunity:

**Market data:**
- US households: 130M
- Suburban homes: 40%
- Security concern (high): 30%
- Tech-savvy: 50%
- Would consider smart security: 20%

**Product economics:**
- Device price: $299
- Monthly monitoring: $29
- Device COGS: $120
- Monthly service cost: $5
- Installation cost: $50

**Marketing plan:**
- Digital CAC: $150
- Expected annual retention: 85%

**Questions:**
1. Calculate TAM (year 1 device sales)
2. Calculate customer LTV
3. What's the LTV/CAC ratio?
4. Is this an attractive opportunity?

<details>
<summary>Solution</summary>

**1. TAM Calculation:**
- Suburban homes: 130M × 0.40 = 52M
- High security concern: 52M × 0.30 = 15.6M
- Tech-savvy: 15.6M × 0.50 = 7.8M
- Would consider: 7.8M × 0.20 = 1.56M households
- TAM = 1.56M × $299 = **$466M** (devices)

**2. LTV Calculation:**
- Device margin: $299 - $120 - $50 = $129 (one-time)
- Monthly service margin: $29 - $5 = $24
- Annual service margin: $24 × 12 = $288
- Service LTV: $288 / (1-0.85) = $1,920
- Total LTV: $129 + $1,920 = **$2,049**

**3. LTV/CAC Ratio:**
- LTV/CAC = $2,049 / $150 = **13.7**

**4. Attractiveness:**
- ✅ Large TAM ($466M devices + recurring revenue)
- ✅ Excellent LTV/CAC ratio (13.7 >> 3)
- ✅ High margins on recurring revenue
- ✅ Strong unit economics

**This is a very attractive opportunity**

</details>

---

## 📝 QUICK DRILL PROBLEMS

### Set A: Mental Math ⭐
1. If margin is 40% and you cut price 10%, what volume increase do you need? **Answer: 33%**
2. Monthly retention 95%, what's annual retention? **Answer: 54% (0.95^12)**
3. LTV is $200, CAC is $50, what's ROI? **Answer: 300%**
4. CTR is 2%, conversion is 5%, what's overall rate? **Answer: 0.1%**
5. If churn is 20%, what's average customer life? **Answer: 5 years**

### Set B: Rule of Thumb ⭐
1. ROAS of 2.5 with 40% margin, is it profitable? **Answer: Yes (needs ROAS > 2.5 to be profitable)**
2. Price elasticity is -3, should you raise price? **Answer: No (highly elastic)**
3. LTV/CAC is 2.2 for SaaS, good enough? **Answer: No (want > 3)**
4. Retailer margin 50%, your COGS 30%, your margin? **Answer: 20%**
5. CAC is $100, margin $25/month, payback period? **Answer: 4 months**

---

## 🎓 CASE INTERVIEW TIPS

### Structure Your Approach
1. **Clarify** assumptions and constraints
2. **Calculate** systematically (show your work)
3. **Sanity check** your answers
4. **Conclude** with recommendation

### Common Traps to Avoid
- Mixing monthly and annual figures
- Using revenue instead of margin
- Forgetting about retention/churn
- Ignoring fixed costs in breakeven
- Double-counting in market sizing

### Quick Estimation Techniques
- Population pyramids for demographics
- 80/20 rule for segmentation
- 2-3% conversion rates for digital
- 10-30% retail margins typical
- 70-90% retention for good subscription businesses

---

*Practice these problems before each case discussion. Focus on speed and accuracy for basic problems, understanding for advanced ones.*