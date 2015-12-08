import boto3
import os
import sys
import time

s3 = boto3.resource('s3')
size = sys.stdout

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

#i'm feeling lazy...
#Start lazy

#blank space generator
def blankSpace(lines):
    blank = "\n"
    if lines <= 1:
        print("")
    else:
        print((lines - 1) * blank)

#menu generator
def menu(title,spacing,*args):
    blank = "\n"
    x = 0
    if spacing < 1:
        spacing = 1
    print(title + ":")
    for a in args:
        x = x+1
        print(a + "[" + str(x) + "]" + (spacing * blank))
    option = input("Option: ")
    return option
#End lazy


#intro "animation" and ASCII art
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

#menu declerations
mainMenu = ['AWS Functions','Setup','Exit']
awsMenu = ['S3','Other','Exit']



#Thanks to Active State user Barry Walker for assistance with window sizing
size.write("\x1b[8;{rows};{cols}t".format(rows=28,cols=150))

clearScreen()
asciiArt()
time.sleep(5)
clearScreen()
print("For first time users select 'Setup'")
blankSpace(1)
print(menu('Main Menu',1,*mainMenu))
