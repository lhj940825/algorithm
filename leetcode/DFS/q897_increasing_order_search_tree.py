'''
 * User: Hojun Lim
 * Date: 2021-01-15
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        root_incBST = TreeNode(0, None, None)
        leaf_incBST = dfs(root, root_incBST)
        leaf_incBST.right = None

        return root_incBST.right

def dfs(node, tail_incBST):
    if not node.left and not node.right:
        tail_incBST.right = TreeNode(node.val, None, TreeNode(None, None, None))
        return tail_incBST.right

    if node.left:
        tail_incBST = dfs(node.left, tail_incBST)

    tail_incBST.right = TreeNode(node.val, None, TreeNode(None, None, None))
    tail_incBST = tail_incBST.right

    if node.right:
        tail_incBST = dfs(node.right, tail_incBST)

    return tail_incBST


