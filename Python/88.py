class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left = m - 1 
        right = n - 1      
        end_point = m + n - 1  

        while right >= 0:
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[end_point] = nums1[left]
                end_point -= 1
                left -= 1
            else:
                nums1[end_point] = nums2[right]
                end_point -= 1
                right -= 1
                