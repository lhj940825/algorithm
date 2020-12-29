'''
 * User: Hojun Lim
 * Date: 2020-12-29
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root:
            return bfs(root)
        return []

def bfs(node):
    from collections import deque
    que = deque()
    traversal_result = []

    que.append(node)
    while len(que) != 0:
        cur_level_traversal_result = []

        for i in range(len(que)):
            cur_node = que.popleft()
            cur_level_traversal_result.append(cur_node.val)

            if cur_node.left:
                que.append(cur_node.left)
            if cur_node.right:
                que.append(cur_node.right)

        traversal_result.append(cur_level_traversal_result)

    return traversal_result
