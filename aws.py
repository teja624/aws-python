#!/usr/bin/env python3
import boto3
import os
import sys
import time
import menugenerator as menu

menu = menu.menu
s3 = boto3.resource('s3')
size = sys.stdout

# intro "animation" and ASCII art
def asciiArt():
    print("Welcome to...")
    time.sleep(1)
    menu.blankSpace(1)
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
    menu.blankSpace(1)
    print("Written by Tom Hulbert")

# menu declerations
mainMenu = ['AWS Functions', 'Setup', 'Exit']
awsMenu = ['S3', 'Other', 'Exit']


# Thanks to Active State user Barry Walker for assistance with window sizing
size.write("\x1b[8;{rows};{cols}t".format(rows=28, cols=150))

menu.clearScreen()
asciiArt()
time.sleep(3)
while True:
    menu.clearScreen()
    print("For first time users select 'Setup'")
    menu.blankSpace(1)
    main = menu.generate('Main Menu', 0, 0, *mainMenu)
    if main == 1:
        menu.clearScreen()
        menu.generate('AWS Functions', 1, 1, *awsMenu)
    elif main == 2:
        os.system('aws configure')
        time.sleep(2)
        menu.clearScreen()
        print("Initial setup is complete")
        menu.time.sleep(2)
    elif main == 3:
        exit()
    else:
        menu.clearScreen()
        print("That is an invalid option")
        time.sleep(2)
