---
# Case Metadata
case_number: "624-092"
title: "Hospital for Special Surgery: Returning to a New Normal? (A)"
course: "TOM"
date_published: 2024-08-05
date_read: 2025-10-05
class_number: 10
professor: "Allison Mnookin"
tags: [case-study, operations-management, process-flow, capacity-planning, bottleneck-analysis, healthcare, covid-19]
industry: "Healthcare"
company: "Hospital for Special Surgery"
geographic_focus: "New York City, NY"
key_topics: [process-capacity, bottleneck-identification, operations-redesign, patient-flow, covid-operations]
protagonists: ["Justin Oppenheimer (Enterprise COO & Chief Strategy Officer, OCTF Chair)"]
decision_point: "How to eliminate patient backups outside the Pavilion building while safely reopening outpatient operations during COVID-19"
teaching_objectives: [capacity-analysis, bottleneck-identification, process-flow-optimization, operational-constraints]
---

# Hospital for Special Surgery: Returning to a New Normal? (A)

## Quick Facts
- **Case #**: 624-092
- **Course**: [[TOM]]
- **Date Read**: 2025-10-05
- **Industry**: Healthcare (Orthopedic Hospital)
- **Geography**: New York City, NY

## Executive Summary
> Hospital for Special Surgery (HSS), a renowned orthopedic hospital in NYC, is reopening outpatient operations after COVID-19 lockdown with consolidated operations in the Pavilion building. Despite dramatically limiting physicians' schedules, simulations show patients will be forced to wait outside the building—unacceptable for HSS's reputation and patients with painful orthopedic conditions. Oppenheimer must identify the root cause and find solutions to eliminate outdoor waiting.

## Case Context

### Company Background
- Hospital for Special Surgery (HSS) is a renowned orthopedic hospital in New York City
- Known for exceptional patient experience and specialized orthopedic care
- Many patients suffer from ailments that make standing painful
- Reputation built on patient-centered care and operational excellence
- Consolidated outpatient operations to Pavilion building during COVID-19 reopening

### Industry Landscape
- COVID-19 pandemic forcing healthcare facilities to redesign operations
- Social distancing and safety protocols creating new operational constraints
- Need to balance patient safety with operational efficiency
- Healthcare facilities nationwide adapting to "new normal" post-lockdown

### Timeline of Events
- **March 2020**: New York City COVID-19 lockdown forces HSS to suspend outpatient operations
- **April 2020**: HSS begins planning for reopening
- **Reopening Planning**: Outpatient Care Task Force (OCTF) formed, co-chaired by Justin Oppenheimer and Dr. Larry Gulotta
- **Decision Point**: OCTF consolidates outpatient operations to Pavilion building with limited physician schedules
- **Current Situation**: Simulations predict patients will be forced to wait outside due to capacity constraints

## Key Protagonists
- **Justin Oppenheimer**: Enterprise Chief Operating Officer and Chief Strategy Officer, Chair of Outpatient Care Task Force (OCTF)
  - Background: HSS executive responsible for reopening strategy
  - Key decisions: Consolidated operations to Pavilion, limited physician schedules, created various COVID accommodations
  - Current challenge: Must solve outdoor waiting problem while maintaining safety protocols

- **Dr. Larry Gulotta**: Vice Chair of Ambulatory Services and Chief of Shoulder and Elbow Division, OCTF Co-Chair
  - Background: Sports Medicine Institute surgeon
  - Key role: Co-chaired OCTF with Oppenheimer

## Central Problem/Decision

### The Question
> What is causing patients to back up outside the Pavilion building, and what adjustments can be made to eliminate outdoor waiting while maintaining COVID-19 safety protocols?

### Constraints
1. **COVID-19 Safety Requirements**: Social distancing, screening, cleaning protocols
2. **Physical Space**: Limited to Pavilion building with fixed elevator capacity, lobby chairs, reception desks
3. **Patient Experience**: HSS reputation depends on not forcing patients with painful conditions to wait outside
4. **Weather Dependency**: Outdoor waiting unacceptable during inclement weather
5. **Physician Schedules**: Already dramatically limited to accommodate new protocols
6. **Arrival Patterns**: Patients scheduled within hourly blocks arrive uniformly throughout the hour

### Success Metrics
- Zero patients waiting outside the building
- Maintain COVID-19 safety protocols
- Preserve HSS reputation for patient experience
- Efficient use of physician time and facility resources

## Analysis

### Process Flow Steps
1. **COVID Screening** (Outdoor plaza/entrance)
   - 3 screening nurses
   - Patients checked for symptoms and temperature

2. **Lobby Waiting Area**
   - 24 chairs (socially distanced)
   - Limited capacity due to COVID spacing requirements

3. **Elevator to Upper Floors**
   - 6-person capacity per elevator trip
   - Bottleneck due to social distancing and building design

4. **Floor Reception/Check-in**
   - 6 reception desks across multiple floors
   - Patient registration and paperwork

5. **Physician Visit**
   - Scheduled appointments
   - Limited physician availability due to reopening constraints

6. **Diagnostic Testing** (if needed)
   - Imaging, labs, other tests
   - Return flow back through building

