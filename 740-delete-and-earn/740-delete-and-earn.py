class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = defaultdict(int)
        for num in nums:
            count[num] += num

        nums = sorted(count.keys())

        # The actual DP part
        take_two_before = 0
        take_one_before = count[nums[0]]

        for i in range(1, len(count)):
            if nums[i] == nums[i - 1] + 1:
                take_two_before, take_one_before = take_one_before, max(take_one_before, take_two_before + count[nums[i]])
            else:
                take_two_before, take_one_before = take_one_before, take_one_before + count[nums[i]]
        return take_one_before