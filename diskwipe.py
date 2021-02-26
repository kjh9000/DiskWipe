#!/usr/bin/python3
###############################################
#  diskwipe.py - a simple disk wiping program #
#         http://github.com/kjh9000           #
###############################################

import os

# Inform the user where the new file will be placed, and prompts the user for 
# any desired change
print("The temporary file will be created in " + os.getcwd() + ".")
answer = input("Is this the desired path? (Y/n): " )
location = ''
flag = 0
while flag == 0:
    try:
        if answer =='n':
            location = input("Please enter the desired path, or nothing (hit " + 
            "the enter key to accept the default (" + os.getcwd() + ").")
        if location == '':
            location = os.getcwd()
            flag = 1
        location = "/" + location
        os.chdir(location)
        flag = 1
    except FileNotFoundError:
        print("Path error.")
        continue

# Prompts user to name the file, or sets the default name
filename = input("Give your temporary file a name (default is temp.txt): ")
if filename == '':
    filename = 'temp.txt'

# Prompts user for file size, sets to a default of 1GB if no number is given
size = ''
while type(size) != int: # A check to be certain a whole number is passed
    try:
        size = input("How big? A number to specify the size in GB (default" +
        " is about 1GB):")
        if size =='':
            size =  1
        else:
            size = int(size)
    except ValueError:
        print("Invalid size. Whole numbers only please.")
        continue

# Prompts for file autoremoval
autorem = input("Do you want the program to delete the temporary file for you? (y/N): ")

# Creates the file then writes zeros and ones to it 
zerosandones = ''
print("Writing to file...")
with open(os.getcwd() + "/" + filename, 'w') as fo:
    for i in range(50000 * int(size)):
        """This huge block of zeros and ones is much faster than generating it
        with a loop. You might make it even faster by adding more zeros and ones
        and reducing the range number in the for loop. Of course, if you did 
        that the size will probably no longer be in 1GB increments."""
        fo.write("0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                0101010101010101010101010101010101010101010101010101010101\
                01010101010101010101")

# Removes the file if desired
if autorem == 'y' or autorem == 'Y':
    os.remove(filename)

print("\nDone.")
