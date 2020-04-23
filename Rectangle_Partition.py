import sys
import math

def cal_all_intervals (measurements):

    all_intervals = []

    for i in range(len(measurements)-1):
        for j in range(i+1, len(measurements)):
            all_intervals.append(measurements[j] - measurements[i])


    return all_intervals




# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h, count_x, count_y = [int(i) for i in input().split()]

w_measurements = [int(i) for i in input().split()] # store the list of measurements on the width side
w_measurements.insert(0, 0)
w_measurements.append(w)

h_measurements = [int(i) for i in input().split()] # store the list of measurements on the height side
h_measurements.insert(0, 0)
h_measurements.append(h)


w_intervals = cal_all_intervals(w_measurements)
h_intervals = cal_all_intervals(h_measurements)

#print(w_intervals)

square_cnt = 0
for width in w_intervals:
    for height in h_intervals:
        if width == height:
            square_cnt+=1

print(square_cnt)


