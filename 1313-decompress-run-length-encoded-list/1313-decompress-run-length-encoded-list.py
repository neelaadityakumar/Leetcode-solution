class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []

        i = 0
        while i < len(nums):
            freq, val = nums[i], nums[i+1]
            
            result.extend([val] * freq)
            i += 2
            
        return result
