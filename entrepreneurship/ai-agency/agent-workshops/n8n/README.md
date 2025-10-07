# n8n Workshop for AI Agent Development

**Purpose:** Essential n8n knowledge and tools for building buyanagent.ai marketplace agents
**Source Repository:** [n8n-sandbox](https://github.com/lindonharris/n8n-sandbox)
**Last Updated:** October 7, 2025
**Status:** Production-ready essentials extracted from 6+ months of n8n production experience

---

## 🎯 What This Workshop Provides

This workshop contains the **minimum essential** n8n knowledge needed to build reliable AI agents for buyanagent.ai. It's distilled from a comprehensive 6-month n8n development project that discovered critical platform bugs and developed proven workarounds.

### Key Components

1. **[Critical Bugs & Solutions](docs/critical-bugs.md)** - Platform bugs that will break your agents (IF node boolean bug, Notion node failure, etc.)
2. **[Development Protocol](docs/development-protocol.md)** - Step-by-step workflow for safe n8n development
3. **[Implementation Guide](docs/implementation-guide.md)** - Master reference for n8n patterns and best practices
4. **[Workflow Manager Tool](tools/n8n-workflow-manager.js)** - CLI for managing workflows via API
5. **[Reference Workflows](workflows/)** - Production-tested workflow templates

---

## 🚀 Quick Start for buyanagent.ai Agents

### Step 1: Understand Critical Bugs (5 minutes)
**Read:** [docs/critical-bugs.md](docs/critical-bugs.md)

You MUST know these before building ANY n8n workflow:
- **IF Node Boolean Bug** - IF nodes always evaluate to FALSE → Use Switch nodes instead
- **Notion Node Failure** - Property mapping doesn't work → Use Google Sheets or direct API
- **Variable Scoping After Routing** - `$json` becomes empty after IF/Switch → Use `$node["Name"].json`
- **Email Parameter** - Use `"message"` not `"text"` for email body

### Step 2: Set Up Development Environment (10 minutes)
```bash
# 1. Set environment variables
export N8N_API_URL="https://your-instance.n8n.cloud/api/v1"
export N8N_API_KEY="your-api-key"

# 2. Test workflow manager
cd tools/
./n8n-workflow-manager.js list

# 3. Download a reference workflow
./n8n-workflow-manager.js download WORKFLOW_ID
```

### Step 3: Follow Development Protocol (Always)
**Read:** [docs/development-protocol.md](docs/development-protocol.md)

Standard development cycle:
1. **List** → `./n8n-workflow-manager.js list`
2. **Download** → `./n8n-workflow-manager.js download ID`
3. **Edit** → Modify the clean JSON file (not the -full version)
4. **Backup** → `cp workflow.json BACKUP-$(date +%s).json`
5. **Upload** → `./n8n-workflow-manager.js upload ID workflow.json`
6. **Test** → Verify actual output, not just "success" status

---

## 📚 Documentation Structure

### Essential Reading (Read in Order)

1. **[Critical Bugs](docs/critical-bugs.md)** (15 min)
   - Platform bugs that will break your agents
   - Proven workarounds and solutions
   - Required reading before building anything

2. **[Development Protocol](docs/development-protocol.md)** (20 min)
   - Standard development workflow
   - Surgical precision protocol for modifying working workflows
   - Emergency rollback procedures

3. **[Implementation Guide](docs/implementation-guide.md)** (45 min)
   - Comprehensive n8n patterns and best practices
   - Node-specific guidance
   - Data flow patterns
   - Production deployment strategies

### Reference Documentation

4. **[Official n8n Docs](https://docs.n8n.io/)** - External reference
5. **[n8n Community Forum](https://community.n8n.io/)** - External support
6. **[n8n-MCP Documentation](https://github.com/n8n-io/n8n-mcp)** - MCP server integration

---

## 🛠️ Tools

### n8n Workflow Manager
**Location:** `tools/n8n-workflow-manager.js`
**Purpose:** CLI for managing n8n workflows via API
**Features:**
- Download workflows (creates clean + full backup)
- Upload with automatic JSON cleaning
- Activate/deactivate workflows
- View execution history
- Interactive menu mode

**Quick Commands:**
```bash
./n8n-workflow-manager.js                    # Interactive mode
./n8n-workflow-manager.js list              # List all workflows
./n8n-workflow-manager.js download ID       # Download workflow
./n8n-workflow-manager.js upload ID file    # Upload workflow
./n8n-workflow-manager.js executions ID 10  # View recent executions
```

---

## 📋 Workflow Templates

### Email Sweeper Agent ($29-39/month)
**Location:** `workflows/email-sweeper-template.json`
**Features:**
- Gmail integration with OAuth2
- AI-powered email classification
- Bulk unsubscribe/archive/delete
- Safety confirmations

### Newsletter Digester Agent ($49-59/month)
**Location:** `workflows/newsletter-digester-template.json`
**Features:**
- Newsletter detection
- AI summarization
- Daily digest email
- Link extraction

### Expense Manager Agent ($69-79/month)
**Location:** `workflows/expense-manager-template.json`
**Features:**
- Receipt email parsing
- AI categorization
- Google Sheets integration
- Monthly summary reports

### Invoice Chaser Agent ($100/month)
**Location:** `workflows/invoice-chaser-template.json`
**Features:**
- Invoice tracking
- Automated reminders
- Payment confirmations
- DSO analytics dashboard

### Lead Qualification Agent ($100-150/month)
**Location:** `workflows/lead-qualification-template.json`
**Features:**
- Form submission processing
- AI scoring
- CRM integration
- Pipeline dashboard

---

## 🏗️ Building buyanagent.ai Agents

### Agent Development Checklist

#### Phase 1: Design (Before Building)
- [ ] Read critical bugs document
- [ ] Identify required integrations (Gmail, Sheets, etc.)
- [ ] Choose closest reference workflow
- [ ] Sketch data flow diagram
- [ ] List all nodes needed

#### Phase 2: Build (Iterative Development)
- [ ] Download reference workflow
- [ ] Create timestamped backup
- [ ] Modify ONE node at a time
- [ ] Test after each change
- [ ] Document any issues encountered

#### Phase 3: Testing (Before Deployment)
- [ ] Test with real data
- [ ] Verify end-to-end functionality (not just "success" status)
- [ ] Check error handling paths
- [ ] Validate all integrations
- [ ] Performance test with volume

#### Phase 4: Production (Deployment)
- [ ] Save to production workflows folder
- [ ] Document setup instructions
- [ ] Create customer activation guide
- [ ] Set up monitoring
- [ ] Test customer onboarding flow

---

## ⚠️ Critical Rules

### NEVER Do This
1. ❌ Use IF nodes for boolean comparisons → Use Switch nodes
2. ❌ Use Notion node for property mapping → Use Google Sheets or HTTP Request
3. ❌ Trust "success" execution status → Always verify actual output
4. ❌ Modify working workflows without backups → Always create timestamped backup
5. ❌ Use Code nodes on n8n Cloud → Use Set nodes or HTTP Request nodes
6. ❌ Access `$json` after routing nodes → Use `$node["NodeName"].json` instead

### ALWAYS Do This
1. ✅ Create backup before modifying working workflow
2. ✅ Make ONE change at a time
3. ✅ Test with actual data, not assumptions
4. ✅ Check end-to-end results in destination systems
5. ✅ Document new bugs or patterns discovered
6. ✅ Use workflow manager tool (not manual API calls)

---

## 📞 Getting Help

### When Building Agents
1. **Check critical bugs doc** - Is this a known issue?
2. **Check implementation guide** - Does a pattern exist?
3. **Check reference workflows** - Has this been solved before?
4. **Check n8n community forum** - Is this a common problem?
5. **Use workflow manager executions** - What does actual data show?

### Common Issues & Solutions
| Issue | Solution | Reference |
|-------|----------|-----------|
| IF node always goes to false | Use Switch node with string comparison | critical-bugs.md |
| Email body is blank | Use "message" parameter, not "text" | critical-bugs.md |
| Data disappears after routing | Use `$node["Name"].json` syntax | critical-bugs.md |
| Notion properties don't save | Use Google Sheets or direct API | critical-bugs.md |
| Workflow success but no output | Check actual destination, not execution status | development-protocol.md |

---

## 🔗 External Resources

### Official n8n Resources
- **Documentation:** https://docs.n8n.io/
- **Node Reference:** https://docs.n8n.io/integrations/builtin/
- **Community Forum:** https://community.n8n.io/
- **GitHub:** https://github.com/n8n-io/n8n
- **API Reference:** https://docs.n8n.io/api/

### n8n-MCP Integration
- **n8n-MCP GitHub:** https://github.com/n8n-io/n8n-mcp
- **MCP Protocol:** https://github.com/modelcontextprotocol
- **Claude Desktop MCP:** https://docs.anthropic.com/claude/docs/mcp

### Related Projects
- **Full n8n-sandbox repo:** https://github.com/lindonharris/n8n-sandbox (comprehensive 6-month research project)

---

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Oct 7, 2025 | Initial extraction from n8n-sandbox for buyanagent.ai |

---

## 🎯 Success Metrics for buyanagent.ai Agents

### Development Velocity
- **Time to build agent:** < 4 hours (using templates and protocols)
- **Time to fix bug:** < 30 minutes (using critical bugs doc)
- **Time to test:** < 1 hour (using development protocol)

### Quality Metrics
- **Zero data loss:** Through backup protocols
- **Zero prolonged outages:** Through surgical precision edits
- **100% bug pattern documentation:** Update critical-bugs.md when new issues found

### Customer Success Metrics
- **Setup time:** < 30 minutes (using customer activation guides)
- **Reliability:** 99.9% uptime (through proven patterns)
- **Support tickets:** < 1 per 100 customers (through comprehensive docs)

---

*This workshop is living documentation. Update it as new patterns emerge from buyanagent.ai agent development.*
