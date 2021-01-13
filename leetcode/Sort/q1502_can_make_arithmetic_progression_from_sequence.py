'''
 * User: Hojun Lim
 * Date: 2021-01-13
'''

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        #arr.sort()
        arr = quick_sort(arr)
        print(arr)
        gap = arr[1] - arr[0]
        for i in range(1 , len(arr)-1):
            if gap == (arr[i+1] - arr[i]):
                continue

            else:
                return False

        return True

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    pivot_left = [item for item in tail if item <= pivot]
    pivot_right = [item for item in tail if item > pivot]

    return quick_sort(pivot_left) + [pivot] + quick_sort(pivot_right)
