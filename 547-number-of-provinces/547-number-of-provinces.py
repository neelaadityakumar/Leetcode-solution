class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        count = 0
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                count+=self.dfs(isConnected, i, visited)
        return count

    def dfs(self, isConnected, i, visited):
        '''helper function for recursion
        '''
        if visited[i]==True:
            return 0
        visited[i] = True
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and (not visited[j]):
                self.dfs(isConnected, j, visited)
        return 1
