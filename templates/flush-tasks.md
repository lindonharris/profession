<%*
// Flush completed tasks to archive
const file = app.workspace.getActiveFile();
if (!file) {
    new Notice('No active file');
    return;
}

const content = await app.vault.read(file);
const lines = content.split('\n');

let completedTasks = [];
let newLines = [];
let inArchive = false;
let archiveEndIndex = -1;

// Process the file
for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    
    if (line.includes('<details>')) {
        inArchive = true;
    }
    if (line.includes('</details>')) {
        inArchive = false;
        archiveEndIndex = i;
    }
    
    // If not in archive and line contains completed task
    if (!inArchive && line.match(/^- \[x\]/i)) {
        let taskText = line;
        // Remove original due date but keep completion date and notes
        taskText = taskText.replace(/📅 \d{4}-\d{2}-\d{2}/g, '').trim();
        completedTasks.push(taskText);
    } else if (!inArchive) {
        newLines.push(line);
    }
}

// Rebuild file with archive
if (completedTasks.length > 0 && archiveEndIndex > 0) {
    // Re-read to get archive section
    const originalLines = content.split('\n');
    let finalContent = [];
    let beforeArchive = true;
    let inArchiveSection = false;
    
    for (let i = 0; i < originalLines.length; i++) {
        const line = originalLines[i];
        
        if (line.includes('<details>')) {
            inArchiveSection = true;
            beforeArchive = false;
        }
        
        if (beforeArchive && !line.match(/^- \[x\]/i)) {
            finalContent.push(line);
        } else if (inArchiveSection) {
            finalContent.push(line);
            if (line.includes('</details>')) {
                // Insert completed tasks before closing tag
                finalContent.splice(finalContent.length - 1, 0, 
                    '',
                    `### Flushed on ${tp.date.now("YYYY-MM-DD")}`,
                    ...completedTasks
                );
                inArchiveSection = false;
            }
        }
    }
    
    await app.vault.modify(file, finalContent.join('\n'));
    new Notice(`✅ Flushed ${completedTasks.length} completed task(s) to archive`);
} else if (completedTasks.length === 0) {
    new Notice('No completed tasks to flush');
}
_%><%* tR = "" %>