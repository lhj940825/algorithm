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
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        val_list = []
        if root:
            dfs(root, val_list)
            val_list = filter(lambda x: x>= low and x <= high, val_list)
            return sum(val_list)

        else:
            return 0



def dfs(cur_node, val_list):

    val_list.append(cur_node.val)

    if not cur_node.left and not cur_node.right:
        return

    if cur_node.left:
        dfs(cur_node.left, val_list)

    if cur_node.right:
        dfs(cur_node.right, val_list)

    return