class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        memo = {}

        stack = []
        for i in reversed(range(len(nums2))):
            while stack and stack[-1] < nums2[i]:
                stack.pop()

            memo[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        
        return [memo[num] for num in nums1]
