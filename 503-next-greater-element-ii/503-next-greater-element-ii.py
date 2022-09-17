class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st=[]
        n=len(nums)
        res=[-1]*n
        for i in range(n):
            while st and nums[st[-1]]<nums[i]:
                res[st.pop()]=nums[i]
            st.append(i)
        for i in range(n):
            while st and nums[st[-1]]<nums[i]:
                res[st.pop()]=nums[i]
        return res            