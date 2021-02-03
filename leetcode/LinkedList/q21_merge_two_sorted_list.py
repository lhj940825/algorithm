'''
 * User: Hojun Lim
 * Date: 2021-02-03
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        point_l1 = l1
        point_l2 = l2

        root = ListNode(None, None)
        head = root

        while point_l1 and point_l2:
            if point_l1.val <= point_l2.val:
                head.next = point_l1
                head = head.next
                point_l1 = point_l1.next


            else:
                head.next = point_l2
                head = head.next
                point_l2 = point_l2.next

        head.next = point_l1 if point_l2 == None else point_l2
        return root.next






