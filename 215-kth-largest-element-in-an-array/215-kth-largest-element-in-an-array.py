class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSelect(nums, 0, len(nums)-1, k)

    def quickSelect(self, nums, start, n, k): # quick select
        pos = self.partition(nums, start, n)
        if pos == k-1:
            return nums[pos]
        elif pos >= k:
            return self.quickSelect(nums, start, pos - 1, k)
        return self.quickSelect(nums, pos + 1, n, k)

    def partition(self, nums, left, right):
        pivot = nums[right] # pick the last one as pivot
        i = left
        for j in xrange(left, right): # left to right -1
            if nums[j] > pivot: # the larger elements are in left side
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[right], nums[i] = nums[i], nums[right] # swap the i and the last element
        return i