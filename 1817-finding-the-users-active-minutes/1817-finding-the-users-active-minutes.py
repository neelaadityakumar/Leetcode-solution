class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dic=defaultdict(set)
        for log in logs:
            ids,time=log
            dic[ids].add(time)
        ans=[0]*k
        for x in dic:
            l=len(dic[x])
            ans[l - 1] += 1
        return ans
        
       