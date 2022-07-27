class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s)) ]
        for i in range(len(s)):
            dp[i][i]=True
        ans=s[0]
        for i in range(len(s)):
            for j in range(i):
                if s[i]==s[j] and (dp[i-1][j+1] or j==i-1):
                    dp[i][j]=True
                    if i-j+1>len(ans):
                        ans=s[j:i+1]
        return ans