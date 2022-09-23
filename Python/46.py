from itertools import permutations


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        t = list(set(permutations(nums)))
        return t
