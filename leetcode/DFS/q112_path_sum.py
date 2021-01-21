'''
 * User: Hojun Lim
 * Date: 2021-01-21
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.is_found = False

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root:
            self.dfs_sum(root, 0, targetSum)
        return self.is_found


    def dfs_sum(self, node, cum_sum, target_sum):

        cum_sum += node.val

        if not node.left and not node.right:
            if cum_sum == target_sum:
                self.is_found = True
            return

        if node.left:
            self.dfs_sum(node.left, cum_sum, target_sum)

        if node.right:
            self.dfs_sum(node.right, cum_sum, target_sum)