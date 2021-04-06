class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while (nums):
            val = target-nums[i]
            if val in nums[i+1:]:
                return [i, nums[i+1:].index(val)+i+1]
            i+=1
