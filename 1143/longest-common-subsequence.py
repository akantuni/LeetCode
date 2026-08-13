class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        DP = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    DP[i][j] = 0
        
        def memoLCS(i, j):
            if DP[i][j] == -1:    
                if i < 0 or j < 0:
                    DP[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    DP[i][j] = 1 + memoLCS(i - 1, j - 1)
                else:
                    skipX = memoLCS(i - 1, j)
                    skipY = memoLCS(i, j - 1)
                    if skipX >= skipY:
                        DP[i][j] = skipX
                    else:
                        DP[i][j] = skipY
            return DP[i][j]

        return memoLCS(m, n)
