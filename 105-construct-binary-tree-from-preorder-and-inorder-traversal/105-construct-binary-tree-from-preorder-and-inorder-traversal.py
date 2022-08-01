# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
""""
Recursive
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(0)
        lo, hi = 0, len(preorder) - 1
        nodes = [(root, lo, hi)]
        lut = {inorder[i]: i for i in range(len(inorder))} 
              # use a look up table to get the index
              # of an element in constant time.
        for i in range(len(preorder)):
            curr, lo, hi = nodes.pop()
            curr.val = preorder[i]
            mid = lut[curr.val]
            if mid < hi:
                curr.right = TreeNode(0)
                nodes.append((curr.right, mid + 1, hi))
            if lo < mid:
                curr.left = TreeNode(0)
                nodes.append((curr.left, lo, mid - 1))
        return root