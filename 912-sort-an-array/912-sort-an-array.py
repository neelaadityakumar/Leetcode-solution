class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        maxdigit = float('-inf')
        
        # find maxdigit
        for ele in nums:
            maxdigit = max(maxdigit, len(str(ele)))
            
        
        # 'B' corresponds to each digit from -9 to 9
        # Run the loop for max number of digits in the list
        for digit in range(maxdigit):
            B = [[] for i in range(10+9)]
            
            for ele in nums:
                # Get the digit at the current position
                # and append it to the corresponding index in 'B'
                if ele < 0:
                    num = 9 - abs(ele)// (10 ** digit) % 10
                    B[num].append(ele)
                else:
                    num = ele// (10 ** digit) % 10
                    B[num+9].append(ele)
            
            # reduce 'B' to a single list
            nums = reduce(lambda x,y: x+y, B)
            
        return nums