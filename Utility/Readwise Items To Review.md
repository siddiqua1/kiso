---
created: 2023-03-10 2016
updated: 2025-05-18T16:58
---

filter_date:: 2024-03-31

## Unprocessed Items

```dataview
list rows.file.link
FROM "Readwise"
WHERE file.name != "Readwise Syncs"
WHERE file.day > date(this.filter_date)
AND file.day != null
AND file.day != date("2023-03-15")
GROUP BY file.day
SORT file.day
```

