class Solution:
    
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp=[[-1]*2 for i in range(n)]
        n = len(prices)
        
        @lru_cache(None)
        def dpfind(i, needBuy):
            if i == n:
                return 0
            
            ans = dpfind(i+1, needBuy)  # Skip
            if needBuy:
                ans = max(ans, dpfind(i+1, False) - prices[i])
            else:
                ans = max(ans, dpfind(i+1, True) + prices[i] - fee)
            return ans
                
        return dpfind(0, True)