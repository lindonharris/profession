# Donner Company Process Flow

## Complete Order-to-Delivery Flow

### Pre-Production
1. **Receive customer order with artwork and specifications**
2. **Write material specifications from 30 base stock types**
3. **Send order to purchasing agent for sourcing**
4. **Enter order into production log for tracking**
5. **Send blueprint and factory order to supervisor**
6. **Wait for raw materials to arrive from vendor**
7. **Schedule production based on capacity and priorities**

### Production Flow

**Preparation Stage:**
1. **Digitize hole locations from customer's detailed drawings**
2. **Inspect laminate sheets for any visual defects**
3. **Shear 36x48 sheets into 12x18 inch panels**
4. **Punch location holes for alignment in drilling**

**Image Transfer Stage:**
5. **Pin panel to drill table using location holes**
6. **Drill approximately 500 holes per circuit board**
7. **Process panels through copper immersion bath**
8. **Wash, scrub, and coat with dry film photoresist**
9. **Lay artwork on coated panels for imaging**
10. **Expose panels to UV light through artwork**
11. **Develop panels to wash away unexposed photoresist**
12. **Electroplate copper conductors now bare from development**
13. **Chemically strip DFPR from panel**
14. **Chemically etch copper layer off glass epoxy base**
15. **Chemically strip tin from circuits leaving copper image**

**Fabrication Stage:**
16. **Apply soldermask protective epoxy over circuit traces**

### Key Process Characteristics
- **Completely serial flow** - no parallel paths except drilling resource choice
- **Setup required at every step** - "on-the-line" setups (not performed until previous order completes)
- **Unit conversions**:
  - Raw sheets: 36"x48"
  - Panels: 12"x18" (typically 8 per sheet)
  - Boards: typically 8 per panel
  - Holes: ~500 per board
- **Single resource at each step** except drilling (7 manual OR 1 CNC)
- **8-hour single shift operation**

### Notes
- Artwork generation happens in parallel to prepare patterns for DFPR exposure
- Inspection, shearing, and location hole punching can occur without referencing the artwork
- Every order requires complete setup at each station before processing begins

---
*Last Updated: 2025-09-09*
*Source: Operations at the Donner Company (602-040)*