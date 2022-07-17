class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        for i in range(len(s)): # for every substring starting with s[i], we search all possible starting index in t
            for j in range(len(t)):
                start_s, start_t = i, j
                count = 0
                while(start_s<len(s) and start_t<len(t)):
                    if s[start_s]!=t[start_t]: # if current letter is different, add one to the count
                        count+=1
                    if count==1: # only if count == 1 we add 1 to the ans
                        ans+=1
                    if count>=2: # early stop for two or more diffferent letters
                        break
                    start_s+=1
                    start_t+=1
        return ans