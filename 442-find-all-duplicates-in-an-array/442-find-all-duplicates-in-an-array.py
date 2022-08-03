class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # result = []
        # for x in nums:
        #     if nums[abs(x)-1] < 0:
        #         result.append(abs(x))
        #     else:
        #         nums[abs(x)-1] = -1*nums[abs(x)-1]
        # return result
    
        i=0
        while i<len(nums):
            idx=nums[i]-1
            if nums[i]!= nums[idx]:
                nums[i],nums[idx]=nums[idx],nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                yield nums[i]