class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # dp = {}
        # def dfs(i,target):
        #     if (i,target) in dp:
        #         return dp[(i,target)]
        #     if i >= n:
        #         if target == 0:
        #             return 1
        #         else:
        #             return 0
        #     # sum of 2 ways 
        #     # 1st way => consider i th index as + nums[i] => ask dfs() to move to next index and reduce the target
        #     # 2nd way => consider i th index as - nums[i] => ask dfs() to move to next index and increase the target
        #     dp[(i,target)] = dfs(i+1,target - nums[i]) + dfs(i+1,target + nums[i]) 
        #     return dp[(i,target)]
        # return dfs(0,target)
        # helper
        def f(i, trgtSum):

            if i == len(nums) and trgtSum == 0: # --- NOTE [1]
                return 1

            # if trgtSum == 0: #  does not work when a 0 is trailing +ve integers
            #     return 1

            if i == len(nums):
                return 0

            if trgtSum < 0:
                return 0

            if (i, trgtSum) in memo:
                return memo[(i, trgtSum)]

            result = f(i+1, trgtSum-nums[i]) + f(i+1, trgtSum)
            memo[(i,trgtSum)] = result
            return result

        # main
        nums.sort()
        memo = {}
        if (sum(nums) + target) % 2 != 0:
            return 0
        trgtSum = (sum(nums) + target) // 2
        return f(0, trgtSum)
