class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        numFresh = 0
        q = deque()
        time = 0
        directions = [[0,1], [1,0], [-1,0], [0,-1]]


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    numFresh += 1
        
        while q and numFresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == '1':
                        numFresh -= 1
                        grid[row][col] = 2
                        q.append((row, col))
            time += 1
        
        return time if numFresh == 0 else -1

