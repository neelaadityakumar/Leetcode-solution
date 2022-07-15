class Solution:
    def countVowelStrings(self, n: int) -> int:
        def count(n,vow):
            if vow == 0: 
                mem[n][vow] =  0
                return mem[n][vow]
            if n == 0: 
                mem[n][vow] = 1
                return mem[n][vow]
            if mem[n][vow]!=-1:
                return mem[n][vow]
            mem[n][vow] = count(n,vow-1)+count(n-1,vow)
            return mem[n][vow]
        mem = [[-1]*6 for i in range(n+1)]
        return count(n,5)
#     for 3: we can add a to all the strings in previous case so 15 will already be there.value will be (n = 2, w = 5) = 15
# lets look at the remaining cases.
# now we need to find values with 4 vowels {e,i,o,u} and need to have 3 lettered strings. i.e (n = 3, vow = 4)

# we can say f(n = 3, vow = 5) = f(n = 2, vow = 5) # for a case
# 					+ f(n = 3, vow = 4) #after removal of a left with vow = 4

# so we are getting a recursion: 
#  recur(n,w) = recur(n-1, w) //here in the previous case, (2,5)
# 					 + recur(n,w-1) // after using a we are left with {e,i,o,u} so w-1 for that
