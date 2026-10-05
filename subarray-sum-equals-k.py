class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = {0: 1}
        c = 0
        ans = 0
        for i, n in enumerate(nums):
            c += n
            ans += memo.get(c - k, 0)
            memo[c] = memo.get(c, 0) + 1

        return ans
