class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        r = [] # Hold the resulting relative sort array
        m = {} # Used for counting elements of arr2 that appear in arr1
        diff = [] # Use for tracking elements that don't appear in arr2 but appear in arr1
        
		# Initialize counts
        for num in arr2:
            if num not in m:
                m[num] = 0
        
        for num in arr1:
            if num in m:
                m[num] += 1 # Increment count of elements seen
            else:
                diff.append(num) # Add element to difference list (e.g. nums in arr1 not in arr2)
        
        diff.sort() # Sort the difference
        
        for num in arr2:
            r.extend([num] * m[num]) # Add the number of elements seen to  the result set
        
        r.extend(diff) # Add the rest of the sorted elements
        
        return r
