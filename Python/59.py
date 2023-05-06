class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for i in range(n)]

        i = 0
        j = 0
        count = 1

        target = n*n
        while count <= target:
            while j < n and ans[i][j] == 0:
                ans[i][j] = count
                count += 1
                j += 1
            j -= 1
            i += 1
            
            while i < n and ans[i][j] == 0:
                ans[i][j] = count
                count += 1
                i += 1
            i -= 1
            j -= 1
            
            while j >= 0 and ans[i][j] == 0:
                ans[i][j] = count
                count += 1
                j -= 1
            j += 1
            i -= 1
            
            while i >= 0 and ans[i][j] == 0:
                ans[i][j] = count
                count += 1
                i -= 1
            i += 1
            j += 1

        return ans
    