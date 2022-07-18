class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def count(arr):
            dp = [0]*len(arr) #dp[i] records the number of element that lower than rating[i] on the left
            ans = 0
            for i in range(len(arr)):
                for j in range(i):
                    if arr[i] > arr[j]:
                        dp[i]+=1
                        ans+=dp[j]
            return ans
        return count(rating) + count(rating[::-1])