class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [[],[nums[0]]]
        prev = self.subsets(nums[1:])
        return ([i+[nums[0]] for i in prev] + [i for i in prev])
    