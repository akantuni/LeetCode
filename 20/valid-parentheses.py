class Solution:
    def isValid(self, s: str) -> bool:
        memo = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for c in s:
            if stack and stack[-1] == memo.get(c):
                stack.pop()
            else:
                stack.append(c)
        
        return not stack
