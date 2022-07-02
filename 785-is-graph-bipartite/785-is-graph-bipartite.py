class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # -1 -> uncoloured
        color = defaultdict(lambda: -1)
        q = []
		# just in case graph is disconnected
        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                #visiting with 0 color initially
                q.append(node)
                while len(q):
                    curr = q.pop(0)
                    for adj_node in graph[curr]:
                        if color[adj_node] == color[curr]:
                            return False
                        if color[adj_node] == -1:
                            color[adj_node] = 1-color[curr] 
                            #alternate color
                            q.append(adj_node)
        return True