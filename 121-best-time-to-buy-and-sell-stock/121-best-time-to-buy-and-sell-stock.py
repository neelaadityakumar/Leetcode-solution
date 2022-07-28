class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp=prices[0]
        pr=0
        for i in range(1,len(prices)):
            pr=max(pr,prices[i]-bp)
            bp=min(bp,prices[i])
        return pr