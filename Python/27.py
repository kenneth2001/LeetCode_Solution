class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while True:
            if i > len(nums)-1:
                break
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
