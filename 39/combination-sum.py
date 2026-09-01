class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(start, target, comb):
            if target == 0:
                res.append(comb)
                return
            
            if target < 0:
                return

            for i in range(start, len(candidates)):
                helper(i, target - candidates[i], comb + [candidates[i]])

        res = []
        helper(0, target, [])
        return res
