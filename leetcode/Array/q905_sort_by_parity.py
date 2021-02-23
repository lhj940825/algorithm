'''
 * Project : algorithm
 * Package : 
 * User    : jun
 * Date    : 2021/02/23
 * Time    : 2:26 오후
'''

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        output = []
        even_idx, odd_idx = 0, 1

        for num in A:
            if num % 2 == 0:
                output.insert(even_idx, num)
                even_idx += 1

            else:
                output.insert(odd_idx, num)
            odd_idx += 1

        return output