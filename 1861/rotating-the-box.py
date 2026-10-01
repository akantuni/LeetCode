class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        for r in range(m):
            empty = n - 1
            for c in reversed(range(n)):
                e = boxGrid[r][c]
                if e == "*":
                    empty = c - 1
                elif e == "#":
                    boxGrid[r][c] = "."
                    boxGrid[r][empty] = "#"
                    empty -= 1

        boxGrid = [list(r) for r in zip(*boxGrid[::-1])]

        return boxGrid
