'''
 * User: Hojun Lim
 * Date: 2021-03-05
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        cur_node = head.next
        cycle_check_pnt = head

        step = 0
        while cur_node:
            if cur_node == cycle_check_pnt:
                return True

            if step % 2 == 1:
                cycle_check_pnt = cycle_check_pnt.next

            cur_node = cur_node.next
            step += 1


        return False

