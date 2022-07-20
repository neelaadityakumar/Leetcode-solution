"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        
        dummy = Node(0)
        prev, stack = dummy, [head]
        while stack:
            curr = stack.pop() 
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
            prev.next = curr
            curr.prev = prev  
            curr.child = None
            prev = curr
        
        res = dummy.next
        res.prev = None
        return res