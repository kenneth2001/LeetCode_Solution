class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        minutes = 0
        fresh = 0
        rotten = []

        # find all rotten oranges and count fresh oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        while rotten and fresh:
            new_rotten = []
            for i, j in rotten:
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        new_rotten.append((x, y))
            rotten = new_rotten
            minutes += 1

        if fresh:
            return -1
        
        return minutes
