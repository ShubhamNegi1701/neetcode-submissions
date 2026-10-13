from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            
            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    row = dr + r
                    col = dc + c

                    if (row, col) not in visited and row in range(ROWS) and col in range(COLS) and grid[row][col] == "1":
                        visited.add((row, col))
                        q.append((row, col))


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        return islands