'''
This helper is intended to copy the drop down of a 
module on Canvas and convert it into Markdown for use
in my obsidian notes
'''
from typing import List, Tuple

def canvas_filter(s: str) -> bool:
    if len(s) < 3:
        return False
    if s[0].isnumeric():
        return True
    if s[0] == 'L' and s[1].isnumeric():
        return True
    return False

def to_logseq(s: list[str]) -> list[str]:
    lines = list(filter(canvas_filter, s))
    lines[0] = f'- # {lines[0]}'
    for i in range(1, len(lines)):
        lines[i] = f'\t- ## {lines[i]}'

    return lines

def extract_module(s: List[str]) -> List[Tuple[str, List[str]]]:
    '''
    List of (module_name, module_parts)

    input should be derived from going to canvas -> modules -> expand all

    then ctrl + A, ctrl + C
    '''

    res = []

    for i, line in enumerate(s):
        if i == 0:
            continue
        prev = s[i - 1]
        if len(line.strip()) > 0 and prev == line:
            res.append((line.strip(), []))
        if prev.strip() == "Page":
            res[-1][1].append(line.strip())
    return res


def to_obsidian(class_prefix: str, modules: List[Tuple[str, List[str]]]) -> List[str]:
    lines = []

    lines.append("# Modules\n\n")
    lines.append(f"- [[{class_prefix} Syllabus|Syllabus]]\n")
    for (module, lectures) in modules:
        lines.append(f"- [[{class_prefix} {module}|{module}]]\n")

    lines.append("\n# Modules (Detailed)\n\n")

    for (module, lectures) in modules:
        lines.append(f"- [[{class_prefix} {module}|{module}]]\n")
        for lecture in lectures:
            lines.append(f"\t- [[{class_prefix} {module} - {lecture}|{lecture}]]\n")
    return lines

if __name__ == '__main__':
    lines = []
    with open("input.txt", 'r') as f:
        lines = to_obsidian("CS 6290", extract_module(f.readlines()))
    with open("output.txt", 'w') as f:
        f.writelines(lines)
