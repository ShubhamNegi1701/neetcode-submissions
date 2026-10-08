class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        while q and fresh > 0:

            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if r + dr in range(ROWS) and c + dc in range(COLS) and grid[dr + r][dc + c] == 1:
                        fresh -= 1
                        grid[dr + r][dc + c] = 2
                        q.append([dr + r, dc + c])
            time += 1
        
        return time if fresh == 0 else -1