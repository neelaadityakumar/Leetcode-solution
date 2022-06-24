# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next

        prev = None
        curr = head
        for _ in range(k):
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        head.next = self.reverseKGroup(curr, k)
        return prev