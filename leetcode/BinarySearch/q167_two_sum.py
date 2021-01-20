'''
 * User: Hojun Lim
 * Date: 2021-01-20
'''
###########################################################################
# Binary Search Solution
###########################################################################
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_numbers = len(numbers)
        for idx in range(num_numbers):
            idx2 = binarySearch(numbers, idx+1, num_numbers -1, numbers[idx], target)

            if idx2 != None:

                return [idx+1, idx2+1]



def binarySearch(numbers, start, end, num1, target):
    if start > end:
        return None

    mid = (start+end)//2
    num2 = numbers[mid]

    target_candidate = num1+num2
    num2_idx = None
    if target > target_candidate:
        num2_idx = binarySearch(numbers, mid+1, end, num1, target)

    elif target < target_candidate:
        num2_idx = binarySearch(numbers, start, mid-1, num1, target)

    else:
        return mid

    return num2_idx


###########################################################################
# Two pointer solution
###########################################################################
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers)-1

        while left_pointer < right_pointer:
            target_candidate = numbers[left_pointer] + numbers[right_pointer]
            if target_candidate < target:
                left_pointer += 1
                continue
            elif target_candidate > target:
                right_pointer -= 1
                continue

            else:
                break
        return [left_pointer +1, right_pointer +1]





