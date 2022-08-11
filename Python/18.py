class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        sol = []

        def threeSum(threeNums: List[int], sub_total, first_num) -> List[List[int]]:
            # sol = []
            for i in range(len(threeNums)-2):
                if i > 0 and threeNums[i] == threeNums[i-1]:
                    continue
                target = sub_total - threeNums[i]
                l = i+1
                r = len(threeNums)-1
                while l < r:
                    if threeNums[l] + threeNums[r] == target:
                        sol.append([first_num, threeNums[i],
                                   threeNums[l], threeNums[r]])
                        l += 1
                        r -= 1
                        while threeNums[l] == threeNums[l-1] and l < r:
                            l += 1
                        while threeNums[r] == threeNums[r+1] and l < r:
                            r -= 1
                    elif threeNums[l] + threeNums[r] < target:
                        l += 1
                    else:
                        r -= 1

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            threeSum(nums[i+1:], target-nums[i], nums[i])
        return sol
