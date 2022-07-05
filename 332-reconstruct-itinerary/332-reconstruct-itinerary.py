class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def createGraph(tickets):
            adjlist = defaultdict(list)
            for u, v in tickets:
                # add out edge node
                adjlist[u].append(v)
                # ensure nodes with zero out degree are also included for in-out-degree calculation below
                #if v not in adjlist:
                #    adjlist[v] = []                    
            return adjlist
        
        def sortOutEdges(adjlist):
            # sort according to the specific task requirements
            # reverse would simplify dfs later because we could remove
            # nodes faster from the back of the array instead of from the beginning
            for u, v_lst in adjlist.items():
                v_lst.sort(reverse = True)
    
        # do dfs and remove outgoing edges until we are stuck, then backtrack
        # until all edges are visited, and if a node has no more outgoing edges
        # add it to the end of the result
        def dfs(start, adjlist):
            while adjlist[start]:
                # optimization: we sorted the array in reverse order above
                # to remove edges faster from the end of the array here
                v = adjlist[start].pop()
                dfs(v, adjlist)
			# backtrack when all out edges are visited (removed) and add the node to the result,
            # optimization: according to the algorithm we should insert into the beginning of the array,
            # but we can optimize here to add it at the end and then reverse the result later
            res.append(start)
            
        res = []
        # create a standard adjacency list
        adjlist = createGraph(tickets) 
        # sort edges because we are specifically asked for smaller lexical order 
        sortOutEdges(adjlist)        
        # according to the task, the start is JFK and the Eulerian path does exist
        # so we don't need to check the existance and find a start node
        # as we would have to do in a general Hierholzer's Algorithm
        #in_deg, out_deg = countInOutDegrees(adjlist)        
        #if not hasEulerianPath(adjlist, in_deg, out_deg):
        #    return []
        #start = findStartNode(in_deg, out_deg)                
        start = 'JFK'
        # do dfs until all edges are visited
        dfs(start, adjlist)
        # revert the result because we optimized by adding to the end of the result in dfs above
        return res[::-1]
		
		#def countInOutDegrees(adjlist):
        #    in_deg = defaultdict(int)
        #    out_deg = defaultdict(int)            
        #    for u, v_lst in adjlist.items():
        #        out_deg[u] = len(v_lst)
        #        for v in v_lst:
        #            in_deg[v] += 1
        #    return in_deg, out_deg
                    
        #def hasEulerianPath(adjlist, in_deg, out_deg):
        #    starts, ends = 0, 0 
        #    for u in adjlist:                                
        #        if abs(in_deg[u] - out_deg[u]) > 1:                    
        #            return False
        #        elif out_deg[u] - in_deg[u] == 1:
        #            starts += 1
        #        elif in_deg[u] - out_deg[u] == 1:
        #            ends += 1                     
        #    return (starts == 0 and ends == 0) or (starts == 1 and ends == 1)
            
        #def findStartNode(out_deg, in_deg):
        #    start = None
        #    for u in out_deg:
        #        if out_deg[u] - in_deg[u] == 1:
        #            return u
        #        if out_deg[u] > 0:
        #            start = u
        #    return start