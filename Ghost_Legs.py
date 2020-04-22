'''
 * User: Hojun Lim
 * Date: 2020-04-22
'''

import sys
import math


w, h = [int(i) for i in input().split()]

top_labels = input().split('  ') #labels are distinguished by double space
top_labels_map = [] # top_labels_map[i] denotes the bottom_label of corresponding i-th top_label


diagram = [input() for i in range(1, h-1)]
connector_idxs_per_line = []

# find all occurences of connector
for line in diagram:
    connector_idxs = [index//3 for index in range(len(line)) if line.startswith('--', index)]
    connector_idxs_per_line.append(connector_idxs)

for i in range(len(top_labels)):
    bottom_label = i # variable to trace the bottom label corresponding to the top label following the connectors

    for connector_idxs in connector_idxs_per_line:
        #print(connector_idxs, i, bottom_label)
        if bottom_label in connector_idxs:
            bottom_label += 1
            continue

        if bottom_label -1 in connector_idxs:
            bottom_label -= 1
            continue

    top_labels_map.append(bottom_label)

bottom_labels = input().split('  ') #labels are distinguished by double space

# print the result
for i in range(len(top_labels)):
    print(top_labels[i]+bottom_labels[top_labels_map[i]])




