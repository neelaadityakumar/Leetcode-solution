class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        windowStart = 0
        maxLengthcount = 0
        hash_map = dict()
        for windowEnd in range(len(s)):
            curr_char = s[windowEnd]
            hash_map[curr_char] = hash_map.get(curr_char,0) + 1
            while(len(hash_map)==3):
                left_char = s[windowStart]
                hash_map[left_char] -= 1
                if(hash_map[left_char]==0):
                    del hash_map[left_char]
                maxLengthcount += len(s)-windowEnd
                windowStart += 1
        return maxLengthcount