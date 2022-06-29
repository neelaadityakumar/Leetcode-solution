class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        discoveryTime = [-1]*n
        lowestNodeReachable = [-1]*n
        
        network = [[] for _ in range(n)]
        for a, b in connections:
            network[a].append(b)
            network[b].append(a)
        
        def tarjan(prev, curr, time, discoveryTime, lowestNodeReachable, network, ans):
            if discoveryTime[curr] != -1:
                return discoveryTime[curr]

            discoveryTime[curr] = time
            lowestNodeReachable[curr] = time
            
            for next in network[curr]:
                if next != prev:
                    lowOfNext = tarjan(curr, next, time+1, discoveryTime, lowestNodeReachable, network, ans)
                    lowestNodeReachable[curr] = min(lowestNodeReachable[curr], lowOfNext)
#after backtracking, the value of low[next] is still higher than disc[curr], then there is no looped #connection, meaning that the edge between curr and next is a bridge, so we should add it to our answer #array (ans).
                    if lowestNodeReachable[next] > discoveryTime[curr]:
                        ans.append([next,curr])
                        
            return lowestNodeReachable[curr]
        
        ans = []
        tarjan(0, 0, 0, discoveryTime, lowestNodeReachable, network, ans)
        
        return ans