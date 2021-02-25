'''
 * Project : algorithm
 * Package : 
 * User    : jun
 * Date    : 2021/02/25
 * Time    : 12:30 오후
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def in_order_traverse(node):

            if node:
                return in_order_traverse(node.left) + [node.val] + in_order_traverse(node.right)
            else:
                return []

        sorted_items_in_bst = in_order_traverse(root)
        gst_items = [sum(sorted_items_in_bst[i:]) for i in range(0, len(sorted_items_in_bst))]

        def update_bst_to_gst(node, gst_items, k):
            if not node.left and not node.right: # when cur_node is the leaf
                node.val = gst_items[k]
                k += 1
                return k

            if node:
                if node.left: k = update_bst_to_gst(node.left, gst_items, k)

                node.val = gst_items[k]
                k += 1

                if node.right: k = update_bst_to_gst(node.right, gst_items, k)


            return k

        update_bst_to_gst(root, gst_items, 0)
        return root

