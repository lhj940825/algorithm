'''
 * User: Hojun Lim
 * Date: 2020-04-17
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


hashmap = {}

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()

    # add each key value to hash map, duplicate check
    if ext not in hashmap:
        hashmap[ext.lower()] = mt #save ext value as its lower case, in order to make the hashmap case insensitive


#print(hashmap)
for i in range(q):
    fname = input()  # One file name per line.
    MiME_type = "UNKNOWN"

    if '.' not in fname:
        pass
    else:
        unpacked_fname = fname.split('.')
        ext = unpacked_fname[len(unpacked_fname)-1] # get the element next to the last occurence of the dot.

        ext = ext.lower() # make ext as lower case
        if ext in hashmap:
            MiME_type = hashmap[ext]


    print(MiME_type)



