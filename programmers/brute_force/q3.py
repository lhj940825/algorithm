'''
 * Project : algorithm
 * Package : 
 * User    : jun
 * Date    : 2021/03/29
 * Time    : 11:37 오후
'''

####################################################################
# Solution 1
####################################################################
def solution(brown, yellow):
    answer = []
    i, max_i = 2,  yellow // 2
    all_comb_yellow = [(yellow, 1)]

    # collect all possible combination of integers such that one times the other equal to yellow
    while i < max_i:
        if yellow % i == 0:
            if yellow // i >= i: all_comb_yellow.append((yellow // i, i))
            else: break
        i += 1

    for comb_yellow in all_comb_yellow:
        row_yellow, col_yellow = comb_yellow
        if (row_yellow+2)*2 + col_yellow*2 == brown:
            answer.extend([row_yellow+2, col_yellow+2])

    return answer

####################################################################
# Solution 2
####################################################################
def solution(brown, yellow):
    answer = []
    y_width = 0
    is_found = False

    while not is_found:
        y_width += 1

        for y_height in range(1, y_width+1):

            if (y_height)*2 + (y_width+2)*2 == brown and y_height*y_width == yellow:
                answer.extend([y_width + 2, y_height + 2])
                is_found = True
                break

    return answer