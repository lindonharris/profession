# AfterQuery Training Methodology

## Overview
Notes from onboarding primer on model training approach for AI finance evaluation.

## Training Process

**Training Process Diagram:**
![[Pasted image 20251016182242.png]]

### Core Mission
Your work trains and evaluates AI systems used across many industries. The goal: **different people should grade a model the same way on the same task** through clear, consistent, and reproducible prompts, rubrics, golden solutions, and evaluations.

### Two Training Methods

#### Supervised Fine-Tuning (SFT)
**Purpose**: Teaches the model to imitate correct answers using prompt + golden solution pairs

**Characteristics**:
- Rubrics **not required** - model directly learns from target answer
- Best for tasks with **clear right answer** and **tight format**
- Direct imitation learning

#### Reinforced Learning from Human Feedback (RLHF)
**Purpose**: Teaches the model to prefer responses that humans rate higher

**Characteristics**:
- Rubrics **essential** - define what "better" means
- Drives the reward signal the model optimizes against
- Best for **open-ended tasks** where quality is subjective
- Matches human preferences

### Practical Examples

#### SFT Example: Question + Golden Answer Pairs

**Task**: "Label ticket urgency as one of: low | medium | high."

**Before Training Answer**:
> The ticket urgency is high. It needs to be taken care of right now!

**Golden Answer**:
> high

**What the Model Learns**:
- Don't overelaborate
- Emit exactly one allowed label
- No punctuation, no explanations
- Pattern matching: question type → answer format

---

#### RLHF Example: Prompts + Answers + Rubrics + Comparisons

**Prompt**:
"Write a customer support reply in <80 words; include a brief apology; explain refund timeline per provided policy; include the refund portal link; professional, friendly tone; do not promise instant refunds. Policy: 'Refunds are processed in 5–7 business days via the Refund Portal.'"

**Sample Rubric** (simplified):
1. **Apology** — Must contain "sorry" or "apologies"
2. **Timeline** — Explicitly says "5–7 business days" (allow "5-7" or "five to seven" + "business day(s)")
3. **Portal** — Includes a URL to the portal or the exact text "Refund Portal"
4. **No instant promise** — Does not contain "instant/immediate/today/right away/same-day" near "refund/process"

**Model A Response**:
Promises an instant refund; no link → *(violates prompt - comparatively worse answer)*

**Rubric Evaluation**:
- 1. Pass
- 2. Fail
- 3. Fail
- 4. Fail
- **Final Evaluation: 1/4**

**Model B Response**:
> "Sorry for the trouble. Per our policy, refunds are processed in 5–7 business days. Start here: Refund Portal. If you need help, reply to this email." → *(on-spec)*

**Rubric Evaluation**:
- 1. Pass
- 2. Pass
- 3. Pass
- 4. Pass
- **Final Evaluation: 4/4**

**What the Model Learns (via rubric/reward)**:
- The rubric teaches the model to produce policy-grounded, on-spec responses
- Outputs missing any item get a lower score (like Model A)
- The model iteratively grades responses according to rubrics
- Learns from model responses with higher evaluation scores
- Eventually can consistently generate responses that get full marks on rubric evaluation

### Knowledge Check (Onboarding Quiz)

**Q1: Which approach is generally more resource-intensive end-to-end?**
- ✅ **A: RLHF** - requires iteratively training the model based on rubric points until the model scores consistently at max rubric score
- B: They're the same
- C: SFT, because prompts are longer
- D: Depends only on dataset size, not method

**Q2: Which task is best suited for RLHF?**
- A: Validate that a number is even
- B: Map a ticket to {low, medium, high}
- C: Extract a 10-digit invoice ID
- ✅ **D: Write a friendly, policy-compliant customer reply** - open-ended task with subjective quality criteria

**Q3: What does Supervised Fine-Tuning (SFT) teach a model to do?**
- A: Generate new training data automatically
- ✅ **B: Imitate correct answers from prompt → gold pairs** - direct pattern matching
- C: Prefer answers humans like via A/B comparisons
- D: Remove all safety risks

**Q4: Rubrics are required for SFT**
- A: True
- ✅ **B: False** - SFT uses golden answers directly; rubrics not needed

### Key Takeaways
- **RLHF = More resource-intensive** (iterative optimization cycles)
- **Open-ended tasks → RLHF** | **Structured/exact tasks → SFT**
- **SFT = Imitation learning** | **RLHF = Preference learning**
- **Rubrics essential for RLHF, not for SFT**

---

## Module 1: Writing a Good Prompt

### Core Principle
**The best prompt is the one that aligns with the project scope. Everything else is secondary.**

### SFT vs RLHF Prompt Nuance

**SFT Prompts**:
- Can be **shorter**
- Used to train tight output structures and correct outputs
- Keep them concise but scope-true

**RLHF Prompts**:
- Should be **richer**
- Include: specific goals, allowed inputs, explicit assumptions, defined output structure
- Ensures rubric points map 1:1

### Four Essential Elements of a Good Prompt

#### 1. Anchor to the Project Scope (Non-Negotiable)

