class Solution:
    def uniquePaths(self, r: int, c: int) -> int:
        row = [1] * c

        for i in range(r - 1):
            newRow = [1] * c
            for j in range(c - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

