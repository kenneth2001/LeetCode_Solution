class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            n = n / 2
            if not n.is_integer():
                return False
        return n == 1
