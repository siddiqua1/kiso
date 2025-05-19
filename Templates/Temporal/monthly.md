---
publish: false
created: 2025-05-18T17:03
updated: 2025-05-18T17:03
---

# Monthly Review:
%% This template Requires the Templater plugin %%
[[2025-M04]] <== <button class="date_button_today">This Month</button> ==> [[2025-M06]]

---

```dataview
TABLE aliases
FROM "Journal"
WHERE aliases != null
AND file.day.year = number(substring(this.file.name, 0, 4))
AND dateformat(date(file.name), "yyyy-MM") = replace(this.file.name, "M", "")
SORT file.day
```

---

```dataview
TABLE WITHOUT ID file.day.weekyear AS Week, highlights
FROM "Journal/Daily"
WHERE highlights != null
AND file.day.year = number(substring(this.file.name, 0, 4))
AND dateformat(date(file.name), "yyyy-MM") = replace(this.file.name, "M", "")
SORT file.day
```
