'''
 * User: Hojun Lim
 * Date: 2020-12-09
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.max_depth = 1
        def dfs(node: TreeNode, depth):
            #global max_depth

            if node == None:
                return

            if depth > self.max_depth:
                self.max_depth = depth

            depth += 1
            if node.left != None:
                dfs(node.left, depth)

            if node.right != None:
                dfs(node.right, depth)


        if root == None:
            return 0
        dfs(root, 1)
        return self.max_depth