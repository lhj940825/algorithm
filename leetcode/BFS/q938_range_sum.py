'''
 * User: Hojun Lim
 * Date: 2021-01-12
'''

# q938 Range Sum of BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        from collections import deque

        que = deque()
        que.append(root)

        val_list = []

        # search by BFS
        while que:
            cur_node = que.popleft()
            cur_val = cur_node.val
            if cur_val <= high and cur_val >= low:
                val_list.append(cur_val)

            if cur_node.left:
                que.append(cur_node.left)

            if cur_node.right:
                que.append(cur_node.right)

        return sum(val_list)