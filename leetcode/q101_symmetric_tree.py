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
    def isSymmetric(self, root: TreeNode) -> bool:

        from collections import deque
        import math
        que = deque()

        if root == None:
            return True

        if type(root.left) != type(root.right):
            return False

        if root.left == None and root.right == None:
            return True

        left_val_list, right_val_list = [], []


        def bfs(root:TreeNode, val_list, search_left_first):
            que.append(root)

            while len(que) != 0:

                cur_node = que.popleft()
                if cur_node.val == None:
                    val_list.append('null')
                    continue
                val_list.append(cur_node.val)

                if search_left_first:
                    if cur_node.left != None:
                        que.append(cur_node.left)
                    else:
                        que.append(TreeNode(None, None, None))

                    if cur_node.right != None:
                        que.append(cur_node.right)
                    else:
                        que.append(TreeNode(None, None, None))

                else:
                    if cur_node.right != None:
                        que.append(cur_node.right)
                    else:
                        que.append(TreeNode(None, None, None))
                    if cur_node.left != None:
                        que.append(cur_node.left)
                    else:
                        que.append(TreeNode(None, None, None))



        bfs(root.left, left_val_list, True)
        bfs(root.right, right_val_list, False)
        print(left_val_list, right_val_list)
        if left_val_list == right_val_list:
            return True
        else:
            return False


