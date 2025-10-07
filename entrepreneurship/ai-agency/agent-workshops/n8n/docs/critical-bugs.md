# Critical n8n Bugs & Solutions

**Purpose:** Platform bugs that will break your agents if you don't know about them
**Source:** 6 months of production n8n debugging and ~30 workflow iterations
**Last Updated:** October 7, 2025
**Status:** Production-validated solutions

---

## ⚠️ READ THIS BEFORE BUILDING ANY WORKFLOW

These are **platform bugs** in n8n itself, not configuration errors. They will break your workflows even if your logic is perfect. Each bug has a proven workaround.

---

## Bug #1: IF Node Boolean Comparison Always Returns FALSE 🔴

### The Problem
IF nodes with boolean comparisons **always evaluate to FALSE**, regardless of the actual value.

### Symptoms
- Routing logic fails even with obvious true conditions
- Always goes to false branch
- No error messages - silent failure
- Affects ALL boolean comparisons (true/false, 1/0, etc.)

### Example of Broken Code
```javascript
// This will ALWAYS go to false branch
IF Node:
  Value 1: {{ $json.isValid }}
  Operation: Equal
  Value 2: true
```

### The Solution
**Replace ALL IF nodes with Switch nodes using string comparison:**

```javascript
// STEP 1: In Code/Set node before Switch:
return { routing: success ? 'valid' : 'invalid' }

// STEP 2: In Switch node:
// Value 1: ={{ $json.routing }}
// Add rules:
//   - Output 0: routing === "valid"
//   - Output 1: routing === "invalid"
```

### When This Matters
- **Every routing decision in your workflow**
- Email filtering (spam vs not spam)
- Lead qualification (qualified vs not qualified)
- Error handling (success vs failure)

**Status:** Fundamental n8n bug, no fix planned
**Workaround Reliability:** 100% - works in all scenarios

---

## Bug #2: Notion Node Property Mapping Failure 🔴

### The Problem
Notion node fails to populate database properties despite showing "success" execution status. Only the title field works.

### Symptoms
- Workflow shows success ✅
- Title field populates correctly
- ALL other properties return empty/null
- No error messages
- Even hardcoded static values fail

### Example of Broken Code
```json
// This shows success but doesn't actually save properties
Notion Node:
  Operation: Create database item
  Database: Your Database
  Properties:
    - Title: Works fine ✅
    - Status: Empty (even with static "Active") ❌
    - Date: Empty (even with hardcoded date) ❌
    - Tags: Empty ❌
```

### The Solution
**Option 1: Use Google Sheets instead**
```javascript
// Google Sheets node works reliably
Google Sheets Node:
  Operation: Append or update row
  Spreadsheet: Your Sheet
  Values: All properties map correctly ✅
```

**Option 2: Use direct Notion API via HTTP Request**
```javascript
HTTP Request Node:
  Method: POST
  URL: https://api.notion.com/v1/pages
  Headers:
    Authorization: Bearer YOUR_NOTION_API_KEY
    Content-Type: application/json
    Notion-Version: 2022-06-28
  Body:
    {
      "parent": { "database_id": "YOUR_DB_ID" },
      "properties": {
        "Name": { "title": [{ "text": { "content": "{{ $json.title }}" }}] },
        "Status": { "select": { "name": "{{ $json.status }}" } }
      }
    }
```

### When This Matters
- **Invoice Chaser**: Tracking invoice status in database
- **Lead Qualification**: Storing lead scores
- **Expense Manager**: Categorizing expenses
- Any workflow that needs structured data storage

**Status:** Confirmed n8n node bug (tested with static values)
**Workaround Reliability:** 100% - Google Sheets is production-stable

---

## Bug #3: Variable Scoping After Routing Nodes 🟡

### The Problem
`$json` becomes **empty** after passing through IF, Switch, or Merge nodes.

### Symptoms
- Data accessible before routing node
- `$json` is empty after routing node
- Expressions like `{{ $json.field }}` return undefined
- No error - silent empty values

### Example of Broken Code
```javascript
// Before routing:
Email Trigger → $json.subject = "Important Email" ✅

// Routing node:
Switch Node (routes by email type)

// After routing:
Email Send → {{ $json.subject }} = undefined ❌
```

### The Solution
**Always reference the source node explicitly:**

```javascript
// Instead of:
{{ $json.subject }}  ❌

// Use:
{{ $node["Email Trigger"].json.subject }}  ✅

// Or for item 0 specifically:
{{ $node["Email Trigger"].json[0].subject }}  ✅
```

### When This Matters
- **Every workflow with routing logic**
- Email Sweeper (routing by sender)
- Newsletter Digester (routing by newsletter type)
- Invoice Chaser (routing by payment status)
- Lead Qualification (routing by score)

**Status:** n8n variable scoping design limitation
**Workaround Reliability:** 100% - node references always work

---

## Bug #4: Email Parameter Naming (`text` vs `message`) 🟡

### The Problem
n8n emailSend nodes use `"message"` parameter for body text, NOT `"text"`. Using `"text"` sends blank emails.

### Symptoms
- Workflow shows success ✅
- Email sends
- **Email body is completely blank**
- Subject line works fine
- No error messages

### Example of Broken Code
```json
// This sends BLANK emails:
Email Send Node:
  {
    "subject": "{{ $json.subject }}",
    "text": "{{ $json.body }}"  ❌
  }
```

### The Solution
```json
// This works correctly:
Email Send Node:
  {
    "subject": "{{ $json.subject }}",
    "message": "{{ $json.body }}"  ✅
  }
```

