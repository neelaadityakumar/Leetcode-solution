class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # white -> uncoloured
        table = defaultdict(lambda: -1)
        q = []
		# just in case graph is disconnected
        for node in range(len(graph)):
            if node not in table:
                table[node] = 0
                q.append(node)
                while len(q):
                    curr = q.pop(0)
                    for adj_node in graph[curr]:
                        if table[adj_node] == table[curr]:
                            return False
                        if table[adj_node] == -1:
                            table[adj_node] = 1 if table[curr] == 0 else 0
                            q.append(adj_node)
        return True