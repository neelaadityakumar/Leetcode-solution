class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        disc = [-1]*n
        low = [-1]*n
        
        network = [[] for _ in range(n)]
        for a, b in connections:
            network[a].append(b)
            network[b].append(a)
        
        def tarjan(prev, curr, time, disc, low, network, ans):
            if disc[curr] != -1:
                return disc[curr]

            disc[curr] = time
            low[curr] = time
            
            for next in network[curr]:
                if next != prev:
                    lowOfNext = tarjan(curr, next, time+1, disc, low, network, ans)
                    low[curr] = min(low[curr], lowOfNext)
#after backtracking, the value of low[next] is still higher than disc[curr], then there is no looped #connection, meaning that the edge between curr and next is a bridge, so we should add it to our answer #array (ans).
                    if low[next] > disc[curr]:
                        ans.append([next,curr])
                        
            return low[curr]
        
        ans = []
        tarjan(0, 0, 0, disc, low, network, ans)
        
        return ans