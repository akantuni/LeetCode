class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = {}
        for num in nums:
            memo[num] = memo.get(num, 0) + 1
        return [k for k, v in heapq.nlargest(k, memo.items(), key=lambda item: item[1])]

        
