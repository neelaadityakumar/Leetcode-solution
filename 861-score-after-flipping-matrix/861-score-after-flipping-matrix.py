class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        for x in range(row):
            if grid[x][0] == 0:
                for y in range(col):
                    if grid[x][y] == 1:
                        grid[x][y] = 0
                    else:
                        grid[x][y] = 1

        for y in range(col):
            onesCount = 0
            for x in range(row):
                if grid[x][y] == 1:
                    onesCount += 1

            if onesCount < row - onesCount: # less ones than zeros
                for x in range(row):
                    if grid[x][y] == 1:
                        grid[x][y] = 0

                    else: 
                        grid[x][y] = 1
        sum=0
        for i in grid:
            dig=0
            for j in i:
                dig=dig*10+j
            sum+=int(str(dig),2)
        return (sum)