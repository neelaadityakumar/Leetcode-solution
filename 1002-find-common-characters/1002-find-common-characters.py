class Solution(object):
    def commonChars(self, A):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        cnt = collections.Counter(A[0])
        for s in A:
            cnt2 = collections.Counter(s)
            for k in cnt.keys():
                cnt[k] = min(cnt[k], cnt2[k])
        return cnt.elements()