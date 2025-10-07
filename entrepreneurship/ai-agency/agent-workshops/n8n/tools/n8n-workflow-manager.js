#!/usr/bin/env node

const fs = require('fs').promises;
const path = require('path');
const axios = require('axios');

// Load configuration from environment or use defaults
const API_URL = process.env.N8N_API_URL || 'https://lindonharris.app.n8n.cloud/api/v1';
const API_KEY = process.env.N8N_API_KEY;

if (!API_KEY) {
    console.error('❌ Error: N8N_API_KEY environment variable is required');
    console.error('Please set it with: export N8N_API_KEY="your-api-key"');
    process.exit(1);
}

// API client setup
const api = axios.create({
    baseURL: API_URL,
    headers: {
        'X-N8N-API-KEY': API_KEY,
        'Content-Type': 'application/json'
    }
});

// Color codes for terminal output
const colors = {
    reset: '\x1b[0m',
    bright: '\x1b[1m',
    green: '\x1b[32m',
    yellow: '\x1b[33m',
    blue: '\x1b[34m',
    red: '\x1b[31m',
    cyan: '\x1b[36m'
};

// Helper functions
function log(message, color = 'reset') {
    console.log(`${colors[color]}${message}${colors.reset}`);
}

function error(message) {
    console.error(`${colors.red}❌ Error: ${message}${colors.reset}`);
}

function success(message) {
    log(`✅ ${message}`, 'green');
}

function info(message) {
    log(`ℹ️  ${message}`, 'blue');
}

// Main functions
async function listWorkflows() {
    try {
        info('Fetching workflows...');
        const response = await api.get('/workflows');
        const workflows = response.data.data || response.data;
        
        console.log('\n📋 Available Workflows:\n');
        workflows.forEach((wf, index) => {
            const status = wf.active ? '🟢 Active' : '⚪ Inactive';
            console.log(`${index + 1}. ${colors.bright}${wf.name}${colors.reset}`);
            console.log(`   ID: ${colors.cyan}${wf.id}${colors.reset}`);
            console.log(`   Status: ${status}`);
            console.log(`   Updated: ${new Date(wf.updatedAt).toLocaleString()}`);
            console.log('');
        });
        
        return workflows;
    } catch (err) {
        error(`Failed to list workflows: ${err.message}`);
        throw err;
    }
}

async function downloadWorkflow(workflowId, outputPath = null) {
    try {
        info(`Downloading workflow ${workflowId}...`);
        const response = await api.get(`/workflows/${workflowId}`);
        const workflow = response.data;
        
        // Generate output filename if not provided
        if (!outputPath) {
            const safeName = workflow.name.replace(/[^a-z0-9]/gi, '-').toLowerCase();
            outputPath = `${safeName}-${workflowId}.json`;
        }
        
        // Save full workflow for reference
        const fullPath = outputPath.replace('.json', '-full.json');
        await fs.writeFile(fullPath, JSON.stringify(workflow, null, 2));
        
        // Save clean version for editing
        const cleanWorkflow = {
            name: workflow.name,
            nodes: workflow.nodes,
            connections: workflow.connections,
            settings: workflow.settings || {}
        };
        await fs.writeFile(outputPath, JSON.stringify(cleanWorkflow, null, 2));
        
        success(`Downloaded workflow to: ${outputPath}`);
        info(`Full backup saved to: ${fullPath}`);
        
        return { workflow, outputPath };
    } catch (err) {
        error(`Failed to download workflow: ${err.message}`);
        throw err;
    }
}

async function uploadWorkflow(workflowId, filePath) {
    try {
        info(`Reading workflow from ${filePath}...`);
        const content = await fs.readFile(filePath, 'utf8');
        const workflow = JSON.parse(content);
        
        // Clean the workflow (remove any read-only fields)
        const cleanWorkflow = {
            name: workflow.name,
            nodes: workflow.nodes,
            connections: workflow.connections,
            settings: workflow.settings || {}
        };
        
        info(`Uploading workflow ${workflowId}...`);
        const response = await api.put(`/workflows/${workflowId}`, cleanWorkflow);
        
        const updatedWorkflow = response.data.data || response.data;
        success(`Workflow updated successfully!`);
        info(`Name: ${updatedWorkflow.name}`);
        info(`Updated: ${new Date(updatedWorkflow.updatedAt).toLocaleString()}`);
        
        return updatedWorkflow;
    } catch (err) {
        if (err.response && err.response.data) {
            error(`Upload failed: ${err.response.data.message || JSON.stringify(err.response.data)}`);
        } else {
            error(`Failed to upload workflow: ${err.message}`);
        }
        throw err;
    }
}

async function activateWorkflow(workflowId, activate = true) {
    try {
        info(`${activate ? 'Activating' : 'Deactivating'} workflow ${workflowId}...`);
        const response = await api.patch(`/workflows/${workflowId}`, { active: activate });
        
        success(`Workflow ${activate ? 'activated' : 'deactivated'} successfully!`);
        return response.data.data || response.data;
    } catch (err) {
        error(`Failed to ${activate ? 'activate' : 'deactivate'} workflow: ${err.message}`);
        throw err;
    }
}

