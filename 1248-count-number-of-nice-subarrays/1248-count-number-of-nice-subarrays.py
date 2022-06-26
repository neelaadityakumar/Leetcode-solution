class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # This is just converting the even number to 0 and odd numbers to 1 in the array
        for i in range(len(nums)):

            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        # Then doing exactly the same thing as subarray sum equal k problem

        currsum = 0
        subarray = 0
        hashmap = {}

        for num in nums:
            currsum += num

            if currsum == k:
                subarray += 1

            if currsum - k in hashmap:
                subarray += hashmap[currsum - k]

            if currsum in hashmap:
                hashmap[currsum] += 1

            else:
                hashmap[currsum] = 1

        return subarray