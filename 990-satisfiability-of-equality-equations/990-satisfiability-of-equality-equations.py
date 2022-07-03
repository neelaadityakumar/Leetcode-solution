class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = {chr(num):chr(num) for num in range(ord("a"), ord("z")+1)}
        
        def find(val):
            if parents[val] == val:
                return val
            parents[val] = find(parents[val])
            return parents[val]
        
        for x,sign,_,y in equations:
            if sign == "=":
                parent_x, parent_y = find(x), find(y)
                parents[parent_x] = parent_y
        
        for x,sign,_,y in equations:
            if sign == "!" and find(x) == find(y):
                return False
        
        return True