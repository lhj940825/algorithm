'''
 * User: Hojun Lim
 * Date: 2021-01-01
'''
class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1: # when only 1 step in staircase
            return 1

        num_ways_by_step = [0]*n

        num_ways_by_step[0] = 1
        num_ways_by_step[1] = 2

        for i in range(2, n): # all possible distinctive ways for i-th stair is just the sum of num_ways from two previous steps.
            num_ways_by_step[i] = num_ways_by_step[i-1]+ num_ways_by_step[i-2]

        return num_ways_by_step[-1]




