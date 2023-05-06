class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if not nums:
            return 0
        elif n == 1:
            return nums[0]
        
        dp = [nums[0], max(nums[0], nums[1])] + [0] * (n - 2)

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
