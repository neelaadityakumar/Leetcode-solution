class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def dfs(i,target):
            if (i,target) in dp:
                return dp[(i,target)]
            if i >= n:
                if target == 0:
                    return 1
                else:
                    return 0
            # sum of 2 ways 
            # 1st way => consider i th index as + nums[i] => ask dfs() to move to next index and reduce the target
            # 2nd way => consider i th index as - nums[i] => ask dfs() to move to next index and increase the target
            dp[(i,target)] = dfs(i+1,target - nums[i]) + dfs(i+1,target + nums[i]) 
            return dp[(i,target)]
        return dfs(0,target)