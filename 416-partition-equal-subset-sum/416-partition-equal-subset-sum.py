class Solution:
    def subset_sum_part2(self,arr,target,index,dp):
        if index==len(arr):
            if target==0:
                return True
            else:
                return False
        if dp[index][target]!=-1:
            return dp[index][target]
                      
                      
        target-=arr[index]
        if self.subset_sum_part2(arr,target,index+1,dp)==True:
            dp[index][target]=True
            return True
        target+=arr[index]

        if self.subset_sum_part2(arr,target,index+1,dp)==True:
            dp[index][target]=True
            return True
    
        dp[index][target]=False
        return False

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