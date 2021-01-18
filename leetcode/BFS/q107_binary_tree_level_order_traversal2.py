'''
 * User: Hojun Lim
 * Date: 2021-01-18
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        val_list = []
        if root:
            val_list = bfs(root, val_list)

        return val_list

def bfs(root, val_list):
    from collections import deque

    que = deque()
    que.append(root)

    while que:
        cur_level_val_list = []
        for i in range(len(que)):
            cur_node = que.popleft()
            cur_level_val_list.append(cur_node.val)

            if cur_node.left:
                que.append(cur_node.left)
            if cur_node.right:
                que.append(cur_node.right)

        val_list.insert(0, cur_level_val_list)

    return val_list

