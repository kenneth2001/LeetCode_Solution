class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = 0

        for i in range(n):
            if reach < i:
                return False
            reach = max(i+nums[i], reach)
            if reach >= n - 1:
                return True
        return False
    