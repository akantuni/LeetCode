class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        l2 = None
        r2 = None
        if target > nums[-1]:
            l2 = 0
            r2 = l
        else:
            l2 = l
            r2 = len(nums) - 1

        while l2 < r2:
            mid = (l2 + r2) // 2
            if nums[mid] < target:
                l2 = mid + 1
            else:
                r2 = mid

        if nums[l2] == target:
            return l2
        return -1
