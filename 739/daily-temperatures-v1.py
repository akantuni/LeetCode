class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i in reversed(range(n)):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]] <= temp:
                stack.pop()

            if stack:
                res[i] = stack[-1] - i

            stack.append(i)

        return res