async function getWorkflowExecutions(workflowId, limit = 10) {
    try {
        info(`Fetching executions for workflow ${workflowId}...`);
        const response = await api.get('/executions', {
            params: {
                workflowId,
                limit
            }
        });
        
        const executions = response.data.data || response.data;
        console.log(`\n📊 Recent Executions (${executions.length}):\n`);
        
        executions.forEach((exec, index) => {
            const status = exec.finished ? 
                (exec.data.resultData.error ? '❌ Failed' : '✅ Success') : 
                '⏳ Running';
            
            console.log(`${index + 1}. Execution #${exec.id}`);
            console.log(`   Status: ${status}`);
            console.log(`   Started: ${new Date(exec.startedAt).toLocaleString()}`);
            if (exec.data.resultData.error) {
                console.log(`   Error: ${colors.red}${exec.data.resultData.error.message}${colors.reset}`);
            }
            console.log('');
        });
        
        return executions;
    } catch (err) {
        error(`Failed to get executions: ${err.message}`);
        throw err;
    }
}

// Interactive CLI
async function interactive() {
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    const question = (prompt) => new Promise(resolve => readline.question(prompt, resolve));
    
    console.log(`\n${colors.bright}🚀 n8n Workflow Manager${colors.reset}\n`);
    
    while (true) {
        console.log('\nAvailable commands:');
        console.log('1. List workflows');
        console.log('2. Download workflow');
        console.log('3. Upload workflow');
        console.log('4. Activate/Deactivate workflow');
        console.log('5. View executions');
        console.log('6. Exit\n');
        
        const choice = await question('Enter your choice (1-6): ');
        
        try {
            switch (choice) {
                case '1':
                    await listWorkflows();
                    break;
                    
                case '2': {
                    const workflows = await listWorkflows();
                    const index = await question('\nEnter workflow number to download: ');
                    const workflow = workflows[parseInt(index) - 1];
                    if (workflow) {
                        await downloadWorkflow(workflow.id);
                    } else {
                        error('Invalid workflow number');
                    }
                    break;
                }
                
                case '3': {
                    const workflowId = await question('Enter workflow ID: ');
                    const filePath = await question('Enter JSON file path: ');
                    await uploadWorkflow(workflowId, filePath);
                    break;
                }
                
                case '4': {
                    const workflows = await listWorkflows();
                    const index = await question('\nEnter workflow number: ');
                    const workflow = workflows[parseInt(index) - 1];
                    if (workflow) {
                        const activate = !workflow.active;
                        await activateWorkflow(workflow.id, activate);
                    } else {
                        error('Invalid workflow number');
                    }
                    break;
                }
                
                case '5': {
                    const workflowId = await question('Enter workflow ID: ');
                    await getWorkflowExecutions(workflowId);
                    break;
                }
                
                case '6':
                    console.log('\n👋 Goodbye!\n');
                    readline.close();
                    return;
                    
                default:
                    error('Invalid choice');
            }
        } catch (err) {
            // Error already logged in functions
        }
    }
}

// Command line interface
async function main() {
    const args = process.argv.slice(2);
    const command = args[0];
    
    try {
        switch (command) {
            case 'list':
                await listWorkflows();
                break;
                
            case 'download':
                if (!args[1]) {
                    error('Please provide workflow ID: n8n-workflow-manager download <workflow-id> [output-file]');
                    process.exit(1);
                }
                await downloadWorkflow(args[1], args[2]);
                break;
                
            case 'upload':
                if (!args[1] || !args[2]) {
                    error('Please provide workflow ID and file: n8n-workflow-manager upload <workflow-id> <file-path>');
                    process.exit(1);
                }
                await uploadWorkflow(args[1], args[2]);
                break;
                
            case 'activate':
                if (!args[1]) {
                    error('Please provide workflow ID: n8n-workflow-manager activate <workflow-id>');
                    process.exit(1);
                }
                await activateWorkflow(args[1], true);
                break;
                
            case 'deactivate':
                if (!args[1]) {
                    error('Please provide workflow ID: n8n-workflow-manager deactivate <workflow-id>');
                    process.exit(1);
                }
                await activateWorkflow(args[1], false);
                break;
                
            case 'executions':
                if (!args[1]) {
                    error('Please provide workflow ID: n8n-workflow-manager executions <workflow-id> [limit]');
                    process.exit(1);
                }
                await getWorkflowExecutions(args[1], args[2] || 10);
                break;
                
            case 'help':
                console.log(`
${colors.bright}n8n Workflow Manager${colors.reset}

Commands:
  list                              List all workflows
  download <id> [file]              Download workflow to JSON file
  upload <id> <file>                Upload workflow from JSON file
  activate <id>                     Activate a workflow
  deactivate <id>                   Deactivate a workflow
  executions <id> [limit]           View workflow executions
  help                              Show this help message

Interactive mode:
  Run without arguments to enter interactive mode

Examples:
  n8n-workflow-manager list
  n8n-workflow-manager download K1LHiBXjBctayOfe
  n8n-workflow-manager upload K1LHiBXjBctayOfe my-workflow.json
  n8n-workflow-manager activate K1LHiBXjBctayOfe
  n8n-workflow-manager executions K1LHiBXjBctayOfe 20
                `);
                break;
                
            default:
                // No command provided, run interactive mode
                await interactive();
        }
    } catch (err) {
        process.exit(1);
    }
}

// Run the CLI
if (require.main === module) {
    main();
}

module.exports = {
    listWorkflows,
    downloadWorkflow,
    uploadWorkflow,
    activateWorkflow,
    getWorkflowExecutions
};