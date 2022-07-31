class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        maxv=0
        for i,h in enumerate(height):
            start=i
            while stack and stack[-1][1]>h:
                ind,val=stack.pop()
                maxv=max(maxv,val*(i-ind))
                start=ind
            stack.append((start,h))
        
        for i,h in stack:
            maxv=max(maxv,h*(len(height)-i))
        return maxv