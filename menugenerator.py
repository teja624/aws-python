# i'm feeling lazy...
# Start lazy

# menu generator
# title = Menu title
# spacing = NO. of lines between options
# *args = name of list that contains the options

# clear screen
# a simple function that clears the screen no matter what OS

# blank space
# inserts specified number of blank lines

import os


class menu:

    def _init_(title, spacing, clear, *args, lines):
        spacing = 0
        title = "Menu"
        lines = 1

    def generate(title, spacing, clear, *args):
        if clear == 1:
            menu.clearScreen()
        x = 0
        print(title + ":")
        for a in args:
            x = x + 1
            print(a + "[" + str(x) + "]" + (spacing * "\n"))
        option = input("Option: ")
        return int(option)

    def clearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def blankSpace(lines):
        print("") if lines <= 1 else print((lines - 1) * "\n")
# End lazy
