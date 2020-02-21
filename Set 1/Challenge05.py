#!/usr/bin/env python
#Filename: Challenge05.py

 ###############################################################################################################
#                                                                                                               #
#                           Cryptopals Crypto Challenges - Solutions of Problems                                #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       19.03.2019                                                                                      #
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

# Set the key
key = 'ICE'

# Import the plaintext
fname = "Challenge05_input.txt"
with open(fname, 'r') as inFile:
    importString=inFile.read()

# Convert the key and import string to a list and get their lengths
keyList = list(key)
keyLength = len(keyList)
importList = list(importString)
importLength = len(importList)

# Iterate over the imported input
output = ''
for i in range(0, importLength):
    currentKey = keyList[i%keyLength]
    currentPlain = importList[i]

    # XOR against the current key and store the output
    output += hex(ord(currentKey) ^ ord(currentPlain))[2:].zfill(2)

# Print out the result
print(output.replace("x0", ""))
