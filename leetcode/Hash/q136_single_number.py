'''
 * User: Hojun Lim
 * Date: 2021-02-01
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        int2cnt = {}
        for num in nums:
            if num in int2cnt:
                int2cnt[num] += 1
            else:
                int2cnt[num] = 1

        for key, val in int2cnt.items():
            if val == 1:
                return key

