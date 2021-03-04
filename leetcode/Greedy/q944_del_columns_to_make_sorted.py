'''
 * Project : algorithm
 * Package : 
 * User    : jun
 * Date    : 2021/03/04
 * Time    : 12:09 오후
'''

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num_col = len(strs[0])
        num_del = 0
        for col_idx in range(num_col):
            for str_idx in range(0, len(strs)-1):
                if strs[str_idx][col_idx] <= strs[str_idx+1][col_idx]:
                    continue
                else:
                    num_del += 1
                    break

        return num_del
