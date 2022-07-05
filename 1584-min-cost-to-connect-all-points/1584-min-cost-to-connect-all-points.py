class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        weights, roots = self.compute_weights(points)
        cost = 0
        edges_needed = len(points) - 1
        while len(weights) and edges_needed > 0:
            weight, i, j = heappop(weights)
            root_j = self.find(roots, j)
            root_i = self.find(roots, i)
            if root_j == root_i:
                continue
            cost += weight
            edges_needed -= 1
            roots[root_j] = root_i
        return cost
    
    def compute_weights(self, points):
        h = []
        roots = []
        for i, a in enumerate(points):
            roots.append(i)
            for j in range(i + 1, len(points)):
                b = points[j]
                weight = self.compute_weight(a, b)
                h.append((weight, i, j))
        heapify(h)
        return h, roots
    
    
    def compute_weight(self, a, b):
        x1, y1 = a
        x2, y2 = b
        return abs(x1 - x2) + abs(y1 - y2)
    
    
    def find(self, roots, i):
        if roots[i] == i:
            return i
        roots[i] = self.find(roots, roots[i])
        return roots[i]