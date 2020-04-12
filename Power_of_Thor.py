'''
 * User: Hojun Lim
 * Date: 2020-04-12
'''
import sys
import math
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

dir_dic = {'0,-1': "N",'1,-1': "NE",'1,0': "E",'1,1': "SE",'0,1': "S",'-1,1': "SW", '-1,0': "W",'-1,-1': "NW"}

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    dir_x = np.sign(light_x - initial_tx)
    dir_y = np.sign(light_y - initial_ty)

    #print(light_y - initial_ty, file=sys.stderr)

    print(dir_dic[str(dir_x)+','+str(dir_y)])

    initial_tx +=dir_x
    initial_ty +=dir_y

    # A single line providing the move to be made: N NE E SE S SW W or NW
    #print("SE")