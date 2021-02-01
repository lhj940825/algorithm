'''
 * User: Hojun Lim
 * Date: 2021-02-01
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        from collections import deque
        que = deque()

        if not root:
            return

        que.append(root)


        while que:
            num_nodes_in_cur_depth = len(que)
            for _ in range(num_nodes_in_cur_depth):
                cur_node = que.popleft()
                cur_node.left, cur_node.right = cur_node.right, cur_node.left

                if cur_node.left:
                    que.append(cur_node.left)
                if cur_node.right:
                    que.append(cur_node.right)

        return root