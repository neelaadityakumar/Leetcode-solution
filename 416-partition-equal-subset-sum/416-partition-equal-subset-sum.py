class Solution:
    def subset_sum_part2(self,arr,target,index,dp):
        if index==len(arr):
            if target==0:
                return True
            else:
                return False
        if dp[index][target]!=-1:
            return dp[index][target]
                      
                      
        res=self.subset_sum_part2(arr,target-arr[index],index+1,dp) or self.subset_sum_part2(arr,target,index+1,dp)
        dp[index][target]=res

       
    
        return res

    def canPartition(self, nums):
        sum=0
        for i in range(0,len(nums)):
            sum+=nums[i]
        if sum%2==1:
            return False

        target=sum//2
        index=0
        n=len(nums)
        dp=[[-1 for i in range(target+1)] for j in range(n+1)]
        return self.subset_sum_part2(nums,target,index,dp)