class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        memo = set(nums)
        longest = 1

        for num in nums:
            if num not in memo:
                continue

            memo.remove(num)

            i = 1
            while num + i in memo:
                memo.remove(num + i)
                i += 1

            j = 1
            while num - j in memo:
                memo.remove(num - j)
                j += 1

            longest = max(longest, i + j - 1)

        return longest
