'''
 * User: Hojun Lim
 * Date: 2021-01-04
'''

class Solution:
    def divisorGame(self, N: int) -> bool:

        if N % 2 == 0:
            return True
        return False

# Bottom-Up DP approach
    def divisorGame(self, N: int) -> bool:

        dp = [False] * (N + 1)
        for n in range(2, N+1):
            for x in range(1, n):
                if (n % x == 0) and (not dp[n-x]):
                    dp[n] = True
                    break
        return dp[N]