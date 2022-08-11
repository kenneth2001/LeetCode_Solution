class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            target = 0 - nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    sol += [[nums[i], nums[l], nums[r]]]
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return sol
