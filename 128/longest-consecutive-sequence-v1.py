class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        memo = {}
        for i in nums:
            memo.update({i: memo.get(i, 0) + 1})

        longest = 1

        visited = set()

        for num in memo.keys():
            if num in visited:
                continue
            i = 1
            while memo.get(num + i) is not None:
                i += 1
                visited.add(num + i)
            j = 1
            while memo.get(num - j) is not None:
                j += 1
                visited.add(num - j)
            longest = max(longest, i + j - 1)
        return longest

