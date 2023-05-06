class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            left = numbers[l]
            right = numbers[r]
            total = left + right

            if total == target:
                return [l+1, r+1]
            elif total > target:
                while numbers[r] == right:
                    r -= 1
            else:
                while numbers[l] == left:
                    l += 1
