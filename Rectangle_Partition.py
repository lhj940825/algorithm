'''
 * User: Hojun Lim
 * Date: 2020-04-23
'''
import sys
import math




def cal_all_intervals (measurements):

    all_intervals = []
    for width in range(1, len(measurements)+1) : # width ~ [1, len(w_intervals)]
        for start_idx in range(len(measurements)):
            if width+start_idx > len(measurements): # case when out of range
                continue
            else:
                all_intervals.append(sum(measurements[start_idx:start_idx+width]))# if it is in the range, compute the interval and append in the list

    #print(all_intervals)
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


# compute the intervals between measurements
w_intervals = [w_measurements[i+1] - w_measurements[i] for i in range(len(w_measurements)-1)]
h_intervals = [h_measurements[i+1] - h_measurements[i] for i in range(len(h_measurements)-1)]

w_intervals = cal_all_intervals(w_intervals)
h_intervals = cal_all_intervals(h_intervals)

square_cnt = 0
for w_interval in w_intervals:
    for h_interval in h_intervals:
        if w_interval == h_interval:
            square_cnt+=1

print(square_cnt)


