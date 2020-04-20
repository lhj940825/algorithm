'''
 * User: Hojun Lim
 * Date: 2020-04-20
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



n = int(input())
cells = [tuple(input().split()) for i in range(n)]
computed_cell = ['None' for i in range(n)] # in order to prevent the repeatedly carculating the same cells in recursive function, we save the computed cell value in this list


def get_arg_value(arg, idx):
    global cells

    if arg == '_':
        return 'None'

    elif '$' == arg[0]: # reference call

        ref = int(arg[1:])
        if computed_cell[ref] == 'None': # if computed_cell[ref] has not been computed
            computed_cell[ref]  = compute(cells[ref]) # update the computed_cell list

        return computed_cell[ref]

    else: # no reference
        return int(arg)


def compute(cell):
    # cell[0] = operation, cell[1] = arg_1, cell[2] = arg_2

    arg_1 = get_arg_value(cell[1], 1)

    if cell[0] == 'VALUE':

        return arg_1
    else:

        arg_2 = get_arg_value(cell[2], 2)

        if cell[0] == 'ADD':

            return arg_1 + arg_2

        elif cell[0] == 'SUB':

            return arg_1 - arg_2

        elif cell[0] == 'MULT':
            return arg_1 * arg_2





for cell in cells:
    print(compute(cell))