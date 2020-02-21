#!/usr/bin/env python
#Filename: Challenge04.py

 ###############################################################################################################
#                                                                                                               #
#                           Cryptopals Crypto Challenges - Solutions of Problems                                #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       17.03.2019                                                                                      #
#   Copyright:  Copyright (C) 2019, Marcel Krause                                                               #
#   License:    GNU General Public License (GNU GPL-3.0-or-later)                                               #
#                                                                                                               #
#               This program is released under GNU General Public License (GNU GPL-3.0-or-later).               #
#               This program is free software: you can redistribute it and/or modify it under the terms of the  #
#               GNU General Public License as published by the Free Software Foundation, either version 3 of    #
#               the License, or any later version.                                                              #
#                                                                                                               #
#               This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;       #
#               without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.       #
#               See the GNU General Public License for more details.                                            #
#                                                                                                               #
#               You have received a copy LICENSE.md of the GNU General Public License along with this program.  #
#                                                                                                               #
 ###############################################################################################################

# import sys
# import os
# from shutil import copyfile, rmtree
# import subprocess
from binascii import a2b_hex

# Returns the score for a single character, given as decimal ASCII code
def getLetterScore(letterCode):
    # Letter frequency values for English letters (from a to z, second to last character is space, last character is everything else) from http://www.data-compression.com/english.html
    frequencyScore = [0.0651738, 0.0124248, 0.0217339, 0.0349835, 0.1041442, 0.0197881, 0.0158610, 0.0492888, 0.0558094, 0.0009033, 0.0050529, 0.0331490, 0.0202124, 0.0564513, 0.0596302, 0.0137645, 0.0008606, 0.0497563, 0.0515760, 0.0729357, 0.0225134, 0.0082903, 0.0171272, 0.0013692, 0.0145984, 0.0007836, 0.1918182, 0.0]

    # Get ASCII value of the character
    intval = letterCode - 97
    if (intval == -65):
        intval = len(frequencyScore) - 2
    else:
        if (intval >= -32) and (intval <= -7):
            intval += 32
        else:
            if (intval < 0) or (intval > 25):
                intval = len(frequencyScore) - 1

    # Return the character score
    return(frequencyScore[intval])

# Iterate over all ASCII chars, XOR them with an encoded string and find the ASCII char which gives the best score for English language (i.e. which contains letters with the highest frequencies for English)
def searchXORChar(encodedString):
    # These three variables save the results with the best score
    maxScore = 0.0
    maxEncrypted = ''
    maxKey = ''

    # Convert the input to int (for XORing)
    importToInt = int(encodedString, 16)

    # Try XORing all 256 ASCII chars with the input
    for i in range(0,256):
        # Fill up the ASCII char to the length of the input
        xorChar = '{:x}'.format(i)
        xorCharFin = ''
        for x in range(1, int(len(encodedString)/2)+1):
            if (len(xorChar) == 1):
                xorCharFin += ('0' + xorChar)
            else:
                xorCharFin += xorChar
        xorCharFinToInt = int(xorCharFin, 16)

        # XOR ASCII char and input
        xordImport = '{:02x}'.format(importToInt ^ xorCharFinToInt)

        # Score every single char of the XORed input
        xordImportRed = xordImport
        tempScore = 0.0
        tempEncrypted = ''
        for x in range(0, int(len(xordImport)/2)):
            currentChar = xordImportRed[:2]
            xordImportRed = xordImportRed[2:]
            tempScore += getLetterScore(int(currentChar, 16))
            tempEncrypted += chr(int(currentChar, 16))

        # If the previous top score is beaten, save the new values
        if (tempScore > maxScore):
            maxScore = tempScore
            maxEncrypted = tempEncrypted
            maxKey = chr(i)

    return(maxScore, maxKey, maxEncrypted)

# Read the file with all 60 strings
fname = "Challenge04_input.txt"
with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

# Variables for saving the total best score of all 60 strings
totalMaxScore = 0.0
totalMaxKey = 0
totalMaxEncrypted = ''
originalString = ''
originalStringLine = 0

# Find the best score for all 60 strings and get the best result
for i in range(0, len(content)):
    maxScore, maxKey, maxEncrypted = searchXORChar(content[i])

    if (maxScore > totalMaxScore):
        totalMaxScore = maxScore
        totalMaxKey = maxKey
        totalMaxEncrypted = maxEncrypted
        originalString = content[i]
        originalStringLine = i + 1

# Print out the result
print("Maximum score: " + str(totalMaxScore))
print("Original string: " + originalString)
print("Original string position: line " + str(originalStringLine))
print("Key: " + totalMaxKey)
print("Message: " + totalMaxEncrypted)
