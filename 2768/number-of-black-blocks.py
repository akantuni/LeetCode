class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        total = max(0, m - 1) * max(0, n - 1)

        memo = {}

        for cell in coordinates:
            directions = ((0, 0), (0, -1), (-1, 0), (-1, -1))
            for d in directions:
                r, c = cell
                r = r + d[0]
                c = c + d[1]

                if r < 0 or r >= m - 1 or c < 0 or c >= n - 1:
                    continue
        
                memo[(r, c)] = memo.get((r, c), 0) + 1

        res = [total] + [0] * 4

        for count in memo.values():
            res[0] -= 1
            res[count] += 1

        return res
