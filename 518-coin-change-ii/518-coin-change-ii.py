class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """  
        def f(i,arr,target,dp):
            if target == 0:
                return 1
            if i >= len(arr):
                return 0
            if dp[i][target] != -1:
                return dp[i][target]
            take = 0
            if arr[i] <= target:
                take = f(i,arr,target-arr[i],dp)
            nottake = f(i+1,arr,target,dp)
            dp[i][target] = take + nottake
            return take + nottake
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        return f(0,coins,amount,dp)