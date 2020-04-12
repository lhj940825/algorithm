'''
 * User: Hojun Lim
 * Date: 2020-04-12
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())


highest_price = max_loss = 0

prices=input().split()
for p in prices:
    p = int(p)
    if p > highest_price:
        highest_price = p

    if p-highest_price < max_loss:
        max_loss = p -highest_price

print(max_loss)

"""
# the solution below causes the time out failure
n = int(input())

previous_value = 0
max_loss = 0
loss = 0
current_value = []
for i in input().split():
    current_value.append(int(i))

for i in range(0,len(current_value)-1):
    for j in range(i+1, len(current_value)):
        diff =current_value[j] - current_value[i]
        if  diff < max_loss:
            max_loss = diff


print(max_loss)
"""


"""
n = int(input())

previous_value = 0
max_loss = 0
loss = 0
for i in input().split():
    current_value = int(i)

    value_difference = current_value - previous_value
    if value_difference < 0:
        loss += value_difference

    elif value_difference >0:
        if loss < max_loss:
            max_loss = loss
            loss = 0

    previous_value = current_value

print(max_loss)

"""