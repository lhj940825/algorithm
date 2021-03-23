'''
 * User: Hojun Lim
 * Date: 2021-03-23
'''

def solution(numbers):

    numbers = [str(number) for number in numbers]
    numbers.sort(key= lambda x: x*3, reverse=True)

    answer = str(int(''.join(numbers)))
    return answer