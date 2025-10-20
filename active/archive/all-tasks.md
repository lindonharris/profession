# All Tasks Overview

## ⚡ High Priority Tasks

```dataview
TABLE WITHOUT ID
  task.text as "Task",
  task.due as "Due Date",
  choice(contains(task.text, "⏫"), "🔴 HIGH", "") as "Priority",
  task.subtasks[0].text as "Key Action"
FROM "active"
WHERE file.tasks
FLATTEN file.tasks as task
WHERE !task.completed AND contains(task.text, "⏫")
SORT task.due ASC
```

## Focus

### Overdue
```tasks
not done
due before today
sort by due
group by folder
hide backlink
```

### Next 7 Days
```tasks
not done
due before in 7 days
sort by due
group by folder
hide backlink
```

---

## 📋 All Active Tasks

### By Folder
```tasks
not done
group by folder
hide backlink
```

### By Due Date
```tasks
not done
has due date
sort by due
group by folder
hide backlink
```

### By Due Date
```tasks
not done
has due date
sort by due
group by folder
hide backlink
```

---

## ✅ Recently Completed

### Today
```tasks
done today
group by folder
hide backlink
```

### This Week
```tasks
done
done after 7 days ago
sort by done reverse
group by folder
hide backlink
```

### Last 20 Tasks
```tasks
done
sort by done reverse
limit 20
group by folder
hide backlink
```

---

## 📊 Task Statistics

### By Status
```tasks
group by done
hide backlink
```

### By File Location
```tasks
not done
group by filename
hide backlink
```

### Tasks with Dependencies
```tasks
not done
description includes depends on
hide backlink
```

---

## 🔍 Special Filters

### Tasks Due Soon
```tasks
not done
due before in 3 days
sort by due
group by folder
hide backlink
```

### Tasks Due This Month
```tasks
not done
due before in 1 month
due after today
sort by due
group by folder
hide backlink
```

### No Due Date
```tasks
not done
no due date
group by folder
hide backlink
```