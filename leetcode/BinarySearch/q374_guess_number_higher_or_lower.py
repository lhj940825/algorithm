'''
 * User: Hojun Lim
 * Date: 2021-01-26
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return binary_search(1, n)


def binary_search(start, end):
    if start > end:
        return None

    mid = (start+end)//2
    hint = guess(mid)

    target = 0
    if hint == -1:
        target = binary_search(start, mid-1)
    elif hint == 1:
        target = binary_search(mid+1, end)
    else:
        target = mid

    return target



