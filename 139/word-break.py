class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len()
        
        memo = {a}

        def find(start, end):
            if start == n:
                return True
            if end == n:
                return False

            if (start, end) in memo:
                return memo[(start, end)]

            if s[start:end + 1] not in wordDict:
                res = find(start, end + 1)
            else:
                res = find(end + 1, end + 1) or find(start, end + 1)

            memo[(start, end)] = res
            return res

        return find(0, 0)
