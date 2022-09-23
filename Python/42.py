class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        left_idx = 0
        right_idx = len(height) - 1

        left_max = height[left_idx]
        right_max = height[right_idx]

        water = 0

        while left_idx < right_idx:
            if left_max < right_max:
                left_idx += 1
                left_max = max(left_max, height[left_idx])
                water += left_max - height[left_idx]
            else:
                right_idx -= 1
                right_max = max(right_max, height[right_idx])
                water += right_max - height[right_idx]
        
        return water