# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int, mem:List[TreeNode]={1:[TreeNode(0)]}) -> List[Optional[TreeNode]]:
        if N%2==0:return []             # if even no balanced trees are possible
        
        
        if N in mem: return mem[N]      # Found a known subtree
        
        for i in range(1,N,2): # From left=1 right=N-2 to left=N-2 right=1 for each tree root
            
            for left in self.allPossibleFBT(i,mem):             # from 1, 3, 5, ...
                for right in self.allPossibleFBT(N-i-1,mem):    # from N-2, N-4, ... ie N=3: 1 or N=5: 3, 1
                    
                    root = TreeNode(0)
                    root.left, root.right = left, right
                    
                    if N in mem: mem[N].append(root)        # add to size N remembered trees 
                    else: mem[N] = [root]                   # remember trees of size N
                        
        return mem[N] 