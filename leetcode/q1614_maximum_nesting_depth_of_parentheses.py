'''
 * User: Hojun Lim
 * Date: 2020-12-31
'''
class Solution:
    def maxDepth(self, s: str) -> int:
        maxdepth = 0
        depth = 0
        for char in s:
            if char == '(':
                depth += 1
                if maxdepth < depth: maxdepth = depth

            if char == ')':
                depth -= 1

        return maxdepth
