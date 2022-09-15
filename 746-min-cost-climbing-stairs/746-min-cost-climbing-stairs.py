class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[max(cost)+1]*n
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,n):
            dp[i]=min(dp[i-1],dp[i-2])+cost[i]
        # ==== 4. Think again what you are trying to find in your dp array.
		# To finish the stairs journey in this problem, there are 2 ways to be the last step before we finish
		# the stairs. The last step might come from both last two stairs. So, we want to know the min of 
		# the costs of last 2 stairs from our dp array.
        return min(dp[-1],dp[-2])