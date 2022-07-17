
class Solution(object):
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for floor in range(1, n + 1):
            for egg in range(1, k + 1):
                dp[floor][egg] = 1 + dp[floor - 1][egg - 1] + dp[floor - 1][egg]
                if dp[floor][egg] >= n: return floor
        return -1