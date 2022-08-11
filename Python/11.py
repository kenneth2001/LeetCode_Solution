class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVal = 0
        l = 0
        r = len(height) - 1

        while l < r:
            minHeight = min(height[l], height[r])
            maxVal = max(maxVal, minHeight * (r - l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxVal
        