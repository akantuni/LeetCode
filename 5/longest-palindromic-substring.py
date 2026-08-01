from collections import deque

class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx = 1
        idx = ()
        for i, c in enumerate(s):
            l = r = i
            while True:
                if l < 0 or r >= len(s) or s[l] != s[r]:
                    if r - l + 1 > mx:
                        mx = r - l + 1
                        idx = (l + 1, r - 1)
                    break
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while True:
                if l < 0 or r >= len(s) or s[l] != s[r]:
                    if r - l + 1 > mx:
                        mx = r - l + 1
                        idx = (l + 1, r - 1)
                    break
                l -= 1
                r += 1

        return s[idx[0]: idx[1] + 1]
            
