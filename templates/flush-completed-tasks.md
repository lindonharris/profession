<%*
// Store reference to the view that was active when hotkey was pressed
const activeView = this.app.workspace.activeLeaf.view;
let originalFile = null;

// Get the original file (before template creates new one)
if (activeView && activeView.file) {
    originalFile = activeView.file;
}

// Check if we're in a valid file
if (!originalFile) {
    new Notice('No active file to flush');
    tR = '';
    return;
}

// Only process task files
const validFiles = ['task-manager.md', 'claude-docket.md'];
if (!validFiles.includes(originalFile.name)) {
    new Notice('Flush only works in task-manager or claude-docket');
    tR = '';
    return;
}

// Read and process the original file
const content = await app.vault.read(originalFile);
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

// Update the original file
if (completedTasks.length > 0) {
    await app.vault.modify(originalFile, finalContent.join('\n'));
    new Notice(`✅ Flushed ${completedTasks.length} completed task(s)`);
} else {
    new Notice('No completed tasks to flush');
}

// Handle the unwanted new file Templater creates
setTimeout(async () => {
    // Get the current file (which is the new untitled one)
    const currentFile = tp.file.find_tfile(tp.file.path(true));
    
    // Switch back to original file
    await app.workspace.activeLeaf.openFile(originalFile);
    
    // Delete the untitled file if it exists
    if (currentFile && (currentFile.name.includes('Untitled') || currentFile.path === tp.file.path(true))) {
        try {
            await app.vault.delete(currentFile);
        } catch (e) {
            // Silent fail if already deleted
        }
    }
}, 100);

// Don't insert any content
tR = '';
_%>