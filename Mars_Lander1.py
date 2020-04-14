'''
 * User: Hojun Lim
 * Date: 2020-04-15
'''
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
prev_y = -1 # variable to store the value of land_y in previous step
prev_x = -1 # variable to store the value of land_x in previous step
flat_x = [] # save the range of x_coordinates where the flat_ground lies


## below for loop and the variables in it are not necessary in this task(Mars_Lander1) as it is simplified task.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

    if land_y == prev_y:
        flat_x.append(prev_x)
        flat_x.append(land_x)


    else:
        prev_y = land_y
        prev_x = land_x

    #print(land_x, land_y, file=sys.stderr)
#print(flat_x, file=sys.stderr)

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    if v_speed >= -30:
        print("0 3")
    else:
        print("0 4")