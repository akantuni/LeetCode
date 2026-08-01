class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = set()

        l = 0
        mx = 0
        for r, c in enumerate(s):
            while c in memo:
                memo.remove(s[l])
                l += 1
            memo.add(c)
            mx = max(mx, len(memo))

        return mx
