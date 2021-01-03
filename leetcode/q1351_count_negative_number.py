'''
 * User: Hojun Lim
 * Date: 2021-01-03
'''

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        import numpy as np

        grid = np.asarray(grid)
        mask = (grid < 0).flatten()

        return sum(mask)
        """

        cnt = 0
        for _list in grid:
            for element in _list:
                if element < 0:
                    cnt += 1


        return cnt