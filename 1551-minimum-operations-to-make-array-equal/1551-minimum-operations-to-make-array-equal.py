class Solution:
    def minOperations(self, n: int) -> int:
        ans=0
        for i in range(n//2):
            val=(2*i)+1
            ans+=abs(n-val)
        return ans
            