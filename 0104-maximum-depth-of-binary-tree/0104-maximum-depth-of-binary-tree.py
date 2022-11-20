# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=0
    def helper(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 0
        h= 1+max(self.helper(root.left),self.helper(root.right))
        self.res=max(h,self.res)
        return h
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.res