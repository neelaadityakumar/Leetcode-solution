class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        indegree = defaultdict(int)
        graph = defaultdict(list)
        queue = deque()
        
        for r in range(m):
            for c in range(n):
                for r1, c1 in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= r1 < m and 0 <= c1 < n and matrix[r1][c1] > matrix[r][c]:
                        graph[(r1, c1)].append((r, c))
                        indegree[(r, c)] += 1
                        
                if indegree[(r, c)] == 0: queue.append((r, c, 1))
                    
        while queue:
            r, c, d = queue.popleft()
            
            for r1, c1 in graph[(r, c)]:
                indegree[(r1, c1)] -= 1
                if indegree[(r1, c1)] == 0:
                    queue.append((r1, c1, d+1))
                    
        return d