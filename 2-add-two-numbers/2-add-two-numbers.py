# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            sum=0
            if l1:
                sum+= l1.val
                l1 = l1.next
            if l2:
                sum+=l2.val
                l2 = l2.next
            carry, val = divmod(sum+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
