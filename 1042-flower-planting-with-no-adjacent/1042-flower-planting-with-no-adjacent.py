class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for x, y in paths:
            g[x].append(y)
            g[y].append(x)
        plantdict = {i: 0 for i in range(1, N + 1)}
        for garden in g: 
            pick = set(range(1,5))
            for each in g[garden]:
                if plantdict[each] != 0 and plantdict[each] in pick:
                    pick.remove(plantdict[each])
            plantdict[garden] = pick.pop()
        return [plantdict[x] if plantdict[x] != 0 else 1 for x in range(1, N+1)]