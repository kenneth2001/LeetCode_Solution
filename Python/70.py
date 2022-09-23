class Solution:
    def climbStairs(self, n: int) -> int:
        t = [1, 1]
        for i in range(n-1):
            t[0], t[1] = t[1], t[0]+t[1]
        return t[1]
