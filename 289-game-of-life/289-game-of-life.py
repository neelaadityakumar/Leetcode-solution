class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        switch = []
        travel = [[1,0],[0,1],[1,1],[1,-1],[-1,1],[0,-1],[-1,0],[-1,-1]]
        for i in range(rows):
            for j in range(cols):
                count = 0
                for dx, dy in travel:
                    if 0 <= i+dx < rows and 0<= j+dy < cols:
                        if board[i+dx][j+dy] == 1:
                            count += 1
                            
                if board[i][j] == 0 and count == 3:
                    switch.append((i,j))
                if board[i][j] == 1:
                    if count < 2:
                        switch.append((i,j))
                    if count > 3:
                        switch.append((i,j))
                            
        for x,y in switch:
            if board[x][y] == 0:
                board[x][y] = 1
            else:
                board[x][y] = 0