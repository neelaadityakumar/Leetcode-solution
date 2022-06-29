class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(cur, path, res):
            
            new_path = path+[cur]
            
            if cur == len(graph)-1:
                res.append(new_path)
                return
            
            for neighbor in graph[cur]:
                dfs(neighbor, new_path, res)
        
        res = []
        dfs(0, [], res)
        return res