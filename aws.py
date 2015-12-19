#!/usr/bin/env python3
import sys, os, time, subprocess, menugenerator as menu
# TODO: Turn follow mess into lib
debug = 1
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
    print("found lib " + packages[0])
else:
    if os.name == 'nt':
        print("windows interface")
        os.system(commands + ' --install-option="--prefix=$HOME/local" ' + packages[0])
        #pip install --install-option="--prefix=$HOME/local" boto3
        time.sleep(1)
    else:
        os.system("sudo" + commands + packages[0])

if awscliStatus:
    print("found lib " + packages[1])
else:
    if os.name == 'nt':
        print("windows interface")
        os.system(commands + ' --install-option="--prefix=$HOME/local" ' + packages[1])
        #pip install --install-option="--prefix=$HOME/local" boto3
        time.sleep(1)
    else:
        os.system("sudo" + commands + packages[1])
if debug:
    time.sleep(1)

import boto3
import botocore

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

# menu declerations (it does support more than 3 listable items)
mainMenu = ['AWS Functions', 'Setup', 'Exit']
awsMenu = ['S3', 'Other', 'Exit']
s3Menu = ['Upload or Download Files', 'Modify or View Buckets']
bucketsMenu = ['List All Buckets', 'Initialise a New Bucket', 'Delete Bucket','Check the Status of a Bucket']


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
                    print("Initialise a New Bucket")
                    print("\nPlease Note:\nThe name that you choose must be unique across all existing bucket names in Amazon S3.\nOne way to help ensure uniqueness is to prefix your bucket names with the name of your organization.\n")
                    bucketName = input("Enter Name For New Bucket: ")
                    menu.blankSpace(1)
                    try:
                        print("Initialising New Bucket as " + bucketName + "...")
                        s3.create_bucket(Bucket='mybucket')
                        print("New Bucket "  + bucketName + " Initialised")
                    except Exception:
                        menu.clearScreen()
                        print("An error has occured, it is likely a bucket already exists with this name...")
                    time.sleep(2)
                elif bucketmain == 3:
                    menu.clearScreen()
                    print("Delete Bucket")
                    bucketName = input("Name of Bucket: ")
                    if input("Are you sure you want to delete bucket" + bucketName +"? [Y/N]") == 'Y' or 'y':
                        bucket = s3.Bucket(bucketName)
                        print("Deleting keys in " + bucketName)
                        for key in bucket.objects.all():
                            key.delete()
                        bucket.delete()
                        print("Bucket " + bucketName +" has been deleted.")
                    else:
                        print("Bucket " + bucketName +" has not been deleted.")
                    time.sleep(1)
                    input("Press Enter to continue...")
                elif bucketmain == 4:
                    menu.clearScreen()
                    bucketName = input("Check Status of Bucket: ")
                    bucket = s3.Bucket(bucketName)
                    exists = True
                    try:
                        s3.meta.client.head_bucket(Bucket='mybucket')
                        print("Bucket is up and functional")
                    except botocore.exceptions.ClientError as e:
                        error_code = int(e.response['Error']['Code'])
                        if error_code == 404:
                            exists = False
                            print("The bucket you requested does not exist or you do not have access to it.")
                    print(exists)
                    time.sleep(2)
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
