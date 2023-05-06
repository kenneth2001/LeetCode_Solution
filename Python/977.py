class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        ans = []

        while l <= r:
            left_num = abs(nums[l])
            right_num = abs(nums[r])

            if left_num > right_num:
                l += 1
                ans.append(left_num ** 2)
            else:
                r -= 1
                ans.append(right_num ** 2)

        ans.reverse()
        return ans
