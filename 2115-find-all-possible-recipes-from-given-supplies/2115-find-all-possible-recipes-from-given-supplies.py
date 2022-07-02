class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        q = deque()
        result = []
        
        # everything in supplies has an indegree of 0
        #reciepe is the end node , supply is start
        for s in supplies:
            indegree[s] = 0
            q.append(s)
            
        for i, r in enumerate(recipes):
            for ing in ingredients[i]:
                graph[ing].append(r)
                indegree[r] += 1
                
        while q:
            node = q.pop()
            if node in recipes:
                result.append(node)
            for n in graph[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
                    
        return result