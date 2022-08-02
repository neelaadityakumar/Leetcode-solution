class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if i == j:  # next index if the index and value match
                i += 1
            else:
                if nums[i] != nums[j]:  # swap
                    nums[i], nums[j] = nums[j], nums[i]
                else:  # this is the duplicate
                    return nums[j]