### Key Operational Constraints
- **Hourly Arrival Pattern**: Patients arrive uniformly within scheduled hour
- **Process starts at 9am**: Patient inflow begins exactly at 9:00am
- **Similar flow patterns**: All patient flows follow similar arrival patterns
- **Continuous flow assumption**: Treat process as continuous rather than batched

### Bottleneck Hypothesis
Based on case details, likely bottleneck candidates:
1. **Elevator capacity** (6 people, vertical transport constraint)
2. **Lobby chairs** (24 seats with social distancing)
3. **Screening nurses** (3 nurses at entrance)
4. **Floor reception** (6 desks across floors)

## Key Exhibits
- Exhibit 1: Pavilion building layout showing process flow
- Exhibit 2: Patient scheduling data and arrival patterns
- Exhibit 3: Capacity constraints for each process step
- Exhibit 4: Simulation results showing outdoor queue formation

## Discussion Questions
1. What is the capacity of each step in the hospital flow? What is the bottleneck that is causing patients to wait? At what point in the day do patients start having to wait in the outdoor plaza?

2. How is the backup at the Hospital for Special Surgery similar and different from the trucks waiting in National Cranberry?

3. What solution would you propose to solve the backup at the Hospital for Special Surgery? What pros and cons does your solution have? Please use both qualitative reasoning and calculations to support the feasibility of your proposal.

## My Analysis & Recommendations

### Option 1: Stagger Appointment Scheduling
**Pros**:
- Smooths patient arrival pattern throughout the day
- Reduces peak load on bottleneck resources
- No additional capital investment required
- Easy to implement through scheduling system changes

**Cons**:
- May inconvenience patients who prefer specific appointment times
- Requires coordination with physician schedules
- Doesn't address fundamental capacity constraints
- May only partially solve the problem

### Option 2: Add Elevator Capacity or Redesign Patient Flow
**Pros**:
- Directly addresses bottleneck if elevator is the constraint
- Could use stairs for able-bodied patients (though orthopedic patients may struggle)
- Permanent solution to capacity issue
- Improves long-term operational efficiency

**Cons**:
- Cannot add elevators (building constraint)
- Many orthopedic patients cannot use stairs
- May require significant operational redesign
- Time-intensive to implement

### Option 3: Expand Waiting Areas and Processing Capacity
**Pros**:
- Increases buffer capacity before bottleneck
- Could add outdoor covered/heated waiting area
- Flexible and scalable solution
- Improves patient comfort

**Cons**:
- Requires capital investment
- May not solve root cause if bottleneck is downstream
- COVID distancing limits how much capacity can increase
- Weather-dependent solutions still problematic

### Recommended Action
> **Hybrid approach**: (1) Immediately implement staggered scheduling to smooth arrivals, (2) Calculate exact bottleneck capacity to identify constraint, (3) Add targeted capacity at bottleneck step (likely elevator or lobby), (4) Consider alternative routing for ambulatory patients to bypass elevator if possible.

### Implementation Plan
1. **Immediate (Week 1)**: Conduct detailed capacity analysis of each process step to identify true bottleneck
2. **Short-term (Weeks 2-3)**: Implement staggered appointment scheduling with 15-minute intervals instead of hourly blocks
3. **Medium-term (Weeks 4-8)**: Add capacity at identified bottleneck (additional screening staff, lobby chairs, elevator trips, or reception desks)
4. **Long-term**: Monitor patient flow data and continuously optimize scheduling and capacity allocation

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
1. **Bottleneck identification is critical in process design**: The case demonstrates how a single constraint (likely the elevator) can create cascading effects throughout the entire patient flow system, even when other resources appear adequate.

2. **Capacity planning must account for variability**: Uniform hourly arrivals create predictable peaks that stress the bottleneck, showing the importance of demand smoothing in capacity-constrained environments.

3. **COVID operations require fundamental process redesign**: Simple capacity reductions aren't sufficient—successful reopening requires rethinking entire patient flows, not just reducing throughput.

### Applications to Future Situations
- Any service operation with physical space constraints and customer experience requirements
- Healthcare operations management with competing objectives (safety vs. efficiency vs. experience)
- Process bottleneck analysis in multi-step service delivery
- Capacity planning under uncertainty and regulatory constraints

### Questions for Further Research
- What is the optimal appointment scheduling interval to minimize waiting while maximizing physician utilization?
- How do patient arrival patterns vary by appointment type, and should scheduling differ accordingly?
- What is the trade-off between patient convenience (preferred appointment times) and operational efficiency (smoothed demand)?
- Could technology (mobile check-in, virtual queuing) reduce physical capacity constraints?

## Related Cases & Readings
- [[National Cranberry Cooperative]]
- [[Process Capacity and Bottleneck Analysis]]
- [[Service Operations Management]]
- [[Healthcare Operations Design]]

## Additional Resources
- Hospital for Special Surgery website: www.hss.edu
- COVID-19 healthcare reopening guidelines
- Process capacity and queuing theory fundamentals

---
*Original PDF*: [[624-092 Hospital for Special Surgery.pdf]]
