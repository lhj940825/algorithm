'''
 * User: Hojun Lim
 * Date: 2021-01-19
'''

class Solution:
    # solution using the counting sorting
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort() #quick sort: nlog(n)

        dic = {num:0 for num in range(arr1[-1] +1) }
        for num in arr1:
            dic[num] += 1

        output = []
        for num in arr2:
            output += [num]*dic[num]
            del dic[num]

        for key, val in dic.items():
            output += [key]*val

        return output
