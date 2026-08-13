class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        DP = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        def lev(i, j):
            if DP[i][j] == -1:
                if i == 0:
                    DP[i][j] = j
                elif j == 0:
                    DP[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    DP[i][j] = lev(i - 1, j - 1)
                else:
                    insChar = lev(i, j - 1)
                    delChar = lev(i - 1, j)
                    repChar = lev(i - 1, j - 1)
                    tot = 1 + min(insChar, delChar, repChar)
                    DP[i][j] = tot
            return DP[i][j]
        
        return lev(m, n)
                    
