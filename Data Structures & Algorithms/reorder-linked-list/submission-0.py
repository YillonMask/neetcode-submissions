# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow , fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # now slow is at the mid point
        second = slow.next
        # cut the original list into two half
        slow.next = None
        # reverse the second half
        pre = None
        cur = second
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        # now pre is the head of reverse second half
        # merge the two half
        cur = head
        second = pre
        while second:
            temp1, temp2 = cur.next, second.next

            cur.next = second
            second.next = temp1

            cur = temp1
            second = temp2
