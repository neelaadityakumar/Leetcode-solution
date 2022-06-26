class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0  # left pointer
        end = 0  # right pointer
        count_ones = 0  # total count of ones
        max_len = 0

        while end <= len(nums) - 1:  # python offset -1 for index
            if nums[end] == 1:
                count_ones += 1

            while end-start-count_ones > 0:
                if nums[start] == 1:
                    count_ones -= 1
                start += 1

            max_len = max(max_len, end - start)
            end += 1
        return max_len
