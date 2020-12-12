'''
 * User: Hojun Lim
 * Date: 2020-12-12
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.dfs(nums, 0, len(nums)-1)

    def dfs(self, nums: List[int], start_point, end_point):

        if (start_point > end_point) or (end_point < start_point):
            return None
        if start_point == end_point:
            return TreeNode(nums[start_point], left=None, right=None)

        cur_item_point = round((end_point+start_point)/2)
        cur_node_val = nums[cur_item_point]

        cur_node = TreeNode(cur_node_val, left=self.dfs(nums, start_point, cur_item_point -1), right=self.dfs(nums, cur_item_point+1, end_point))
        return cur_node

