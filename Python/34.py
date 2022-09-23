import bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target) - 1
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        return [l, r]
