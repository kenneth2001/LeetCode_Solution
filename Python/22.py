class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        ans = []

        def search(i, j, path):
            if i == n and j == n:
                ans.append(''.join(path))
                return
            if i < n:
                path.append('(')
                search(i + 1, j, path)
                path.pop()
            if j < i:
                path.append(')')
                search(i, j + 1, path)
                path.pop()
        
        search(0, 0, [])
        return ans
