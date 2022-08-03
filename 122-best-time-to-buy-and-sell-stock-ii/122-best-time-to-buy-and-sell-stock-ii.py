class Solution(object):
    def dfs(self, prices, index, buy, n, dp):
        if index == n:
            return 0
        
        if dp[index][buy]!=-1:
            return dp[index][buy]
        
        buying = selling = 0
        
        if buy:
            buying = max(
                -prices[index]+self.dfs(prices, index+1, False, n, dp),
                self.dfs(prices,index+1, True, n, dp)
            )
        else:
            selling = max(
                prices[index]+self.dfs(prices, index+1, True, n, dp),
                self.dfs(prices,index+1, False, n, dp)
            )
        dp[index][buy] =  max(buying, selling)
        return dp[index][buy]
    
    def maxProfit(self, prices):
        dp = [[-1 for i in range(2)] for j in range(len(prices))]
        return self.dfs(prices, 0, True, len(prices), dp)