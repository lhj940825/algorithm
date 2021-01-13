'''
 * User: Hojun Lim
 * Date: 2021-01-13
'''

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter

        jewels = Counter(jewels)
        stones = Counter(stones)

        cnt = 0
        for jewel in jewels:
            if jewel in stones:
                cnt += stones[jewel]

        return cnt