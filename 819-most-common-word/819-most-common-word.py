class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for c in "!?',;.": 
            paragraph = paragraph.replace(c, " ")
        d, res, count = {},"",0
        for word in paragraph.lower().split():
            if word not in banned:
                if word not in d:
                    d[word] = 0
                d[word] += 1
                if d[word] > count:
                    count = d[word]
                    res = word
        return res