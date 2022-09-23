class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        if target < 0:
            return []
        res = []
        for i in range(len(candidates)):
            # for every candidate, we can minus it from target
            for j in self.combinationSum(candidates[i:], target - candidates[i]):
                res.append([candidates[i]] + j)
        return res