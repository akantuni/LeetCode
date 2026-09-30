class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        nm = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
            nm.append(row)
        return nm
