# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root,diameter):
            if not root:
                return 0
            
            left = height(root.left,diameter)
            right = height(root.right,diameter)
            diameter[0] = max(diameter[0], left + right)
            return max(left, right) + 1
        
        diameter = [0]
        height(root,diameter)
        return diameter[0]