'''
 * User: Hojun Lim
 * Date: 2020-11-06
'''

import numpy as np

def stack_check(stack:list, count):
    """
    if two consecutive items are identical, remove them
    """
    if len(stack) >= 2: # don't perform duplicate check if num_item in stack is below 2
        if stack[-1] == stack[-2]:
            stack = stack[:-2]
            count += 2
    return stack, count

def solution(board, moves):
    stack = []
    count = 0 # number of vanished dolls

    board = np.asarray(board, dtype=np.int)
    for move in moves:
        move -= 1
        for i in range(np.shape(board)[0]):

            if board[i][move] == 0:
                pass

            else:
                item = board[i][move]
                stack.append(item)
                stack, count = stack_check(stack, count)
                board[i][move] = 0
                break

    return count
