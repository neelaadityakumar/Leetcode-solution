class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start, end, tmp):
            ans.append(tmp[:])
            for i in range(start, end):
                backtrack(i+1, end, tmp+[nums[i]])
        ans = []
        backtrack(0, len(nums), [])
        return ans