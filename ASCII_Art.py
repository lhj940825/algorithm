'''
 * User: Hojun Lim
 * Date: 2020-04-13
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def get_idx_4_letters(text):
    idxs = []
    for letter in text:
        ascii_code = ord(letter)
        if ascii_code >= 97 and ascii_code <=122: #lower case
            idxs.append(ascii_code - 65 -32)

        elif ascii_code >=65 and ascii_code <= 90: #upper case
            idxs.append(ascii_code - 65) # ascii code for 'A' is 65

        else: #letter neither lower nor upper case
            idxs.append(26)

    return idxs


def get_Ascii_art_row(idxs, l, rows):

    # l = length
    if len(idxs) ==1: # if there is only one letter

        ascii_art_rows =rows[:, l*idxs[0]:(l+1)*idxs[0]]
    else:
        #print(idxs)
        ascii_art_rows = np.concatenate([rows[:,l*idx:l*(idx+1)] for idx in idxs], axis=1)


    return ascii_art_rows



l = int(input())
h = int(input())
text = input()


rows = []
for i in range(h):
    temp = []
    row = input()

    for letter in row:
        temp.append(letter)
    rows.append(temp)


import numpy as np
rows = np.asarray(rows)
idxs = get_idx_4_letters(text)
ascii_art_rows = get_Ascii_art_row(idxs, l, rows)

for row in ascii_art_rows.tolist():
    print("".join(row))