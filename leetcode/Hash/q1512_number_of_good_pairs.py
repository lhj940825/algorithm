'''
 * User: Hojun Lim
 * Date: 2021-01-10
'''

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num2idx = {}

        for idx, num in enumerate(nums):
            if num not in num2idx:
                num2idx[num] = [idx]
            else:
                num2idx[num].append(idx)

        def combination(n):
            return int(n*(n-1)/2)

        num_pairs = 0
        for value in num2idx.values():
            n = len(value)
            if n >= 2:
                num_pairs += combination(n)
            else:
                continue

        return num_pairs

