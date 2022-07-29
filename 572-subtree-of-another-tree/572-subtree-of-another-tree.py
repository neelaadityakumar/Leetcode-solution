# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        def convert(p):
            return "s" + str(p.val) + "e" + convert(p.left) + convert(p.right) if p else "$"
        
        return convert(t) in convert(s)