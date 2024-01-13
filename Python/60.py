class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        res = []
        k -= 1
        while n > 0:
            n -= 1
            idx, k = divmod(k, math.factorial(n))
            res.append(nums.pop(idx))
        return ''.join(res)