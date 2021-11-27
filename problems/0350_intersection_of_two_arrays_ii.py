"""
Solution of the easy problem
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"Intersection of Two Arrays II"
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Intersection.

        >>> Solution().intersect([1, 2, 2, 1], [2, 2])
        [2, 2]
        >>> Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4])
        [4, 9]

        """
        nums1.sort()
        nums2.sort()


        ans = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                ans.append(nums1[i])
                i += 1
                j += 1

        return ans
