#! python3
# str_project.py - Adds Wikipedia bullet points to the start

import pyperclip as ppc
text = ppc.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i]='* '+lines[i]
    text='\n'.join(lines)
ppc.copy(text)

print(ppc.paste())