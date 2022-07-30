"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node',p=None) -> 'Node':
        head = root  # save head to return

        def find_next(node):
            if not node: 
                return

            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    tmp = node.next
                    while tmp:
                        if tmp.left:
                            node.left.next = tmp.left
                            break
                        elif tmp.right:
                            node.left.next = tmp.right
                            break
                        else:
                            tmp = tmp.next

            if node.right:
                tmp = node.next
                while tmp:
                    if tmp.left:
                        node.right.next = tmp.left
                        break
                    elif tmp.right:
                        node.right.next = tmp.right
                        break
                    else:
                        tmp = tmp.next

            # the recurse order of right before left is important
            find_next(node.right)
            find_next(node.left)

        find_next(root)

        return head