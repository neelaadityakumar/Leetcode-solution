class Solution(object):
    def climbStairs(self, n,dp={}):
        """
        :type n: int
        :rtype: int
        """
        if n in dp:
            return dp[n]
        if n ==0 or n==1:
            return 1
        else:
            dp[n]= self.climbStairs(n-1,dp)+self.climbStairs(n-2,dp)
        return dp[n]
        