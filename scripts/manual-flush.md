# Manual Flush Script

To flush completed tasks manually:

1. Open the Developer Console:
   - Windows/Linux: `Ctrl + Shift + I`
   - Mac: `Cmd + Option + I`

2. Go to the Console tab

3. Copy and paste this entire script:

```javascript
(async () => {
  const file = app.workspace.getActiveFile();
  if (!file) {
    new Notice('No active file');
    return;
  }
  
  const content = await app.vault.read(file);
  const lines = content.split('\n');
  
  let completedTasks = [];
  let finalContent = [];
  let inArchive = false;
  let archiveStarted = false;
  
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    
    if (line.includes('<details>')) {
      inArchive = true;
      archiveStarted = true;
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
  
  if (completedTasks.length > 0 && archiveStarted) {
    await app.vault.modify(file, finalContent.join('\n'));
    new Notice(`✅ Flushed ${completedTasks.length} completed task(s)`);
  } else if (completedTasks.length === 0) {
    new Notice('No completed tasks to flush');
  } else {
    new Notice('No archive section found');
  }
})();
```

4. Press Enter to run it

This will flush all completed tasks in the currently active file to the archive.