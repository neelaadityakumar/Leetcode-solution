# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, A):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        return self.buildTree(A[::-1], float('inf'),float('-inf'))

    def buildTree(self, A, lbound,rbound):
        if not A or A[-1] > lbound or A[-1] < rbound: return None
        node = TreeNode(A.pop())
        node.left = self.buildTree(A, node.val,rbound)
        node.right = self.buildTree(A, lbound,node.val)
        return node