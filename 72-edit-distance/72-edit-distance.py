class Solution:
    '''
    Bottom Up
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        edit=[[0]*(m+1) for i in range(n+1)]
        for i in range(n+1):
            edit[i][0]=i
        for i in range(m+1):
            edit[0][i]=i
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    edit[i][j]=edit[i-1][j-1]
                else:
                    edit[i][j]=1+min(edit[i-1][j],edit[i-1][j-1],edit[i][j-1])
                    
        return edit[-1][-1]
    
    '''
    
    def minDistance(self, s1, s2) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == 0: return j  # Need to insert j chars
            if j == 0: return i  # Need to delete i chars
            if s1[i-1] == s2[j-1]:
                return dp(i-1, j-1)
            return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1
        
        return dp(len(s1), len(s2))
