class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g=defaultdict(list)
        
        for edge, prob in zip(edges, succProb):
            u,v, cost = edge[0], edge[1], prob
            g[u].append([v, log2(1/cost)])
            g[v].append([u, log2(1/cost)])
            
        def dijkstra(src, dest):
            dist=[float('inf')]*n 
            minHeap = [(0, src)]
            dist[src]=0
            while minHeap:
                d, u = heapq.heappop(minHeap)
                for (v, cost) in g[u]:
                    if dist[v]>cost+dist[u]:
                        dist[v]=cost+dist[u]
                        heapq.heappush(minHeap, (dist[v], v))
            return dist[dest]
        print(g)
        x = dijkstra(start, end)
        return 1/(2**x)