### When This Matters
- **Email Sweeper**: Confirmation emails
- **Newsletter Digester**: Daily digest emails
- **Invoice Chaser**: Payment reminders
- **Any agent that sends emails**

**Status:** n8n parameter naming inconsistency
**Workaround Reliability:** 100% - use "message" always

---

## Bug #5: n8n Cloud Code Node Sandbox Errors 🟠

### The Problem
Code nodes fail on n8n Cloud with cryptic "JsTaskRunnerSandbox" errors, even with valid JavaScript.

### Symptoms
- Error: "Unknown error at JsTaskRunnerSandbox"
- Same code works in local n8n
- Simple JavaScript operations fail
- Complex operations completely broken

### The Solution
**Replace Code nodes with Set nodes or HTTP Request nodes:**

```javascript
// Instead of Code node with:
const result = items.map(item => ({
  transformed: item.json.value * 2
}));
return result;

// Use Set node:
Field Name: transformed
Value: ={{ $json.value * 2 }}
```

For API calls:
```javascript
// Instead of Code node with fetch():
const response = await fetch(url, options);

// Use HTTP Request node directly
```

### When This Matters
- **Any workflow running on n8n Cloud** (not self-hosted)
- Data transformations
- API integrations
- Complex logic

**Status:** n8n Cloud sandbox limitation
**Workaround Reliability:** 95% - Set nodes cover most use cases

---

## Bug #6: Workflow "Success" ≠ Functional Success 🔴

### The Problem
n8n shows green "success" execution status even when the workflow **silently failed** to perform its intended function.

### Symptoms
- Execution shows ✅ success
- No error messages
- **Nothing actually happened**
- Destination systems unchanged

### Example
```
Workflow: Save to Google Sheets
Execution Status: ✅ Success
Google Sheet: No new rows added ❌
```

### The Solution
**Always verify end-to-end results:**

1. **Check actual destination**
   - Open Google Sheet → Verify row exists
   - Open Notion database → Verify page created
   - Check email inbox → Verify email received

2. **Use n8n API for truth**
   ```bash
   ./n8n-workflow-manager.js executions WORKFLOW_ID 10
   # Look at actual output data, not just status
   ```

3. **Add verification nodes**
   ```javascript
   // After critical operation, add verification:
   HTTP Request → GET the just-created resource
   IF (resource exists) → Continue
   ELSE → Send alert email
   ```

### When This Matters
- **Every production workflow**
- Customer-facing agents
- Financial operations (Invoice Chaser)
- Data integrity operations (Expense Manager)

**Status:** n8n execution reporting design
**Workaround Reliability:** 100% - always verify actual outcomes

---

## Bug #7: n8n API Deployment Strictness 🟡

### The Problem
n8n API rejects workflows with ANY extra properties in the JSON, even if those properties are ignored.

### Symptoms
- API Error 400: "Unknown field: X"
- Workflow exports from n8n contain extra fields
- Manually edited JSON fails to upload

### Example of Broken Code
```json
// This fails API upload:
{
  "name": "My Workflow",
  "nodes": [...],
  "connections": {...},
  "id": "123",  ❌ Extra field
  "active": true,  ❌ Extra field
  "createdAt": "2025-01-01",  ❌ Extra field
  "settings": {
    "executionOrder": "v1",
    "saveDataErrorExecution": "all"  ❌ Extra setting
  }
}
```

### The Solution
**Clean workflow JSON before upload:**

```javascript
// Workflow manager tool does this automatically:
./n8n-workflow-manager.js upload ID workflow.json

// Or manually clean:
const clean = {
  name: workflow.name,
  nodes: workflow.nodes,
  connections: workflow.connections,
  settings: { executionOrder: "v1" }  // ONLY allowed setting
};
```

### When This Matters
- **Deploying workflows via API**
- **Programmatic workflow updates**
- **Automated deployment pipelines**

**Status:** n8n API validation strictness
**Workaround Reliability:** 100% - workflow manager tool handles this

---

## Summary Checklist

Before building ANY workflow, remember:

- [ ] ❌ NO IF nodes with boolean comparisons → Use Switch nodes
- [ ] ❌ NO Notion node for property mapping → Use Google Sheets
- [ ] ✅ ALWAYS use `$node["Name"].json` after routing
- [ ] ✅ ALWAYS use `"message"` parameter for email body
- [ ] ❌ NO Code nodes on n8n Cloud → Use Set/HTTP Request nodes
- [ ] ✅ ALWAYS verify actual output, not just execution status
- [ ] ✅ ALWAYS clean JSON before API upload (or use workflow manager)

---

## Where to Get Help

1. **Known issue?** → Check this document
2. **New pattern?** → Check [implementation-guide.md](implementation-guide.md)
3. **Still stuck?** → [n8n Community Forum](https://community.n8n.io/)
4. **Found new bug?** → Document it here and in n8n-sandbox repo

---

## Source Documentation

These bugs were discovered and validated through:
- 30+ workflow iterations
- Production debugging sessions
- Static value testing to isolate node bugs
- End-to-end validation protocols

**Full research:** [n8n-sandbox repository](https://github.com/lindonharris/n8n-sandbox)
**Hard-won lessons:** `/docs/n8n-hard-won-lessons.md`
**Debugging protocols:** `/docs/workflow-debugging-checklist.md`

---

*Last updated: October 7, 2025 | Add new discoveries as they're validated*
