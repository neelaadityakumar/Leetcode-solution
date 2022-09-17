class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = []
        
        # convert input number into digits array
        while(n != 0):
            r = n%10
            digits.append(r)
            n = n//10
        
        # as digits were taken out in reverse order
        # hence, reverse the list to maintain original order
        digits = digits[::-1]
        
        # find the peak element i such that digits[i] <= digits[i-1]
        i = len(digits)-1
        while(i>0 and digits[i] <= digits[i-1]):
            i -= 1
        
        # if digits array is sorted into ascending order
        # hence, next greater not possible
        if i == 0:
            return -1
        
        # else, find the smallest element greater than i-1
        j = i
        while(j+1 < len(digits) and digits[j+1] > digits[i-1]):
            j += 1
        
        # swap the i-1 element with j i.e. next greater
        digits[i-1], digits[j] = digits[j], digits[i-1]
        
        # reverse the remaining part of the array
        digits[i:] = digits[i:][::-1]
        
        # finally formulate the resultant number
        result = 0
        for i in range(len(digits)):
            result = result*10+digits[i]
        
        return -1 if result > (2**31)-1 else result