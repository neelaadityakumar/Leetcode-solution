class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(output,tiles):
            count = 0
            
            for i in range(len(tiles)):
                if i == 0 or tiles[i-1] != tiles[i]:
                    output.append(tiles[i])
                    count += 1
                    count += backtrack(output, tiles[:i] + tiles[i+1:])
                    output.pop()

            return count
        
        return backtrack([],sorted(tiles))