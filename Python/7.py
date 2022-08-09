class Solution:
    def reverse(self, x: int) -> int:
        sol = int(str(abs(x))[::-1]) * (-1 if x < 0 else 1)
        return sol if -2**31 <= sol <= 2**31 - 1 else 0
