class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        mx = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                mx = max(mx, (i - idx) * height)
                start = idx
            stack.append((start, h))

        for i, h in stack:
            mx = max(mx, (len(heights) - i) * h)

        return mx
