---
tags: 
publish: false
aliases: 
created: 2025-05-18T17:03
updated: 2025-05-18T17:03
---

# Annual Review:

[[2024-Y]] <== <button class='date_button_today'>This Month</button> ==> [[2026-Y]]

## Aliases

```dataview
TABLE aliases
FROM "Journal"
WHERE aliases != null
WHERE length(aliases) >= 1
WHERE file.day.year = 2025
```

## Highlights

```dataview
TABLE WITHOUT ID dateformat(file.ctime, "yyyy-MM") AS Month, file.day.weekyear AS Week, highlights
FROM "Journal"
WHERE highlights != null
WHERE file.day.year = 2025
SORT file.day.weekyear
```

