# n8n Workshop Documentation Index

**Purpose:** Quick reference to all n8n documentation
**Last Updated:** October 7, 2025

---

## 📚 Internal Documentation (This Workshop)

### Essential Reading (Priority Order)

1. **[critical-bugs.md](critical-bugs.md)** ⭐ **START HERE**
   - 7 platform bugs that will break your workflows
   - Proven workarounds for each
   - **Time:** 15 minutes
   - **Required before building anything**

2. **[development-protocol.md](development-protocol.md)**
   - Standard development workflow
   - Surgical precision protocol
   - Emergency rollback procedures
   - **Time:** 20 minutes
   - **Follow this for every workflow**

3. **[implementation-guide.md](implementation-guide.md)**
   - Comprehensive n8n patterns
   - Node-specific best practices
   - Data flow patterns
   - **Time:** 45 minutes
   - **Reference as needed**

---

## 🔗 Official n8n Documentation (External)

### Core References

| Documentation | URL | Purpose |
|--------------|-----|---------|
| **Main Docs** | https://docs.n8n.io/ | Official documentation hub |
| **Node Reference** | https://docs.n8n.io/integrations/builtin/ | All 525+ node specifications |
| **API Reference** | https://docs.n8n.io/api/ | REST API endpoints |
| **Workflow Examples** | https://docs.n8n.io/workflows/ | Official workflow templates |
| **Expressions** | https://docs.n8n.io/code-examples/expressions/ | n8n expression syntax |

### Integration-Specific Docs

| Integration | URL | Notes |
|------------|-----|-------|
| **Gmail** | https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/ | OAuth2 setup required |
| **Google Sheets** | https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/ | Preferred over Notion |
| **OpenAI** | https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.lmchatopenai/ | For AI agents |
| **Slack** | https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/ | For notifications |
| **HTTP Request** | https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/ | Generic API calls |
| **Webhook** | https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/ | For triggers |

### Advanced Topics

| Topic | URL | When You Need It |
|-------|-----|------------------|
| **Credentials** | https://docs.n8n.io/credentials/ | Setting up API keys |
| **Error Workflows** | https://docs.n8n.io/workflows/error-handling/ | Production error handling |
| **Execution Data** | https://docs.n8n.io/hosting/configuration/configuration-examples/execution-data/ | Data retention |
| **Webhooks Security** | https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/#webhook-security | Securing endpoints |

---

## 🤖 n8n-MCP Documentation (AI Integration)

### n8n-MCP Server

| Documentation | URL | Purpose |
|--------------|-----|---------|
| **n8n-MCP GitHub** | https://github.com/n8n-io/n8n-mcp | MCP server for AI assistants |
| **Quick Start** | https://github.com/n8n-io/n8n-mcp#quick-start | Setup with Claude Desktop |
| **Tool Reference** | https://github.com/n8n-io/n8n-mcp#available-tools | All MCP tools |

### Model Context Protocol

| Documentation | URL | Purpose |
|--------------|-----|---------|
| **MCP Specification** | https://github.com/modelcontextprotocol | Protocol specification |
| **Claude Desktop MCP** | https://docs.anthropic.com/claude/docs/mcp | Claude integration guide |

---

## 🏗️ buyanagent.ai-Specific Documentation

### Agent Templates

| Agent | Template Location | Documentation |
|-------|------------------|---------------|
| **Email Sweeper** | `workflows/email-sweeper-template.json` | TBD |
| **Newsletter Digester** | `workflows/newsletter-digester-template.json` | TBD |
| **Expense Manager** | `workflows/expense-manager-template.json` | TBD |
| **Invoice Chaser** | `workflows/invoice-chaser-template.json` | TBD |
| **Lead Qualification** | `workflows/lead-qualification-template.json` | TBD |

### Integration Guides

| Integration | Documentation | Status |
|------------|---------------|--------|
| **Stripe (Payments)** | TBD | Pending |
| **Supabase (Database)** | TBD | Pending |
| **Customer Onboarding** | TBD | Pending |

---

## 💬 Community Resources

### Forums and Support

| Resource | URL | Purpose |
|----------|-----|---------|
| **Community Forum** | https://community.n8n.io/ | Questions and support |
| **Discord** | https://discord.gg/n8n | Real-time chat |
| **GitHub Issues** | https://github.com/n8n-io/n8n/issues | Bug reports |
| **Feature Requests** | https://community.n8n.io/c/feature-requests/ | Request features |

### Learning Resources

| Resource | URL | Type |
|----------|-----|------|
| **Official YouTube** | https://www.youtube.com/@n8n-io | Video tutorials |
| **Workflow Templates** | https://n8n.io/workflows/ | Community workflows |
| **n8n Academy** | https://academy.n8n.io/ | Courses |

---

## 🔧 Development Tools

### CLI Tools (This Workshop)

| Tool | Location | Documentation |
|------|----------|---------------|
| **Workflow Manager** | `tools/n8n-workflow-manager.js` | See tool `--help` |

### External Tools

| Tool | URL | Purpose |
|------|-----|---------|
| **n8n Desktop** | https://n8n.io/download/ | Local development |
| **n8n Docker** | https://docs.n8n.io/hosting/installation/docker/ | Self-hosted setup |

---

## 📖 Reading Paths by Goal

### "I'm building my first agent"
1. [critical-bugs.md](critical-bugs.md) (15 min)
2. [development-protocol.md](development-protocol.md) (20 min)
3. [Official Node Reference](https://docs.n8n.io/integrations/builtin/) (as needed)
4. Choose closest template from `workflows/`
5. Follow development protocol

**Total time:** 35 minutes + build time

### "I'm debugging a broken workflow"
1. Check [critical-bugs.md](critical-bugs.md) - Known issue?
2. Check [implementation-guide.md](implementation-guide.md) - Pattern exists?
3. Use workflow manager: `./n8n-workflow-manager.js executions ID 10`
4. Check [Community Forum](https://community.n8n.io/)
5. Document new pattern if discovered

**Time to resolution:** < 30 minutes for known issues

### "I'm optimizing an existing workflow"
1. [implementation-guide.md](implementation-guide.md) - Performance section
2. [Official Best Practices](https://docs.n8n.io/hosting/scaling/)
3. Workflow manager execution analysis
4. Community workflow patterns

**Time:** Varies by complexity

---

## 🔄 Keeping Documentation Updated

### When to Update This Index
- New n8n version released → Check official docs for changes
- New bug discovered → Add to critical-bugs.md
- New agent template created → Add to templates section
- New integration needed → Add to integration guides

### Update Protocol
1. Document new findings in appropriate file
2. Add reference to this index
3. Update "Last Updated" date
4. Commit to version control

---

## 📞 Quick Reference

| Need | Go To |
|------|-------|
| **Known bug?** | [critical-bugs.md](critical-bugs.md) |
| **How to develop?** | [development-protocol.md](development-protocol.md) |
| **Best practices?** | [implementation-guide.md](implementation-guide.md) |
| **Node syntax?** | [Official Node Reference](https://docs.n8n.io/integrations/builtin/) |
| **API docs?** | [n8n API Reference](https://docs.n8n.io/api/) |
| **Community help?** | [n8n Forum](https://community.n8n.io/) |

---

*Last updated: October 7, 2025 | Maintained as part of buyanagent.ai development*
