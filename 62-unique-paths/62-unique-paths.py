class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path=[[0]*m for i in range(n)]
        for i in range(n):
            path[i][0]=1
        for i in range(m):
            path[0][i]=1
        for i in range(1,n):
            for j in range(1,m):
                path[i][j]=path[i][j-1]+path[i-1][j]
        return path[-1][-1]