class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        pq = [(0, 0, 0)]
        visited = set()

        while pq:
            cost, r, c = heapq.heappop(pq)

            # we find the answer
            if (r, c) == (nrow - 1, ncol - 1):
                return cost

            if (r, c) in visited:
                continue
            visited.add((r, c))

            # Four neighbours
            for d, (dr, dc) in enumerate(directions, 1):
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= nrow or nc < 0 or nc >= ncol or (nr, nc) in visited:
                    continue
                if d == grid[r][c]:
                    heapq.heappush(pq, (cost, nr, nc))
                else:
                    heapq.heappush(pq, (cost + 1, nr, nc))