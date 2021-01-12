'''
 * User: Hojun Lim
 * Date: 2021-01-12
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# q110. Balanced Binary Tree
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.balance = True

        if not root: # if root node is None
            return True

        self.dfs(root, 0)

        return self.balance


    def dfs(self, node: TreeNode, cur_depth):
        cur_depth += 1
        if not node.left and not node.right:
            return cur_depth

        left_depth, right_depth = cur_depth, cur_depth

        if node.left:
            left_depth = self.dfs(node.left, cur_depth)

        if node.right:
            right_depth = self.dfs(node.right, cur_depth)

        if abs(left_depth - right_depth) > 1:
            self.balance = False

        return max(left_depth, right_depth)