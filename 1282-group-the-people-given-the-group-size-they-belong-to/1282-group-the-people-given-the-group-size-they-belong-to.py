class Solution:
    def groupThePeople(self, g: List[int]) -> List[List[int]]:
        ans=[]
        d=defaultdict(list)
        for i in range(len(g)) :
            d[g[i]].append(i)
            
        for val in d:
            if len(d[val])>val:
                for i in range(0,len(d[val]),val):
                    ans+=[d[val][i:i+val]]
            else:
                ans+=[d[val]]
        return ans