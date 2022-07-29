class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i=0
    
        n=len(matrix)
        m=len(matrix and matrix[0])
        j=m-1
        while i<n and j>=0:
            if target>matrix[i][j]:
                i+=1
            elif target<matrix[i][j]:
                j-=1
            else:
                return True
        return False
        