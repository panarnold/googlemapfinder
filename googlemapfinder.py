#! python
# googlemapfinder.py - shows in the browser map from data of command line
# if argument in command line is empty, script will try to reach the data from the clipboard
# X 2020 Arnold Cytrowski

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.pl/maps/place/' + address)