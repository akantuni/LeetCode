import math
from itertools import groupby

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        mx = mn = 1

        for num in nums:
            vals = (num, mn * num, mx * num)
            mx, mn = max(vals), min(vals)
            res = max(res, mx)

        return res
