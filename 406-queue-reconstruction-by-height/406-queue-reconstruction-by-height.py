class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        people.sort(key=lambda p:(p[0],-p[1]))
        ans = [0]*n
        
        def update(i, diff):  # update BIT
            while i<=n:
                bit[i] += diff
                i+=(i&(-i))
            
        def prefixSum(i): # calculate prefix sum using BIT
            s = 0
            while i>0:
                s += bit[i]
                i-=(i&(-i))
            return s
    
        def findKth(k): # find position such that there are k empty slots to the left of it
            return bisect_right(range(n), k, key = lambda i:prefixSum(i+1))
        
        # Initialize BIT 
        bit = [0]*(n+1)
        for i in range(1, n+1):
            update(i, 1)
        
        # Iteratre people and find appropriate position for each person
        for p in people:
            pos = findKth(p[1])
            update(pos+1, -1)
            ans[pos]=p
        return ans