import boto3
import os
import sys
import time

s3 = boto3.resource('s3')


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def asciiArt():
    print("Welcome to...")
    time.sleep(1)
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
    print("\nWritten by Tom Hulbert")
#Thanks to active state user Barry Walker for assistance with window sizing
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=28,cols=150))

clearScreen()
asciiArt()
time.sleep(10)
clearScreen()