**What to check**:
- Task goal
- In-bounds sources/tools
- Out-of-scope items
- Output schema
- Success criteria from the brief

**Why it matters**: Scope-aligned prompts reduce grader variance and make downstream rubrics (RLHF) and golden solutions (SFT) straightforward.

#### 2. State the Specific Outcome

**Example (Academia)**:
> "Identify four key findings from the passage, each supported by evidence from the text."

**Why**: Defines correctness (evidence), coverage (four), and scope (the passage).

#### 3. Write Explicit Assumptions

**Ask yourself**: "Which definitions, formulas, or defaults vary by person/industry?"

**Example (Finance)**:
> "Treat Revenue as GAAP net sales unless the source explicitly provides constant-currency growth."

**Why**: Removes hidden judgment calls; ensures consistent application.

#### 4. Define the Output Structure

**Ask yourself**: "If I had to auto-check the output, what would I verify?"

**Example (Calculation)**:
> "Express the final answer in $ millions, rounded to 2 decimals."

**Why**: Enables fast, deterministic checking.

**Prompt Structure Overview:**
![[documents/prompt-structure-overview.png]]

**Prompt Best Practices:**
![[documents/prompt-best-practices.png]]

### Module 1 Comprehension Quiz

**Q1: Which is the best example of a specific Output Structure?**
- A: "Return a table."
- B: "Include important points and figures as needed."
- C: "Write a clear answer."
- ✅ **D: "Two sections: Summary (100–130 words) then Recommendations (exactly 3 bullets, ≤15 words each). Express any dollar amounts in $ millions, 2 decimals."** - Precise, verifiable structure

**Q2: Which is generally the best prompt for RLHF?**
- A: "Summarize the Q3 report in bullets. Use recent sources if needed and keep it under 120 words."
- ✅ **B: "From Security_Report_Q3.pdf only, produce a Markdown table with exactly 3 rows and headers Finding | Evidence (≤25 words) | p.#. No external sources. Evidence must be a verbatim quote from the PDF in quotes; page format p.#. No text before/after the table."** - Rich specification with explicit constraints that map 1:1 to rubric points
- C: "Summarize the Q3 security report and add helpful web context. Sort bullets by importance and include any notable quotes."
- D: "Summarize the report clearly and concisely. Keep it professional and accurate."

**Q3: The best prompt is the one that aligns with the project scope; everything else is secondary.**
- ✅ **A: True** - Core principle of prompt writing
- B: False

**Q4: SFT prompts should generally be…**
- A: Identical to the rubric
- B: Vague so the model "figures it out"
- C: Very long with many edge cases
- ✅ **D: Concise but scope-true** - Tight output structures need clear but brief prompts

---

## Module 2: Making Strong Rubric Points (RLHF-Only)

### Purpose of Rubrics
Rubrics are **only for RLHF**. They let the model iteratively learn which outputs are "better" through rubric grading. The goal: **model eventually scores at the highest level for a rubric evaluation**.

### Four Qualities of Good Rubric Points

#### 1. Atomic & Objective – One Pass/Fail Check Per Line

**Good**:
> "Section 'Key Findings' has exactly 4 bullets."

**Bad**:
> "Has 4 bullets and uses € format." *(Compound: must split into two points)*

#### 2. 1:1 with the Prompt – Don't Introduce New Requirements

**Good** (Prompt asked for exact headers):
> "Table headers are Finding | Evidence (≤25 words) | Source Ref in that order."

