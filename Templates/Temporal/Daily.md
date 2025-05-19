---
tags: 
publish: false
aliases: 
created: 2025-05-18T17:03
updated: 2025-05-18T17:05
---
<% tp.file.cursor(0) %>



## On This Day...

```dataview
LIST 
FROM "Journal/Daily"
WHERE dateformat(file.day, "MM-dd") = dateformat(this.file.day, "MM-dd")
AND file.day != this.file.day
```

---

## Notes Created Today

```dataview
TABLE created, updated as modified, tags
FROM "" AND !"Journal" AND !"Templates"
WHERE contains(dateformat(file.ctime, "yyyy-MM-dd"), dateformat(this.file.day, "yyyy-MM-dd"))
```

---

## Highlights For Today

```dataview
TABLE highlights
FROM "Journal/Daily"
WHERE this.file.name = file.name
AND highlights != null
```

---

[[<% tp.date.now("YYYY-MM-DD", -1, tp.file.title, "YYYY-MM-DD") %>]] <== <button class="date_button_today">Today</button> ==> [[<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>]]

## Top of Mind

---

<%* if (tp.date.now("M-D") == "1-1") { %>
**Make Yearly Note**
<%* } _%>
<%* if (tp.date.now("D") == 1) { %>
**Make Monthly Note**
<%* } _%>
<%* if (tp.date.now("ddd") == "Sun") { %>
**Make Weekly Note**
<%* } _%>