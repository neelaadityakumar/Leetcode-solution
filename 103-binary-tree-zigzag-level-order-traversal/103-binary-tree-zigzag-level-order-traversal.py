# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return root
        queue=[root]
        res=[]
        last=1
        while (queue):
            temp=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                temp+=[node.val]
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            res+=[temp[::last]]
            last*=-1
        return res
            
        
        