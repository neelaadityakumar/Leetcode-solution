class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(left,right,curr,ans):
            if right<left:
                return
            if not right and not left:
                ans.append(curr)
                return
                
            if left:
                gen(left-1,right,curr+"(",ans)
            if right:
                gen(left,right-1,curr+")",ans)
        if not n:
            return []
        left, right, ans = n, n, []

        gen(left,right,"",ans)
        return ans
        
# def generateParenthesis(self, n):
#     if not n:
#         return []
#     left, right, ans = n, n, []
#     self.dfs(left,right, ans, "")
#     return ans

# def dfs(self, left, right, ans, string):
#     if right < left:
#         return
#     if not left and not right:
#         ans.append(string)
#         return
#     if left:
#         self.dfs(left-1, right, ans, string + "(")
#     if right:
#         self.dfs(left, right-1, ans, string + ")")