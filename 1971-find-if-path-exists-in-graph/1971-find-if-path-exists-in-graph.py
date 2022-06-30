class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        visited = [False]*n
        d = defaultdict(list)
		#store the undirected edges for both vertices
        for i in edges:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
            
        #create a queue as we will apply BFS
        q = [start]
        while q:
            curr = q.pop(0)  #pop the first element as we do in queue
            if curr == end:  #if its the end then we can return True
                return True
            elif curr in d and not visited[curr]: #else if it is not the end then check whether its visited or not
                q+=d[curr]  #add the adjacent vertices of the current node to the queue
            visited[curr] = True  #mark this curr vertex as visited = True, so that we dont visit this vertex again
        return False  #return False if the queue gets empty and we dont reach the end