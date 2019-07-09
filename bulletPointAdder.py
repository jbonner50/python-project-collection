#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip


text = pyperclip.paste()

#separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i] # add star in front of string

text = '\n'.join(lines) # adds a new line before each *

pyperclip.copy(text)
