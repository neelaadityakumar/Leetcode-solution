class Solution(object):
    def climbStairs(self, n,dp={}):
        """
        :type n: int
        :rtype: int
        """
        if n in dp:
            return dp[n]
        if n ==1 or n==2:
            dp[n]=n
        else:
            dp[n]= self.climbStairs(n-1,dp)+self.climbStairs(n-2,dp)
        return dp[n]
        