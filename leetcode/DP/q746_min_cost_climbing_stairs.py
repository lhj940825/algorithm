'''
 * User: Hojun Lim
 * Date: 2021-01-01
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cum_cost = [0]*len(cost)
        cum_cost[0] = cost[0]
        cum_cost[1] = cost[1]

        for i in range(0, len(cost)):
            cum_cost[i] = min(cum_cost[i-1], cum_cost[i-2]) + cost[i]


        return min(cum_cost[-1], cum_cost[-2])

