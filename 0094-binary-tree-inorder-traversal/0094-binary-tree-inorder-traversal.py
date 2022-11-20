# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
    def inorderTraversal(self, root: Optional[TreeNode],res=[]) -> List[int]:
        self.helper(root)
        return self.res
    def helper(self, root: Optional[TreeNode],res=[]) -> List[int]:
        if root:
            if root.left:
                self.helper(root.left)
            self.res.append(root.val)
            if root.right:
                self.helper(root.right)
        