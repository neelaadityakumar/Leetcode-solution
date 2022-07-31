class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[sys.maxsize]*len(nums)
        dp[0]=0
        for i in range(1,len(nums)):
            for j in range(i):
                if j+nums[j]>=i:
                    dp[i]=min(dp[i],dp[j]+1)
        return dp[len(nums)-1]
        
            