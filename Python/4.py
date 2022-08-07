class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        start1 = 0
        start2 = 0

        len1 = len(nums1)
        len2 = len(nums2)

        targetLength = (len1 + len2) // 2 + 1
        tmpArray = []

        while len(tmpArray) != targetLength:
            if start1 == len1:
                tmpArray.append(nums2[start2])
                start2 += 1
                continue
            if start2 == len2:
                tmpArray.append(nums1[start1])
                start1 += 1
                continue

            if nums1[start1] <= nums2[start2]:
                tmpArray.append(nums1[start1])
                start1 += 1
            elif nums1[start1] > nums2[start2]:
                tmpArray.append(nums2[start2])
                start2 += 1

        if (len1 + len2) % 2 == 0:
            return (tmpArray[-1] + tmpArray[-2]) / 2
        else:
            return tmpArray[-1]
