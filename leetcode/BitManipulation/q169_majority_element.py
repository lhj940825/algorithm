'''
 * User: Hojun Lim
 * Date: 2021-02-02
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        from collections import defaultdict
        num2freq = defaultdict(int)

        num_elements = len(nums)
        for num in nums:
            num2freq[num] += 1

        for key, val in num2freq.items():
            if val > (num_elements//2):
                return key



