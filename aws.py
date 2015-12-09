#!/usr/bin/env python3
import boto3
import os
import sys
import time

s3 = boto3.resource('s3')
size = sys.stdout


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# i'm feeling lazy...
# Start lazy

# blank space generator


def blankSpace(lines):
    blank = "\n"
    print("") if lines <= 1 else print((lines - 1) * blank)

# menu generator
# title = Menu title
# spacing = NO. of lines between options
# *args = name of list that contains the options


class menu:

    def _init_(title, spacing, clear, *args):
        spacing = 0
        title = "Menu"

    def generate(title, spacing, clear, *args):
        blank = "\n"
        if clear == 1:
            clearScreen()
        x = 0
        print(title + ":")
        for a in args:
            x = x + 1
            print(a + "[" + str(x) + "]" + (spacing * blank))
        option = input("Option: ")
        return int(option)
# End lazy


# intro "animation" and ASCII art
def asciiArt():
    print("Welcome to...")
    time.sleep(1)
    blankSpace(1)
    print("      ___           ___           ___                    ___           ___           ___           ___           ___           ___     ")
    print("     /\  \         /\__\         /\  \                  /\  \         |\__\         /\  \         /\__\         /\  \         /\__\    ")
    print("    /::\  \       /:/ _/_       /::\  \                /::\  \        |:|  |        \:\  \       /:/  /        /::\  \       /::|  |   ")
    print("   /:/\:\  \     /:/ /\__\     /:/\ \  \              /:/\:\  \       |:|  |         \:\  \     /:/__/        /:/\:\  \     /:|:|  |   ")
    print("  /::\~\:\  \   /:/ /:/ _/_   _\:\~\ \  \            /::\~\:\  \      |:|__|__       /::\  \   /::\  \ ___   /:/  \:\  \   /:/|:|  |__ ")
    print(" /:/\:\ \:\__\ /:/_/:/ /\__\ /\ \:\ \ \__\          /:/\:\ \:\__\     /::::\__\     /:/\:\__\ /:/\:\  /\__\ /:/__/ \:\__\ /:/ |:| /\__\ ")
    print(" \/__\:\/:/  / \:\/:/ /:/  / \:\ \:\ \/__/          \/__\:\/:/  /    /:/~~/~       /:/  \/__/ \/__\:\/:/  / \:\  \ /:/  / \/__|:|/:/  /")
    print("      \::/  /   \::/_/:/  /   \:\ \:\__\                 \::/  /    /:/  /        /:/  /           \::/  /   \:\  /:/  /      |:/:/  / ")
    print("      /:/  /     \:\/:/  /     \:\/:/  /                  \/__/     \/__/         \/__/            /:/  /     \:\/:/  /       |::/  /  ")
    print("     /:/  /       \::/  /       \::/  /                                                           /:/  /       \::/  /        /:/  /   ")
    print("     \/__/         \/__/         \/__/                                                            \/__/         \/__/         \/__/    ")
    blankSpace(1)
    print("Written by Tom Hulbert")

# menu declerations
mainMenu = ['AWS Functions', 'Setup', 'Exit']
awsMenu = ['S3', 'Other', 'Exit']


# Thanks to Active State user Barry Walker for assistance with window sizing
size.write("\x1b[8;{rows};{cols}t".format(rows=28, cols=150))

clearScreen()
asciiArt()
time.sleep(5)
while True:
    clearScreen()
    print("For first time users select 'Setup'")
    blankSpace(1)
    menuSel = [menu.generate('Main Menu', 0, 0, *mainMenu),
               menu.generate('AWS Functions', 1, 1, *awsMenu)]
    if menuSel[0] == 1:
        clearScreen()
        menuSel[1]
    elif menuSel[0] == 2:
        os.system('aws configure')
    elif menuSel[0] == 3:
        exit()
    else:
        clearScreen()
        print("That is an invalid option")
        time.sleep(2)
