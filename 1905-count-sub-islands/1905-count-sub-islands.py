class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def isIsland(i, j):
            flag = True
            if grid1[i][j]!=1:
                flag = False
            
            if i-1>=0 and grid2[i-1][j]==1:
                grid2[i-1][j] = 2
                flag = isIsland(i-1,j) and flag and grid1[i-1][j]
                    
            if i+1<n and grid2[i+1][j]==1:
                grid2[i+1][j] = 2
                flag = isIsland(i+1,j) and flag and grid1[i+1][j]
            
            if j-1>=0 and grid2[i][j-1]==1:
                grid2[i][j-1] = 2
                flag = isIsland(i,j-1) and flag and grid1[i][j-1]
            
            if j+1<m and grid2[i][j+1]==1:
                grid2[i][j+1]=2
                flag = isIsland(i,j+1) and flag and grid1[i][j+1]
            return flag
            
        
        count = 0
        n = len(grid2)
        m = len(grid2[0])
        for i in range(n):
            for j in range(m):
                if grid2[i][j]==1:
                    grid2[i][j] = 2
                    if isIsland(i, j):
                        count += 1
        return count