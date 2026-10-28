class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        visited_pacific = set()
        visited_atlantic = set()


        pacific_queue = deque()
        atlantic_queue = deque()


        for c in range(COLS):
            pacific_queue.append((0, c))
            visited_pacific.add((0, c))

            atlantic_queue.append((ROWS - 1, c))
            visited_atlantic.add((ROWS - 1, c))


        for r in range(ROWS):
            pacific_queue.append((r, 0))
            visited_pacific.add((r, 0))

            atlantic_queue.append((r, COLS - 1))
            visited_atlantic.add((r, COLS - 1))

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_row = dr + r 
                    new_col = dc + c
                    if new_row in range(ROWS) and new_col in range(COLS) and (new_row, new_col) not in visited and heights[new_row][new_col] >= heights[r][c]:
                        visited.add((new_row,new_col))
                        queue.append((new_row,new_col))

        bfs(pacific_queue, visited_pacific)
        bfs(atlantic_queue, visited_atlantic)

        result = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited_pacific and (r, c) in visited_atlantic:
                    result.append([r, c])

        return result


        






