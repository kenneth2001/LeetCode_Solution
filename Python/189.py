class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def swap(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        n = len(nums)
        k = k % n

        swap(nums, 0, n-1)
        swap(nums, 0, k-1)
        swap(nums, k, n-1)
