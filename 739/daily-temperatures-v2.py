class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res
