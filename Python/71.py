class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        for part in path.split('/'):
            if part in ('', '.'):
                continue
            
            if part == '..': 
                if ans:
                    ans.pop()
            else:
                ans.append(part)
        return '/' + '/'.join(ans)
