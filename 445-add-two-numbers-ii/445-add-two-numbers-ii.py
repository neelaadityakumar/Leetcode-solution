# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry, curr,next = 0, None,None
        while stack1 or stack2 or carry:
            d1 = stack1.pop() if stack1 else 0
            d2 = stack2.pop() if stack2 else 0
            carry, val = divmod(d1+d2+carry, 10)
            curr = ListNode(val, next)
            next=curr
        return curr