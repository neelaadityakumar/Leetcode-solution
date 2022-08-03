# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # ensure the first part has the same or one more node
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        tpart=prev
        # combine head part and node part
        fpart = head
        while tpart:
            tmp = tpart.next
            tpart.next = fpart.next
            fpart.next = tpart
            fpart= fpart.next.next #p = node.next
            tpart = tmp