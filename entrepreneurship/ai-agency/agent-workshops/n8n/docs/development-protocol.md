# n8n Development Protocol

*Last Updated: August 4, 2025*

## Purpose

This protocol prevents common errors and ensures systematic development of n8n workflows. Based on hard-won lessons from production debugging sessions.

## Prerequisites Setup

### Environment Variables (One-Time Setup)
```bash
# Add to your ~/.bashrc or ~/.zshrc
export N8N_API_URL="https://lindonharris.app.n8n.cloud/api/v1"
export N8N_API_KEY="your-api-key-here"

# Verify setup
echo $N8N_API_URL  # Should show full URL with /api/v1
echo $N8N_API_KEY  # Should show your key
```

### Tool Verification
```bash
# Test the workflow manager
./n8n-workflow-manager.js list

# Should show workflows without errors
# If errors occur, check environment variables above
```

---

## Development Protocols

### 🔄 Standard Development Cycle

**For new workflow development:**

```bash
# 1. List available workflows
./n8n-workflow-manager.js list

# 2. Download template or existing workflow
./n8n-workflow-manager.js download WORKFLOW_ID

# 3. Edit the generated *-WORKFLOW_ID.json file (NOT the -full.json)
# 4. Upload changes
./n8n-workflow-manager.js upload WORKFLOW_ID edited-workflow.json

# 5. Test and verify
./n8n-workflow-manager.js executions WORKFLOW_ID 10
```

### ⚡ Surgical Precision Protocol

**For modifying WORKING workflows (CRITICAL):**

```bash
# 1. Download current working version
./n8n-workflow-manager.js download WORKING_WORKFLOW_ID

# 2. IMMEDIATELY create timestamped backup
cp workflow-name-WORKING_WORKFLOW_ID.json BACKUP-$(date +%s).json

# 3. Make EXACTLY ONE minimal change
#    - Change only what's absolutely necessary
#    - Do NOT "improve" other parts
#    - Do NOT change working nodes

# 4. Upload and test immediately
./n8n-workflow-manager.js upload WORKING_WORKFLOW_ID workflow-name-WORKING_WORKFLOW_ID.json

# 5. Test the ONE change
#    - If success: document change, continue
#    - If failure: IMMEDIATELY restore backup
./n8n-workflow-manager.js upload WORKING_WORKFLOW_ID BACKUP-timestamp.json
```

### 🚨 Emergency Rollback Protocol

```bash
# If workflow breaks and you need to restore immediately:
./n8n-workflow-manager.js upload WORKFLOW_ID BACKUP-timestamp.json

# Or restore from production folder:
./n8n-workflow-manager.js upload WORKFLOW_ID workflows/project/production/last-working-version.json
```

---

## Error Response Protocols

### Step 1: Error Pattern Recognition

Consult the [Error Pattern Recognition Database](./n8n-hard-won-lessons.md#error-pattern-recognition-database) first.

**Common Patterns:**
- `"Unknown error at JsTaskRunnerSandbox"` → Code node issue (use Set node)
- `"405 Not Allowed"` → API URL missing /api/v1
- `"string found, object expected"` → Remove JSON.stringify()
- `"Invalid point ID"` → Convert IDs to strings

### Step 2: Systematic Debugging

```bash
# 1. Check execution details
./n8n-workflow-manager.js executions WORKFLOW_ID 5

# 2. Download current state for analysis
./n8n-workflow-manager.js download WORKFLOW_ID

# 3. Create debug version with minimal changes
# 4. Test single node or connection at a time
# 5. Document findings in hard-won-lessons.md
```

### Step 3: Known Solution Application

**n8n Cloud Code Node Issues:**
- Replace Code nodes with Set nodes
- Use HTTP Request nodes for API calls
- Never use complex JavaScript on n8n Cloud

**Boolean Logic Issues:**
- Replace IF nodes with Switch nodes
- Use string comparison instead of boolean
- Prepare routing in Code/Set node first

---

## Node-Specific Best Practices

### ✅ Preferred Nodes (Cloud-Safe)
- **Set Node** - For data transformation instead of Code
- **HTTP Request** - For API calls instead of Code
- **Switch Node** - For routing instead of IF
- **Google Sheets** - Instead of Notion (more reliable)
- **Merge Node** - For combining data flows

### ❌ Problematic Nodes (Cloud)
- **Code Node** - Fails with sandbox errors
- **IF Node** - Boolean comparison bugs
- **Notion Node** - Property mapping failures

### 📋 Data Handling Patterns

```javascript
// ID handling (critical for APIs)
String(tweetId)  // Always convert to string

// Property access with fallbacks
$json['Property Name'] || 'default'

// URL extraction
const urlMatch = text.match(/https?:\/\/[^\s]+/);
const url = urlMatch ? urlMatch[0] : 'no-url';
```

---

## Quality Assurance Checkpoints

### Before Upload Checklist
- [ ] Only modified what was necessary
- [ ] Backed up working version
- [ ] No Code nodes on n8n Cloud workflows
- [ ] No IF nodes with boolean comparisons
- [ ] String conversion for all IDs
- [ ] Fallback values for all dynamic properties

### After Upload Verification
- [ ] Workflow uploads without API errors
- [ ] Manual test execution succeeds
- [ ] Check actual output (not just "success" status)
- [ ] Verify end-to-end functionality
- [ ] Document any new patterns discovered

### Production Deployment
- [ ] Save working version to production folder
- [ ] Update workflow documentation
- [ ] Test with real data
- [ ] Monitor for 24 hours
- [ ] Update hard-won lessons if new issues found

---

## Emergency Contacts and Resources

### Key Documentation
- **[Hard-Won Lessons](./n8n-hard-won-lessons.md)** - Comprehensive error database
- **[Workflow Debugging Checklist](./workflow-debugging-checklist.md)** - Step-by-step procedures
- **[Error Handling Guide](./error-handling-guide.md)** - Recovery strategies

### Tool Locations
- **Workflow Manager**: `./n8n-workflow-manager.js`
- **Production Workflows**: `workflows/*/production/`
- **Development Workflows**: `workflows/*/development/`

---

## Protocol Violations and Consequences

### ⚠️ WARNING: Never Do This
1. **Use curl instead of workflow manager** → API errors, no backups
2. **Modify multiple nodes simultaneously** → Unable to isolate failures
3. **Skip backup creation** → Cannot recover from failures
4. **Ignore error patterns** → Waste hours on known issues
5. **Deploy without testing** → Production outages

### 🚫 CRITICAL: These Actions Are Forbidden
1. **Upload workflows without backups**
2. **Use Code nodes on n8n Cloud production**
3. **Modify working workflows without singular precision**
4. **Ignore environment variable validation errors**

---

## Success Metrics

### Development Velocity
- **Time to identify error**: < 5 minutes (using pattern database)
- **Time to resolution**: < 30 minutes (using known solutions)
- **Rollback time**: < 2 minutes (using backup protocol)

### Quality Metrics
- **Zero data loss** through backup protocols
- **Zero prolonged outages** through surgical precision
- **100% error pattern documentation** for future prevention

---

*This protocol is living documentation. Update it whenever new patterns or procedures are discovered.*