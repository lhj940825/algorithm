'''
 * User: Hojun Lim
 * Date: 2020-12-21
'''
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.bin_search(arr, 0, len(arr)-1)

    def bin_search(self, arr, start, end):

        idx_mid = (start+end)//2
        print(start, end, idx_mid)
        mid = arr[idx_mid]
        right = arr[idx_mid+1]
        left = arr[idx_mid-1]

        if mid > left and mid < right:
            return self.bin_search(arr, idx_mid+1, end)

        if mid < left and mid >right:
            return self.bin_search(arr, start, idx_mid-1)

        if mid > left and mid >right:
            return idx_mid

        