class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        def solve(r,c):
            grid[r][c]=-1
            nonlocal ans
            ans+=1
            for i in range(len(grid)):
                if grid[i][c]==1:
                    solve(i, c)

            for j in range(len(grid[0])):
                if grid[r][j]==1:
                    solve(r, j)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans=0
                    solve(i,j)
                    if ans>1:
                        count+=ans
        return count