class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(cur, path, res):
            
            new_path = list(path)
            new_path.append(cur)
            
            if cur == len(graph)-1:
                res.append(new_path)
                return
            
            for neighbor in graph[cur]:
                dfs(neighbor, new_path, res)
        
        res = []
        dfs(0, [], res)
        return res