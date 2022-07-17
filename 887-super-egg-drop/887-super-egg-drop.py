
class Solution(object):
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for floor in range(1, n + 1):
            for egg in range(1, k + 1):
                dp[floor][egg] = 1 + dp[floor - 1][egg - 1] + dp[floor - 1][egg]
                if dp[floor][egg] >= n: return floor
        return -1
#     Explanation

# Drop eggs is a very classical problem.
# Some people may come up with idea O(KN^2)
# where dp[K][N] = 1 + max(dp[K - 1][i - 1], dp[K][N - i]) for i in 1...N.
# However this idea is very brute force, for the reason that you check all possiblity.

# So I consider this problem in a different way:
# dp[M][K]means that, given K eggs and M moves,
# what is the maximum number of floor that we can check.

# The dp equation is:
# dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1,
# which means we take 1 move to a floor,
# if egg breaks, then we can check dp[m - 1][k - 1] floors.
# if egg doesn't breaks, then we can check dp[m - 1][k] floors.

# dp[m][k] is the number of combinations and it increase exponentially to N