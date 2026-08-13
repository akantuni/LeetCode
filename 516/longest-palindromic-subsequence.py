class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        s_rev = s[::-1]

        DP = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                if i == 0 or j == 0:
                    DP[i][j] = 0
        
        def memoLCS(i, j):
            if DP[i][j] == -1:    
                if i < 0 or j < 0:
                    DP[i][j] = 0
                elif s[i - 1] == s_rev[j - 1]:
                    DP[i][j] = 1 + memoLCS(i - 1, j - 1)
                else:
                    skipX = memoLCS(i - 1, j)
                    skipY = memoLCS(i, j - 1)
                    if skipX >= skipY:
                        DP[i][j] = skipX
                    else:
                        DP[i][j] = skipY
            return DP[i][j]

        return memoLCS(n, n)



        
