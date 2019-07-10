#! python3
# Gets a street address from the command line arguments or clipboard.
# Opens the web browser to the Google Maps page for the address.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # get address from command line
    address = '+'.join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()
    address.replace(" ", "+")

webbrowser.open('https://www.google.com/maps/place/' + address)


