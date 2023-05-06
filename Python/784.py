class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = s.lower()
        n, ans = len(s), []
        def dfs(i, res=''):
            if i < n:
                dfs(i+1, res + s[i])
                if s[i].islower(): 
                    dfs(i+1, res + s[i].upper())
            else:
                ans.append(res)
                
        dfs(0)
        return ans
