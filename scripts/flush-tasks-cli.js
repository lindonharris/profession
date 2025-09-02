#!/usr/bin/env node

// CLI script to flush completed tasks in Obsidian files
const fs = require('fs');
const path = require('path');

// Configuration
const OBSIDIAN_PATH = '/mnt/c/Users/lindo/Documents/Obsidian/active';
const FILES = {
  'task-manager': path.join(OBSIDIAN_PATH, 'task-manager.md'),
  'claude-docket': path.join(OBSIDIAN_PATH, 'claude-docket.md'),
  'tm': path.join(OBSIDIAN_PATH, 'task-manager.md'), // shortcuts
  'cd': path.join(OBSIDIAN_PATH, 'claude-docket.md')
};

function flushTasks(filePath) {
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    return false;
  }

  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split('\n');
  
  let completedTasks = [];
  let finalContent = [];
  let inArchive = false;
  
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    
    if (line.includes('<details>')) {
      inArchive = true;
      finalContent.push(line);
      continue;
    }
    
    if (line.includes('</details>')) {
      if (completedTasks.length > 0) {
        finalContent.push('');
        finalContent.push(`### Flushed on ${new Date().toISOString().split('T')[0]}`);
        completedTasks.forEach(task => finalContent.push(task));
      }
      finalContent.push(line);
      inArchive = false;
      continue;
    }
    
    if (!inArchive && line.match(/^[\s]*- \[x\]/i)) {
      let taskText = line.replace(/📅 \d{4}-\d{2}-\d{2}/g, '').trim();
      completedTasks.push(taskText);
    } else {
      finalContent.push(line);
    }
  }
  
  if (completedTasks.length > 0) {
    fs.writeFileSync(filePath, finalContent.join('\n'));
    console.log(`✅ Flushed ${completedTasks.length} task(s) in ${path.basename(filePath)}`);
    return true;
  } else {
    console.log(`No completed tasks to flush in ${path.basename(filePath)}`);
    return false;
  }
}

// Parse command line arguments
const args = process.argv.slice(2);

if (args.length === 0 || args[0] === '--help' || args[0] === '-h') {
  console.log(`
Flush completed tasks to archive in Obsidian files

Usage:
  flush-tasks <file>        Flush tasks in specific file
  flush-tasks all           Flush tasks in all files
  
Files:
  task-manager, tm          Task Manager
  claude-docket, cd         Claude Docket
  all                       Both files
  
Examples:
  flush-tasks tm            Flush task-manager.md
  flush-tasks claude-docket Flush claude-docket.md
  flush-tasks all           Flush both files
`);
  process.exit(0);
}

const target = args[0].toLowerCase();

if (target === 'all') {
  let flushed = false;
  flushed = flushTasks(FILES['task-manager']) || flushed;
  flushed = flushTasks(FILES['claude-docket']) || flushed;
  if (!flushed) {
    console.log('No tasks were flushed in any file');
  }
} else if (FILES[target]) {
  flushTasks(FILES[target]);
} else {
  console.error(`Unknown target: ${target}`);
  console.log('Use --help for usage information');
  process.exit(1);
}