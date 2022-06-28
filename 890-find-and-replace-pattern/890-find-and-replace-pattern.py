class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans=[]
        def find(word):
            dict={}
            for i in range(len(word)):
                if word[i] in dict.keys():
                    dict[word[i]].append(i)
                else:
                    dict[word[i]]=[i]
            return dict
        dict_1=find(pattern)        
        for j in words:
            dict_2=find(j)
            if list(dict_1.values()) == list(dict_2.values()):
                ans.append(j)
        return ans