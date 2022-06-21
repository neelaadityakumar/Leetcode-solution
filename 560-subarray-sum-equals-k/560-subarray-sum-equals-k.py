class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        preSum = 0
        counter = defaultdict(int)

        for num in nums:
            preSum += num
            
            # instead of initiate counter[0] with 1
            if preSum == k:
                res += 1

            if preSum - k in counter:
	            res += counter[preSum - k]

            counter[preSum] += 1

        return res