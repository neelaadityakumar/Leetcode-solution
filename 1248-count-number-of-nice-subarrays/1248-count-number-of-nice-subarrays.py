class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # This is just converting the even number to 0 and odd numbers to 1 in the array
        for i in range(len(nums)):
            nums[i] = nums[i]&1
        # Then doing exactly the same thing as subarray sum equal k problem

        currsum = 0
        subarray = 0
        hashmap = {0:1}

        for num in nums:
            currsum += num
            if currsum - k in hashmap:
                subarray += hashmap[currsum - k]
            hashmap[currsum]=hashmap.get(currsum,0)+1

        return subarray