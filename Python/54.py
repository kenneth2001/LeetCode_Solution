class Solution:
    def spiralOrder(self, matrix):
        ans = []

        while matrix:
            ans += matrix.pop(0)
            matrix = (list(zip(*matrix)))[::-1]
        return ans
    