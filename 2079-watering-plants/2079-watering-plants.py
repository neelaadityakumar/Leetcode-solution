class Solution:
    def wateringPlants(self, plants: List[int], cap: int) -> int:
        ans=0
        c=cap
        pos=-1
        for i in range(len(plants)):
            if c>=plants[i]:
                ans+=1
                c-=plants[i]
                pos=i
            else:
                ans+=2*i+1
                c=cap-plants[i]
        return ans
        