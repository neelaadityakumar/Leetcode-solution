class Solution:
    
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp=[[-1]*2 for i in range(n)]
        n = len(prices)
        
        def profit(i, needBuy):
            if i == n:
                return 0
            if dp[i][needBuy]==-1:
                ans = profit(i+1, needBuy)  # Skip
                if needBuy:
                    ans = max(ans, profit(i+1, 0) - prices[i])
                    dp[i][1]=ans
                else:
                    ans = max(ans, profit(i+1, 1) + prices[i] - fee)
                    dp[i][0]=ans
            return dp[i][needBuy]
                
        return profit(0, 1)