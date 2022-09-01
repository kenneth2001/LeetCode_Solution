class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Key Logic: The next permutation is the one that is lexicographically larger than the current one.
        n = len(nums)
        i = n - 1
    
        # Find the first number from the end which is larger than the next one
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        i -= 1

        if i >= 0:
            j = n - 1

            # Find the first number from the end which is larger than or equal to the i-th number
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
