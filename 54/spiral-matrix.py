class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        d = ((0, 1), (1, 0), (0, -1), (-1, 0))

        r = c = i = 0
        res = []
        while len(res) < m * n:
            res.append(matrix[r][c])
            matrix[r][c] = None
            
            dr, dc = d[i]
            nr, nc = r + dr, c + dc

            if not (0 <= nr < m and 0 <= nc < n) or matrix[nr][nc] is None:
                i = (i + 1) % 4
                dr, dc = d[i]
                nr, nc = r + dr, c + dc
            
            r, c = nr, nc
        
        return res
