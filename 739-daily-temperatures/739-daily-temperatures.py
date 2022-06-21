class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n=len(t)
        ans=[0]*n
        st=[]
        for i in range(n):
            while st and t[st[-1]]<t[i]:
                curr=st.pop()
                ans[curr]=i-curr
            st.append(i)
            
        return ans