class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[1]*n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i-1][j] + mat[i][j-1]
        return mat[-1][-1]   
    