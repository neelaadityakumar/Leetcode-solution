# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):

        def bfs(root: TreeNode) -> None:
            dq = collections.deque([root])
            self.seen.add(root.val)
            while dq:
                node = dq.popleft()
                if node.left:
                    node.left.val = 2 * node.val + 1
                    dq.append(node.left)
                    self.seen.add(node.left.val)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    dq.append(node.right)
                    self.seen.add(node.right.val)
            
        self.seen = set()
        if root:
            root.val = 0
            bfs(root)
        
    def find(self, target: int) -> bool:
        return target in self.seen 

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)