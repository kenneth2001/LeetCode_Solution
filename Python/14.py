class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = min([len(s) for s in strs])
        sol = ''
        for i in range(minLength):
            if all([s[i] == strs[0][i] for s in strs]):
                sol = sol + strs[0][i]
            else:
                break
        return sol
