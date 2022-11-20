class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        position={}
        for i in range(len(nums)):
            if not target-nums[i] in position:
                position[nums[i]]=i
            else:
                return [i,position[target-nums[i]]]