**Bad**:
> "Table is sorted by importance." *(Sorting wasn't asked)*

#### 3. Objective Phrasing – Use Exact Strings/Limits/Enumerations

**Good**:
> "Each Evidence cell is a verbatim quote ≤25 words."

**Bad**:
> "Evidence is properly cited." *(Subjective)*

#### 4. Measurable – Deterministic to Verify Quickly

**Good**:
> "Use sources published within 12 months of the task date and include the publication date."

**Bad**:
> "Use recent sources." *(Undefined window)*

### Example Prompt and Sample Rubrics

![[documents/rubric-example-1.png]]

![[documents/rubric-example-2.png]]

![[documents/rubric-example-3.png]]

### Module 2 Comprehension Quiz
**Passing Score Required: 80%** - Course restarts if failed

**Q1: "Evidence is properly cited" is objective phrasing.**
- A: True
- ✅ **B: False** - "Properly cited" is subjective; needs exact specification

**Q2: It's acceptable for rubrics to add helpful requirements not stated in the prompt.**
- A: True
- ✅ **B: False** - Rubrics must be 1:1 with the prompt; no new requirements

**Q3: Each rubric line should be a single pass/fail check.**
- ✅ **A: True** - Atomic & objective principle
- B: False

**Q4: Which rubric point is truly atomic?**
- ✅ **A: "Section 'Key Findings' has exactly 4 bullets."** - Single verifiable check
- B: "Has 4 bullets and uses € format." - Compound (two checks)
- C: "Bullets are clear and professional." - Subjective
- D: "Findings are stated well, and conclusion is written in 4-6 bullets." - Compound & subjective

**Q5: Where are rubrics required?**
- ✅ **A: RLHF only** - SFT uses golden answers directly
- B: SFT and RLHF equally
- C: Neither SFT nor RLHF
- D: SFT only

---

## Module 3: Writing the Golden Solution

### Purpose
A golden solution is a **single source of truth** that walks another person through your structured reasoning. The primary goal: **enable a reviewer to understand your logic** while solving the prompt.

### Three Key Components

#### 1. Explicit Assumptions
**What this means**: Reiterate assumptions emphasized in the prompt that might not be common sense or industry standard.

**Why**: Emphasizes the solution's compliance with the prompt.

#### 2. Formulas & Definitions (for calculation-based prompts)
**What this means**: The exact equations, variable definitions, units, rounding, and tolerance you used.

**Why**: Results are reproducible by another person.

#### 3. Step-by-Step Solution
**What this means**: Minimal checkable steps showing what you did and why.

**Why**: Enables a reviewer to reproduce results and spot errors quickly.

### Golden Solution Examples

![[documents/golden-solution-1.png]]

![[documents/golden-solution-2.png]]

![[documents/golden-solution-3.png]]

![[documents/golden-solution-4.png]]

**Why These Examples Work**: They lay out a **minimal, reproducible path** that anyone can retrace and spot the first error quickly.

### Module 3 Comprehension Quiz
**Passing Score Required: 75%** - Course restarts if failed

**Q1: It's acceptable to use out-of-scope sources in the Golden Solution if they seem accurate.**
- A: True
- ✅ **B: False** - Must stay within project scope boundaries

**Q2: Explicit assumptions restate definitions that could vary across people or industries.**
- ✅ **A: True** - Ensures consistent application across evaluators
- B: False

**Q3: Which principle matters most for a Golden Solution?**
- A: Minimizing technical terms
- B: Creative storytelling
- C: Maximum length for completeness
- ✅ **D: Structured so another person can understand the solution** - Primary goal is reviewer comprehension

**Q4: What is the primary purpose of a Golden Solution?**
- ✅ **A: Guide reviewers through your logic as a single source of truth** - Enable others to understand and reproduce
- B: Showcase the Expert's writing style
- C: Train the model directly without prompts
- D: Speed up data collection by skipping details

---

## Module 4: Reviewing a Model's Chain of Thought

### Overview
Evaluating a model's chain-of-thought is primarily associated with **RLHF workflows**. Read the model's reasoning closely. Today's models can sometimes outperform the seeded Q&A. **Be willing to update your own work**—and be precise when the model is wrong.

### When the Model is Right (and your original Q&A pair was wrong)

1. **Acknowledge the discrepancy**
2. **Verify with allowed sources/assumptions**
3. **Amend the golden solution** (and, if RLHF, adjust rubric if needed)
4. **Rewrite prompt, answer, and golden solution** if that is within scope of the project

### When the Model is Wrong — Find the First Break

**Why it matters**: Identifying the first break in logic is important, as all the following steps within the model's chain of reasoning rely on the assumptions made at the previous step.

**Process**: After identifying the first break, still read through the model's logic to ensure that the model does not make any more logical errors.

#### Common Model Errors

**Formula misuse**:
- Error: Used (New−Old)/New instead of (New−Old)/Old
- Fix: Apply correct base

**Arithmetic slip**:
- Error: Rounding/sign/decimal error
- Fix: Recompute per tolerance

**Definition mismatch**:
- Error: The prompt requires "5–7 business days." The model writes "5–7 days" or "within a week"
- Fix: Ensure exact terminology match

### Wrap-Up Principle
**Assume good faith, test claims against scope, and either:**
- Update your prompt and answer sets (when the model is right), OR
- Pinpoint the first error with a crisp fix (when the model is wrong)

### Chain of Thought Review Examples

![[documents/cot-review-1.png]]

![[documents/cot-review-2.png]]

### Module 4 Comprehension Quiz

**Q1: The first divergence from the prompt or golden solution is the primary place to intervene within the model's chain-of-thought.**
- ✅ **A: True** - All following steps rely on previous assumptions; identify the first break
- B: False

**Q2: Scenario: Prompt defines growth as (New − Old) / Old. The model shows (New − Old) / New in its steps; due to numbers, the final percent matches. How do you mark the model's chain-of-thought?**
- A: Model get's it right, final answer is the same as expected.
- B: Ignore this step entirely
- C: Penalize the model's tone
- ✅ **D: Identify the first step that diverges from the instructions, mark that the model got the question incorrectly and explain the correct specified method from the prompt.** - Process compliance matters, not just outcome

**Q3: You should verify the model's answer against allowed sources/assumptions before updating the golden solution.**
- ✅ **A: True** - Always verify before updating golden solutions
- B: False

**Q4: A top model returns an in-scope, correct answer that improves on your current prompt + golden solution set. What should you do next?**
- A: Fail the model; the golden solution is authoritative
- B: Keep the item unchanged for consistency
- C: Add a new rubric requirement mid-task to force a miss
- ✅ **D: Retire this item, and author a new prompt + golden solution that targets a remaining gap** - Model has mastered this; create new challenges

---

