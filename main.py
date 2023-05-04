# Import webbot
from webbot import Browser

# Create an instance of the chromium browser
web = Browser()

# Go to repl.it
web.go_to("google.com")

# Input prompt for typing (You can't use the shift key in the display)
while True:
    # Ask for key input
    key = input("> ")
    # Type in key input
    web.type(key)
