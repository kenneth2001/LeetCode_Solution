class Solution:
    def reverseBits(self, n: int) -> int:
        b = '{:032b}'.format(n)[::-1]
        return int(b, 2)
