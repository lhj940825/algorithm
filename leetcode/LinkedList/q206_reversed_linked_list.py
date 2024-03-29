'''
 * User: Hojun Lim
 * Date: 2021-02-02
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

