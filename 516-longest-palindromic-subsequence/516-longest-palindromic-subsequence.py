class Solution:
    def longestPalindromeSubseq(self, s) :
        n = len(s)
        
        cache = {}
        def helper(l, r):
            if (l,r) in cache: return cache[(l,r)]
            if l > r: return 0
            if l == r: return 1
            if s[l] == s[r]:
                cache[(l,r)] = helper(l + 1, r - 1) + 2
                return cache[(l, r)]
            cache[(l,r)] = max(helper(l, r - 1), helper(l + 1, r))
            return cache[(l, r)]

        return helper(0, n - 1) 