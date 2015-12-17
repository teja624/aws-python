#!/usr/bin/env python3
import sys
import os
import time
import menugenerator as menu
# TODO: Turn follow mess into lib
boto3Status = 0
awscliStatus = 0
commands = 'pip3 install'
packages = ['boto3','awscli']
try:
    import boto3
    boto3Status = 1
except ImportError:
    boto3Status = 0

try:
    import awscli
    awscliStatus = 1
except ImportError:
    awscliStatus = 0

if boto3Status:
    print("found lib boto3")
else:
    if os.name == 'nt':
        print("windows interface")
        os.system(commands + ' --install-option="--prefix=$HOME/local" ' + packages[0])
        #pip install --install-option="--prefix=$HOME/local" boto3
        time.sleep(1)
    else:
        os.system("sudo" + commands + packages[0])
    import boto3
if awscliStatus:
    print("found lib awscli")
else:
    if os.name == 'nt':
        print("windows interface")
        os.system(commands + ' --install-option="--prefix=$HOME/local" ' + packages[0])
        #pip install --install-option="--prefix=$HOME/local" boto3
        time.sleep(1)
    else:
        os.system("sudo" + commands + packages[0])
time.sleep(1)

menu = menu.menu
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

# menu declerations (it does actually support more than 3 listable items)
mainMenu = ['AWS Functions', 'Setup', 'Exit']
awsMenu = ['S3', 'Other', 'Exit']
s3Menu = ['Upload or Download Files', 'Modify or View Buckets']
bucketsMenu = ['List All Buckets', 'Create Bucket', 'Delete Bucket']


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
        submain1 = menu.generate('AWS Functions', 1, 1, *awsMenu)
        if submain1 == 1:
            menu.clearScreen()
            s3 = boto3.resource('s3')
            s3main = menu.generate('S3 Functions', 1, 1, *s3Menu)
            if s3main == 1:
                menu.clearScreen()
                time.sleep(1)
            elif s3main == 2:
                bucketmain = menu.generate('Bucket Functions', 1, 1, *bucketsMenu)
                if bucketmain == 1:
                    menu.clearScreen()
                    for bucket in s3.buckets.all():
                        print(bucket.name)
                    input("Press Enter to continue...")
                elif bucketmain == 2:
                    menu.clearScreen()
                    print("second option")
                    input("Press Enter to continue...")
                elif bucketmain == 2:
                    menu.clearScreen()
                    print("third option")
                    input("Press Enter to continue...")
            time.sleep(1)
        if submain1 == 2:
            menu.clearScreen()
            print(awsMenu[1])
            time.sleep(1)
        if submain1 == 3:
            menu.clearScreen()
            print(awsMenu[2])
            time.sleep(1)
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
        print("Please enter a valid option")
        time.sleep(2)
