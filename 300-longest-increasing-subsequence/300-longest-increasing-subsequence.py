class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n<1:
            return 0
        long=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    long[i]=max(long[i],long[j]+1)
                
        return max(long)
        