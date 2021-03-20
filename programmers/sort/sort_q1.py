'''
 * User: Hojun Lim
 * Date: 2021-03-20
'''

def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        i -= 1
        j -= 1
        k -= 1
        temp_arr = array[i: j+1]
        temp_arr.sort()
        answer.append(temp_arr[k])

    return answer