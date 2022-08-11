class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = -inf
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l = i+1
            r = len(nums)-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(ans - target):
                    ans = sum
                if sum < target:
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                else:
                    r -= 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
        return ans
        