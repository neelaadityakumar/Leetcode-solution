class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        n=len(nums)
        out=[]
        for i in range(n):
            out.append(p)
            p*=nums[i]
        p=1
        for i in range(n-1,-1,-1):
            out[i]*=p
            p*=nums[i]
        return out