#!/usr/bin/env python
#Filename: Challenge02.py

 ###############################################################################################################
#                                                                                                               #
#                           Cryptopals Crypto Challenges - Solutions of Problems                                #
#                                                                                                               #
#   Author:     Marcel Krause                                                                                   #
#   Date:       17.02.2019                                                                                      #
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

from binascii import a2b_hex, b2a_base64
importString1 = '1c0111001f010100061a024b53535009181c'
importString2 = '686974207468652062756c6c277320657965'

convString1 = int(importString1, 16)
convString2 = int(importString2, 16)

output = '{:x}'.format(convString1 ^ convString2)
output2 = a2b_hex('{:02x}'.format(convString1 ^ convString2))

print(output)
print(output2)
