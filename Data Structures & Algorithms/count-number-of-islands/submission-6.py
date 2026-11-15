class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        islands = 0

        def bfs(r, c):
            q = deque()
            q.append([r,c])
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    new_row = r + dr
                    new_col = c + dc

                    if new_row in range(ROWS) and new_col in range(COLS) and (new_row, new_col) not in visited and grid[new_row][new_col] == "1":
                        visited.add((new_row, new_col))
                        q.append([new_row, new_col])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    islands += 1
                    visited.add((r, c))
                    bfs(r,c)

        return islands

        


