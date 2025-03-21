class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  <=i:
                    combs[i] += combs[i - num]
        return combs[target]
