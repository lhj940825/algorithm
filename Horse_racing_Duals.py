'''
 * User: Hojun Lim
 * Date: 2020-04-20
'''
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
list_pi = []
for i in range(n):
    pi = int(input())
    list_pi.append(pi)

list_pi.sort() #sort the given list of strenghts of horses

smallest_D = sys.maxsize # the strength difference
prev_p = 0 # previous strength in list_pi

for pi in list_pi:
    D = pi - prev_p
    if D < smallest_D: # update the smallest_D
        smallest_D = D

    prev_p = pi


print(smallest_D)