#! python3
# ,ulticlipboard - saves and loads pieces of text to the clipboard
# py.exe mcb.py save <keyword> saves clipboard to keyword
# py.exe mcb.py <keyword> loads keyword to clipboard
# py.exe mcb.py list - copies keywords and content

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argc[1]])

