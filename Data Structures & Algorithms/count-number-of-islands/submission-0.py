class Solution:
    


    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, visited, r, c):
            if (r > len(grid) - 1 or c > len(grid[0]) - 1 or r < 0 or c < 0 or visited[r][c] == True or grid[r][c] == '0'):
                return
            visited[r][c] = True
            dfs(grid, visited, r + 1, c)
            dfs(grid, visited, r - 1, c)
            dfs(grid, visited, r, c + 1)
            dfs(grid, visited, r, c - 1)

        # create a visited list, nothing is visited
        rows = len(grid)
        cols = len(grid[0])
        counter = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        # iterate through grid, if you find a '1', thats not visited, then increment counter, apply dfs
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '0':
                    continue
                if grid[r][c] == '1':
                    if not visited[r][c]:
                        counter += 1
                        dfs(grid, visited, r, c)

        # return counter
        return counter