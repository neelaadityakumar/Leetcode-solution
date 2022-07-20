class Solution:
    def greatestLetter(self, s: str) -> str:
        sets=set(s)
        for char in range(ord("z"),ord("a")-1,-1):
            lower,upper=chr(char),chr(char).upper()
            if lower in sets and upper in sets:
                return upper
        return ""