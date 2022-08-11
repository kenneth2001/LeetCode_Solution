class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        s_len = len(s)
        p_len = len(p)

        def search(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            elif i >= s_len and j >= p_len:
                return True
            elif j >= p_len:
                return False
            
            match = i < s_len and (s[i] == p[j] or p[j] == '.')
            if j + 1 < p_len and p[j + 1] == '*':
                cache[(i, j)] = search(i, j + 2) or (match and search(i + 1, j))
                return cache[(i, j)]
            elif match:
                return search(i + 1, j + 1)
            return False
        return search(0, 0)
