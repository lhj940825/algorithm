'''
 * User: Hojun Lim
 * Date: 2021-02-11
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        from collections import deque
        que = deque()

        if not root:
            return

        que.append(root)
        output = []

        while que:
            num_nodes_in_cur_level = len(que)

            for i in range(num_nodes_in_cur_level):
                cur_node = que.popleft()
                if cur_node.left: que.append(cur_node.left)
                if cur_node.right: que.append(cur_node.right)


            output.append(cur_node.val)

        return output


