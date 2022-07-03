class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        seen = set()
        number_of_servers = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                potential_servers = 0 
                # if grid[row][col] == 1 and (row, col) not in seen:
                #     seen.add((row, col))
                potential_servers = self.four_directional_search(grid, row, col, seen)
                if potential_servers > 1:
                    number_of_servers += potential_servers 
        return number_of_servers
		
    def four_directional_search(self, grid, row, col, seen):
        if (row, col) not in seen and grid[row][col] == 1:
            seen.add((row, col))
            count = 1
            for new_row in range(len(grid)):
                count += self.four_directional_search(grid, new_row, col, seen)
            for new_col in range(len(grid[0])):
                count += self.four_directional_search(grid, row, new_col, seen)  
            return count
        return 0