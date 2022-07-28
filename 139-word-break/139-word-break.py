class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def memoize(target, wordDict):
            if target == "":
                return True
            if target in memo:
                return memo[target]
            
            for word in wordDict:
                if target[:len(word)] == word and memoize(target[len(word):], wordDict):
                    memo[target] = True
                    return memo[target]
            memo[target] = False
            return memo[target]
        
        return memoize(s, wordDict)