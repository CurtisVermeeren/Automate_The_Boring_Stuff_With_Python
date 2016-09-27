#! python3
# Launches a map in the browser using an address from the Command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #Get address from the command line.
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
