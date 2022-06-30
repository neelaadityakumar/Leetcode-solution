class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(graph,n,curr,viz):
            viz[curr]=True
            for i in graph[curr]:
                if not viz[i]:
                    dfs(graph,n,i,viz)
            
            
            
        n=len(rooms)
        graph=defaultdict(list)
        for i in range(n):
            for j in rooms[i]:
                graph[i].append(j)
        print(graph)
        viz=[False]*n
        dfs(graph,n,0,viz)
        for i in range(n):
            if not viz[i]:
                return False
        return True