class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0]*(cols) for _ in range(rows)]
        max_side = 0
        for i in range(rows):
            dp[i][0]=int(matrix[i][0])
            max_side=max(max_side,dp[i][0])
        for j in range(cols):
            dp[0][j]=int(matrix[0][j])
            max_side=max(max_side,dp[0][j])
        
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[r][c] == '1':
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1 # Be careful of the indexing since dp grid has additional row and column
                    max_side = max(max_side, dp[r][c])
                
        return max_side * max_side