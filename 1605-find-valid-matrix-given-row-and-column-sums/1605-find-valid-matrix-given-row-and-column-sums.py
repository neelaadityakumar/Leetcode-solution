class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        arr = [[0] * n for _ in range(m)]
        
        def dfs(r, c):
            if r == m or c == n:
                return
            arr[r][c] = min(rowSum[r], colSum[c])
            if arr[r][c] == rowSum[r]:
                colSum[c] -= rowSum[r]
                dfs(r+1, c)
            else:
                rowSum[r] -= colSum[c]
                dfs(r, c + 1)
        
        dfs(0, 0)
        return arr