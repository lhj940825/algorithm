'''
 * User: Hojun Lim
 * Date: 2021-02-22
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def dfs(node):
            if not node.left and not node.right:
                return [node.val], [], 0

            child = []
            g_child = []
            left_sum_child, right_sum_child = 0, 0
            if node.left:
                left_child, left_g_child, left_sum_child = dfs(node.left)
                child.extend(left_child)
                g_child.extend(left_g_child)
            if node.right:
                right_child, right_g_child, right_sum_child = dfs(node.right)
                child.extend(right_child)
                g_child.extend(right_g_child)

            sum_g_child = left_sum_child + right_sum_child
            if node.val % 2 == 0:
                sum_g_child += sum(g_child)

            g_child = child
            child = [node.val]
            return child, g_child, sum_g_child

        _, _, sum_g_child = dfs(root)
        return sum_g_child