'''
 * User: Hojun Lim
 * Date: 2021-01-24
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        diction = dict();
        sortedNums = sorted(nums)
        for i in range(len(nums)):
            if sortedNums[i] not in diction:
                diction[sortedNums[i]] = i

        for i in range(len(nums)):
            nums[i] = diction[nums[i]]
        return nums
    # Time Complexity: O(nlog(n))
    # Space Complexity: O(n)
