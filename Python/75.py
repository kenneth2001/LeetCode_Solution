class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0
        r = len(nums) - 1

        idx = 0
        while idx <= r:
            if nums[idx] == 0:
                nums[idx], nums[l] = nums[l], nums[idx]
                idx += 1
                l += 1
            elif nums[idx] == 1:
                idx += 1
            else:
                nums[idx], nums[r] = nums[r], nums[idx]
                r -= 1
                