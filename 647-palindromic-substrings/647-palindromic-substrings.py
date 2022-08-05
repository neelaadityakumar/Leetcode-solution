class Solution:
    def countSubstrings(self, s: str) -> int:
        out = 0 
        dp = [[False]*len(s) for _ in range(len(s))]
        # Fill the diagonal by True
        for i in range(len(s)):
            dp[i][i] = True
            out += 1  # append each char, since they are palindrome

        #Fill the DP table
        for i in range(len(s)): # traverse in backward
            for j in range(i):   # traverse forward starting from the index from the outer loop
                if s[i] == s[j]:          # if the characters match
                    if i-j == 1 or dp[i-1][j+1]:
                        dp[i][j] = True    # mark the location as True b/c it is palindrom
                        out += 1
        return out
