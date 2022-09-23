from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.append(0)
        n = len(nums)

        if n == 1:
            return 1
        
        # remove negative numbers and numbers greater than n
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0

        for i in range(n):
            nums[nums[i] % n] += n

        for i in range(n):
            if nums[i] < n:
                return i 
        return n
            


print(Solution().firstMissingPositive([7, 8, 9, 11, 12, 3])) # 1
print('')
print(Solution().firstMissingPositive([1, 2, 0])) # 3
print('')
print(Solution().firstMissingPositive([3, 4, -1, 1])) # 2
print('')
print(Solution().firstMissingPositive([1])) # 2
print('')
