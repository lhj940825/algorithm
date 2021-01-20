'''
 * User: Hojun Lim
 * Date: 2021-01-20
'''
###########################################################################
# naive sorting approach
###########################################################################
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [num**2 for num in nums]
        nums.sort()
        return nums
###########################################################################
# Two pointer solution
###########################################################################

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        idx_start_pos_num = -1 # index of the first positive number in the array:nums
        for idx, num in enumerate(nums):
            if num >= 0:
                idx_start_pos_num = idx
                break

        output = []
        # when all numbers are negative
        if idx_start_pos_num == -1:
            output = [num**2 for num in nums]
            output = output[::-1]

        # else
        else:
            left_pointer = idx_start_pos_num - 1
            right_pointer = idx_start_pos_num

            while left_pointer >= 0 and right_pointer < len(nums):
                num_left = abs(nums[left_pointer])
                num_right = nums[right_pointer]

                if num_right <= num_left:
                    output += [num_right**2]
                    right_pointer += 1
                    continue

                elif num_right > num_left:
                    output += [num_left**2]
                    left_pointer -= 1
                    continue

            if left_pointer >= 0:
                temp_output = [num**2 for num in nums[:left_pointer + 1]]
                output += temp_output[::-1]
            else:
                temp_output = [num**2 for num in nums[right_pointer:]]
                output += temp_output

        return output






