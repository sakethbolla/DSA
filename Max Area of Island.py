class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])
        max_island = 0

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= column or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0  # mark visited
            area = 1

            area += dfs(r, c + 1)  # right
            area += dfs(r + 1, c)  # down
            area += dfs(r, c - 1)  # left
            area += dfs(r - 1, c)  # up

            return area
        
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1:
                    max_island = max(max_island, dfs(r, c))

        return max_island