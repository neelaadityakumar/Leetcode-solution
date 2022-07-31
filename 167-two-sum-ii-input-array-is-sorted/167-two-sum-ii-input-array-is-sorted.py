class Solution(object):
    def twoSum(self, nums, t):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        s=0
        e=len(nums)-1
        while s<e:
            if nums[s]+nums[e]==t:
                return [s+1,e+1]
            elif nums[s]+nums[e]<t:
                s+=1
            else:
                e-=1
                
            