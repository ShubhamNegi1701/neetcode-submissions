class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        visited = set()

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r not in range(ROWS) or c not in range(COLS) or word[i] != board[r][c] or (r, c) in visited:
                return False

            visited.add((r, c))

            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc

                if dfs(new_row, new_col, i+1):
                    return True
            
            visited.remove((r, c))

            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False