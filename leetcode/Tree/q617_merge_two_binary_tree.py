'''
 * User: Hojun Lim
 * Date: 2021-01-27
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        merged_root = dfs(t1, t2)
        return merged_root


def dfs(node1, node2):
    if node1 == None and node2 == None:
        return None

    if node1 == None:
        return node2
    elif node2 == None:
        return node1

    merged_node = TreeNode(val=node1.val + node2.val, left=dfs(node1.left, node2.left), right=dfs(node1.right, node2.right))
    return merged_node









