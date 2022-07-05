class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        # build graph
        graph = defaultdict(dict)
        for s, e, w in edges:
            graph[s][e] = w
            graph[e][s] = w
            
        # Distance to last node
        dist_to_last = {node: float('inf') for node in range(1, n+1)}
        dist_to_last[n] = 0
        
        # number of restricted path to last node
        count_path = {node: 0 for node in range(1, n+1)}
        count_path[n] = 1
        
        # Dijkstra
        ## calculated nodes
        decided = set()
        ## heap for candidate nodes
        candidates = [(0,n)]
        while candidates:
            _, node = heapq.heappop(candidates)
            if node in decided:
                continue
            decided.add(node)
            for neigh in graph[node]:
                if neigh in decided:
                    continue
                new_dist = graph[node][neigh] + dist_to_last[node]
                
                # update distance
                if new_dist < dist_to_last[neigh]:
                    dist_to_last[neigh] = new_dist
                    heapq.heappush(candidates, (dist_to_last[neigh], neigh))
                    
                # update number of paths
                if dist_to_last[neigh] > dist_to_last[node]:
                    count_path[neigh] += count_path[node]


        return count_path[1] % (10 ** 9 + 7)