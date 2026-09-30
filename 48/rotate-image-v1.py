class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for r in range(n // 2):
            for c in range(r, n - r - 1):
                nr, nc = c, n - 1 - r
                temp = matrix[r][c]
                for _ in range(4):
                    matrix[nr][nc], temp = temp, matrix[nr][nc]
                    nr, nc = nc, n - 1 - nr
