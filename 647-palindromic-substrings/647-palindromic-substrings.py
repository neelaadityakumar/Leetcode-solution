class Solution:
    def dp(self, s, i, j, dp):
        ans = False
        if i >= j:
            return True

        if dp[i][j]:
            return dp[i][j]

        if s[i] == s[j]:
            ans = self.dp(s, i+1, j-1, dp)

        dp[i][j] = ans
        return ans


    def countSubstrings(self, s):
        cnt = 0
        n = len(s)
        dp = [[False]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(i, n):
                if self.dp(s, i, j, dp):
                    cnt += 1

        return cnt
        
        
        count(dp,len(s),0)
        return self.out
        
        
