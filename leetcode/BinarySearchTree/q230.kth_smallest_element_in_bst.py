'''
 * User: Hojun Lim
 * Date: 2021-02-15
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return inorder_traverse(root, k, 0)[0]


def inorder_traverse(node, k, visit_cnt):

    if not node.left and not node.right:
        visit_cnt += 1
        if k == visit_cnt:
            return (node.val, k, visit_cnt)
        else:
            return (None, k, visit_cnt)

    if node.left:
        val, k, visit_cnt = inorder_traverse(node.left, k, visit_cnt)

    if visit_cnt != k: # not yet found
        visit_cnt += 1 # visit the cur node
        if visit_cnt == k:
            return (node.val, k, visit_cnt)

        else:
            if node.right:
                val, k, visit_cnt = inorder_traverse(node.right, k, visit_cnt)

    return (val, k, visit_cnt)



###################################################################################
## simpler solution
###################################################################################

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root:
            return inorder_traverse(root)[k-1]


def inorder_traverse(node):
    if node:
        return inorder_traverse(node.left) + [node.val] + inorder_traverse(node.right)
    else:
        return []

