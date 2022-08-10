# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxDiff(root,mn,mx):
            if not root:
                return abs(mn-mx)
            
            leftmx=maxDiff(root.left,min(mn,root.val),max(mx,root.val))
            rightmx=maxDiff(root.right,min(mn,root.val),max(mx,root.val))
            return max(leftmx,rightmx)
        return maxDiff(root,sys.maxsize,-1*sys.maxsize)