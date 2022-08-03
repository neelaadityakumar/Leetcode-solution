class Solution:
    def nextGreaterElement(self, findNums: List[int], nums: List[int]) -> List[int]:
        cache, st = {}, []
        for x in nums:
            while st and st[-1] < x:
                cache[st.pop()] = x
            st.append(x)
        result = [-1]*len(findNums)
        for idx,x in enumerate(findNums):
            if x in cache:
                result[idx] = cache[x]
        return result