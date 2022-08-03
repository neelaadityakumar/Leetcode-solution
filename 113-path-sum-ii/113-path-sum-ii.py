# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def path(root,sum,ls,res):
            if not root:
                return
            if not root.left and not root.right and sum == root.val:
                ls.append(root.val)
                res.append(ls)
                return
            path(root.left, sum-root.val, ls+[root.val], res)
            path(root.right, sum-root.val, ls+[root.val], res)
        res = []
        path(root, targetSum, [], res)
        return res