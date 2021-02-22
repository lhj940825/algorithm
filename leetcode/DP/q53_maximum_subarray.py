'''
 * User: Hojun Lim
 * Date: 2021-02-22
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cum_max = [0]*len(nums)
        cum_max[0] = nums[0]


        for idx, num in enumerate(nums[1:], start=1):
            if num > cum_max[idx-1] + num:
                cum_max[idx] = num
            else:
                cum_max[idx] = cum_max[idx-1] + num


        return max(cum_max)


