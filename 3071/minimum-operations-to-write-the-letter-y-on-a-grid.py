class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)

        rest = [0] * 3
        y = [0] * 3

        for r in range(n):
            for c in range(n):
                e = grid[r][c]
                if (r <= n // 2 and (r == c or r + c == n - 1)) or (
                    r > n // 2 and c == n // 2
                ):
                    y[e] += 1
                else:
                    rest[e] += 1

        m = float("inf")

        for i in range(3):
            m = min(
                m, rest[i] + sum(y) - y[i] + min(rest[(i + 1) % 3], rest[(i + 2) % 3])
            )

        return m
