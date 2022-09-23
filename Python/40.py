class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(star_idx, target, path):
            if target < 0:
                return
            if target == 0:
                ans.append(path.copy())
                return
            
            for i in range(star_idx, len(candidates)):
                if i > star_idx and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i + 1, target - candidates[i], path)
                path.pop()

        candidates.sort()
        dfs(0, target, [])
        return ans
