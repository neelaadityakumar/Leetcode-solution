class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot = len(nums) * (len(nums) - 1) // 2
        good = 0
        dic = {}
        
        for i,num in enumerate(nums):
            v = i - num
            good += dic.get(v, 0)
            dic[v] = dic.get(v, 0) + 1
        
        return tot - good