class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, column = len(grid), len(grid[0])
        number_of_islands = 0

        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=column or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            dfs(r,c+1)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r-1,c)

        for r in range(row):
            for c in range(column):
                if grid[r][c] == '1':
                    number_of_islands+=1
                    dfs(r,c)

        return number_of_islands