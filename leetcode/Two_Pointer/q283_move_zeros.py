'''
 * User: Hojun Lim
 * Date: 2021-02-04
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        none_zero_point = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[none_zero_point] = nums[none_zero_point], nums[i]
                none_zero_point += 1




        