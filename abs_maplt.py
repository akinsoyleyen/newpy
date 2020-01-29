import webbrowser
from sys import argv

script, adress = argv
adress1 = str.join(sys.argv[1:])
webbrowser.open(f'https://www.google.com/maps/place/{adress1}/')