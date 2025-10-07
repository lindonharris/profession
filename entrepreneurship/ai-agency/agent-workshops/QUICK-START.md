# Agent Workshops - Quick Start Guide

**Created:** October 7, 2025
**Purpose:** Get building agents in < 10 minutes

---

## 🚀 Fastest Path to Building

### Step 1: Read Critical Bugs (15 minutes) ⚠️ **REQUIRED**
```bash
cd n8n/docs/
cat critical-bugs.md
```

**Why:** n8n has 7 platform bugs that will break your agents. You MUST know these before building anything.

**Critical Knowledge:**
- IF nodes always return FALSE → Use Switch nodes
- Notion node doesn't work → Use Google Sheets
- `$json` becomes empty after routing → Use `$node["Name"].json`
- Email body parameter is `"message"` not `"text"`

---

### Step 2: Set Up n8n Environment (5 minutes)
```bash
# Set environment variables
export N8N_API_URL="https://your-instance.n8n.cloud/api/v1"
export N8N_API_KEY="your-api-key"

# Test workflow manager
cd n8n/tools/
./n8n-workflow-manager.js list
```

---

### Step 3: Clone Template & Build (Variable)
```bash
# Download a reference workflow
./n8n-workflow-manager.js download WORKFLOW_ID

# Create backup before editing
cp workflow.json BACKUP-$(date +%s).json

# Edit workflow.json
# (Make ONE change at a time)

# Upload and test
./n8n-workflow-manager.js upload WORKFLOW_ID workflow.json
```

---

## 📚 Essential Documentation (Read in Order)

1. **[n8n/README.md](n8n/README.md)** - 5 min
2. **[n8n/docs/critical-bugs.md](n8n/docs/critical-bugs.md)** - 15 min ⚠️ **REQUIRED**
3. **[n8n/docs/development-protocol.md](n8n/docs/development-protocol.md)** - 20 min

**Total:** 40 minutes to production-ready knowledge

---

## ⚡ Emergency Reference

### "My IF node always goes to false"
**Solution:** Replace with Switch node using string comparison
**Doc:** [critical-bugs.md](n8n/docs/critical-bugs.md#bug-1-if-node-boolean-comparison-always-returns-false-)

### "My email body is blank"
**Solution:** Use `"message"` parameter, not `"text"`
**Doc:** [critical-bugs.md](n8n/docs/critical-bugs.md#bug-4-email-parameter-naming-text-vs-message-)

### "Data disappears after routing"
**Solution:** Use `$node["NodeName"].json` instead of `$json`
**Doc:** [critical-bugs.md](n8n/docs/critical-bugs.md#bug-3-variable-scoping-after-routing-nodes-)

### "Workflow shows success but nothing happened"
**Solution:** Always verify actual output in destination systems
**Doc:** [critical-bugs.md](n8n/docs/critical-bugs.md#bug-6-workflow-success--functional-success-)

---

## 🎯 buyanagent.ai Agent Templates

| Agent | Template | Price Tier |
|-------|----------|-----------|
| **Email Sweeper** | `workflows/email-sweeper-template.json` | $29-39 (Utility) |
| **Newsletter Digester** | `workflows/newsletter-digester-template.json` | $49-59 (Utility) |
| **Expense Manager** | `workflows/expense-manager-template.json` | $69-79 (Utility) |
| **Invoice Chaser** | `workflows/invoice-chaser-template.json` | $100 (Premium) |
| **Lead Qualification** | `workflows/lead-qualification-template.json` | $100-150 (Premium) |

---

## 🔗 All Documentation Locations

```
agent-workshops/
├── README.md                          Workshop overview
├── QUICK-START.md                     👈 You are here
│
└── n8n/                               n8n Workshop
    ├── README.md                      n8n overview & quick start
    ├── docs/
    │   ├── DOCUMENTATION-INDEX.md     All n8n official docs
    │   ├── critical-bugs.md           ⚠️ MUST READ FIRST
    │   ├── development-protocol.md    Standard workflows
    │   └── implementation-guide.md    Comprehensive reference
    ├── tools/
    │   └── n8n-workflow-manager.js    CLI tool
    └── workflows/
        └── (agent templates)
```

---

## 💡 Pro Tips

### Development Workflow
1. ✅ **ALWAYS** create backup before modifying working workflow
2. ✅ **ALWAYS** make ONE change at a time
3. ✅ **ALWAYS** test with real data, not assumptions
4. ✅ **ALWAYS** verify actual output, not just "success" status
5. ✅ **ALWAYS** use workflow manager tool (not manual API)

### Critical Rules
1. ❌ **NEVER** use IF nodes for boolean comparisons
2. ❌ **NEVER** use Notion node for property mapping
3. ❌ **NEVER** trust execution status without verifying output
4. ❌ **NEVER** use Code nodes on n8n Cloud
5. ❌ **NEVER** access `$json` after routing without node reference

---

## 📞 Getting Help

| Issue | Solution |
|-------|----------|
| **Known bug?** | [critical-bugs.md](n8n/docs/critical-bugs.md) |
| **How to develop?** | [development-protocol.md](n8n/docs/development-protocol.md) |
| **Node syntax?** | [DOCUMENTATION-INDEX.md](n8n/docs/DOCUMENTATION-INDEX.md) |
| **Still stuck?** | [n8n Community Forum](https://community.n8n.io/) |

---

## 🎯 Success Checklist

Before deploying any agent:

- [ ] Read critical-bugs.md
- [ ] Avoided all 7 known platform bugs
- [ ] Created timestamped backup
- [ ] Made changes one at a time
- [ ] Tested with real data
- [ ] Verified actual output (not just status)
- [ ] Documented any new patterns discovered

---

*Get building! Questions? Start with [n8n/README.md](n8n/README.md)*
