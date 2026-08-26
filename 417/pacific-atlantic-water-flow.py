class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        memo = {}
        m, n = len(heights), len(heights[0])

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                nc, nr = r + dx, c + dy
                if 0 <= nc < m and 0 <= nr < n and (nc, nr) not in visited and heights[nc][nr] >= heights[r][c]:
                    dfs(nc, nr, visited)
                

        atlantic, pacific = set(), set()
        for r in range(m):
            dfs(r, 0, pacific)
        for c in range(n):
            dfs(0, c, pacific)
        for r in range(m):
            dfs(r, n - 1, atlantic)
        for c in range(n):
            dfs(m - 1, c, atlantic)
        return list(atlantic & pacific)
