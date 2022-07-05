class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph=defaultdict(list)
        for u,v,cnt in edges:
            graph[u].append((cnt+1,v))
            graph[v].append((cnt+1,u))
		#maintains minimum dist to reach i-th node from 0-th node
        dist=[sys.maxsize]*n
        dist[0]=0
		#priority queue (weight,node)
        pq=[(0,0)]
        while pq:
            d,node=heapq.heappop(pq)
            for nd,nei in graph[node]:
                if d+nd<dist[nei]:
                    dist[nei]=d+nd
                    heapq.heappush(pq,(d+nd,nei))
        ans=0
		#This covers all n nodes in initial edges graph
        for node,weight in enumerate(dist):
            if weight<=maxMoves: 
                ans+=1
		#This checks for cnt between edges and also checks for cases of overlapping of cnts
        for u,v,weight in edges:
            if dist[u]>maxMoves and dist[v]>maxMoves:
                continue
            count1=max(0,maxMoves-dist[u])
            count2=max(0,maxMoves-dist[v])
            ans+=min(count1+count2,weight)
        return ans