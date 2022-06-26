class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        c=len(nums)-1
        for i in range(len(nums)//2):
            ans=max(ans,nums[i]+nums[c])
            c-=1
        return ans