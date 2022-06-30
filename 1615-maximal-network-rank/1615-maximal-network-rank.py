class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adlist=[[] for x in range(n)]            # adjacency list creation
        for i in roads:
            adlist[i[0]].append(i[1])
            adlist[i[1]].append(i[0])
			
        l=[]           
        for i in range(len(adlist)):
            for j in range(i+1,len(adlist)):
                if i in adlist[j] and j in adlist[i]:              #   if both vertex are directly connected ,count only once between vertex
                    l.append(len(adlist[i])+len(adlist[j])-1)
                else:                                      # if vertex are not directly connected
                    l.append(len(adlist[i])+len(adlist[j]))
        return max(l) 