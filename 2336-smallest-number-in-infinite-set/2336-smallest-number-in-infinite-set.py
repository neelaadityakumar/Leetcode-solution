class SmallestInfiniteSet:

    def __init__(self):
        self.set = set()
        self.heap = []
        for i in range(1,1001):
            heappush(self.heap, i)
            self.set.add(i)
            
    def popSmallest(self):
        """
        :rtype: int
        """
        s_number = heapq.heappop(self.heap)
        self.set.remove(s_number)
        return s_number

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num in self.set:
            pass
        
        else:
            heapq.heappush(self.heap, num)
            self.set.add(num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)