class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # importing heap module
        import heapq
        
        l1 = []
        
        # convert list into heap
        heapq.heapify(l1)
        
        # using max heap and push a,b,c into max heap
        heapq.heappush(l1, -1*a)
        heapq.heappush(l1, -1*b)
        heapq.heappush(l1, -1*c)
        
        # count variable to store steps
        count = 0
        while True:
            
            # poping biggest 2 piles
            ans1 = heapq.heappop(l1)
            ans2 = heapq.heappop(l1)
            
            # terminating condition, if either of one or both of them is equal to zero then return the steps
            if ans1 == 0 or ans2 == 0:
                return count
            
            # subtracting 1 stone from biggest 2 piles
            temp = abs(ans1) - 1
            temp1 = abs(ans2) - 1
            
            # again pushing modified values of piles into the heap
            heapq.heappush(l1, -1*temp)
            heapq.heappush(l1, -1*temp1)
            
            # incrementing the step number
            count += 1