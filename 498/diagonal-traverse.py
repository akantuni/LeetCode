class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])

        res = []
        d = ((-1, 1), (1, -1))
        r = c = i = 0
        while len(res) < m * n:
            res.append(mat[r][c])
            dr, dc = d[i]
            nr, nc = r + dr, c + dc
            if nc >= n:
                r += 1
            elif nr >= m:
                c += 1
            elif nr < 0:
                c += 1
            elif nc < 0:
                r += 1
            else:    
                r, c = nr, nc
                continue
                
            i ^= 1

        return res
