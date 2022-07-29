# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def inorder(self,root,a):
        if root is None:
            return
        self.inorder(root.left,a)
        a.append(root.val)
        self.inorder(root.right,a)

    def __init__(self, root: TreeNode):
        self.a=[]
        self.inorder(root,self.a)
        
        
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.a.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.a)
            
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()