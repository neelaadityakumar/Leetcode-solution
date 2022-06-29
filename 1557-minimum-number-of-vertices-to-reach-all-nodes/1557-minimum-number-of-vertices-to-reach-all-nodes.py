class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        
        incoming_degrees = {i: 0 for i in range(n)}
        
        for x, y in edges:
            incoming_degrees[y] += 1
            
        result = [k for k, v in incoming_degrees.items() if v == 0]
        return result