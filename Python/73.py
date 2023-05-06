class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        flag1 = False
        flag2 = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0 or j == 0:
                        if i == 0 and j == 0:
                            flag1 = True
                            flag2 = True
                        elif i == 0:
                            flag1 = True
                        else:
                            flag2 = True
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

        # row by row
        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i] = [0]*n

        # col by col
        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(m):
                    matrix[j][i] = 0
        
        if flag1:
            matrix[0] = [0] * n
        if flag2:
            for i in range(m):
                matrix[i][0] = 0
                