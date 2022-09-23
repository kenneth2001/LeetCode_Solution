from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        n = len(matrix)
        self.printMatrix(matrix)
        print('-- -- -- --')

        for i in range(1, n):
            for j in range(i):
                print(f'{i}, {j} -> {j}, {i}')
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                self.printMatrix(matrix)

    def printMatrix(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            print(matrix[i])
        print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Solution().rotate(matrix)
print(matrix)