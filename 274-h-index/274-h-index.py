class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        arr = [0] * (n + 2)
        for i in range(n):
            if citations[i] > n:
                arr[n + 1] += 1
            else:
                arr[citations[i]] += 1
            
        accSum = arr[n + 1]
        # iterate in reversed order from the last second one
        for i in range(n, -1, -1):
            accSum += arr[i]
            if accSum >= i:
                return i
        return 0