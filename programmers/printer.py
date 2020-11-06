'''
 * User: Hojun Lim
 * Date: 2020-11-06
'''

from collections import deque

def solution(priorities, location):
    my_doc_flag = [False]*len(priorities)
    my_doc_flag[location] = True
    waiting_list = deque([(priority, flag) for priority, flag in zip(priorities, my_doc_flag)])

    round = 0

    while True:

        priority, my_doc = waiting_list.popleft()

        print_flag = True

        for _priority, _mydoc in waiting_list:
            if priority < _priority:
                print_flag = False
                break

        if print_flag:
            round += 1
            if my_doc:
                return round

        else:
            waiting_list.append((priority, my_doc))