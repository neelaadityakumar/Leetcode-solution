class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.visited = [False] * (n + 1)
        self.color = [False] * (n + 1)        
        graph = defaultdict(list)
        
        for w, v in dislikes:
		    # I used to think disliking is one-way, but in this case, we should consider them bi-directional
            graph[w].append(v)
            graph[v].append(w)
        
        for node in range(1, n + 1):
            if not self.visited[node]:
                
                if not self.traverse(graph, node):
                    return False
        return True
    
    def traverse(self, graph, node):
        self.visited[node] = True
        for v in graph[node]:
            if not self.visited[v]:
                self.color[v] = not self.color[node]
                self.traverse(graph, v)
            else:
                if self.color[v] == self.color[node]:
                    return False
        return True