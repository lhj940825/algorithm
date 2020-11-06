'''
 * User: Hojun Lim
 * Date: 2020-11-06
'''

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])

    answer.sort()
    answer = list(dict.fromkeys(answer)) # remove duplicate items by building dictionary out of the answer list

    return answer
