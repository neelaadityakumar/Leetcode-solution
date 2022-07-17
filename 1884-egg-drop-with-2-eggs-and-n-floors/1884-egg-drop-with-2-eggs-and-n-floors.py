class Solution:
    def twoEggDrop(self, n: int) -> int:
        self.dp={}
        def dropEgg(floor,egg):
            if (floor,egg) not in self.dp:
                if floor<=1:
                    self.dp[(floor,egg)]=floor
                elif egg==1:
                    self.dp[(floor,egg)]=floor
                
                else:
                    res=sys.maxsize
                    for f in range(1,floor+1):
                        res=min(res,1+max(dropEgg(f-1,egg-1),dropEgg(floor-f,egg)))
                    self.dp[(floor,egg)]=res
                
            return self.dp[(floor,egg)]
        return dropEgg(n,2)
        