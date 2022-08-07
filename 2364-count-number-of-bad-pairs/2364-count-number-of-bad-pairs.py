class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dic={}
        for i in range(n):
            if nums[i] - i not in dic:
                dic[nums[i] - i]=0
            dic[nums[i] - i]+=1

        ans = n * (n - 1) // 2
        for x in dic:
            if dic[x] > 1:
                ans -= dic[x] * (dic[x] - 1) // 2
        
        return ans