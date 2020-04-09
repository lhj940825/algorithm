'''
 * User: Hojun Lim
 * Date: 2020-04-09
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
t_min = 5527

try:
    input_list = input().split()
    len_input_list = len(input_list)

    if len_input_list != 0:
        for i in input_list:
            # t: a temperature expressed as an integer ranging from -273 to 5526
            t = int(i)
            if abs(t) < abs(t_min):
                t_min = t

            elif abs(t) == abs(t_min):
                if t>0:
                    t_min =t

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)
        print(t_min)

    else:
        print('0')


except :

    pass


