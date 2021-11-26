"""
Solution of the easy problem
https://leetcode.com/problems/intersection-of-two-arrays/
"Intersection of Two Arrays"
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Intersection.

        >>> Solution().intersection([1, 2, 2, 1], [2, 2])
        [2]
        >>> Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4])
        [9, 4]

        """
        return list(set(nums1) & set(nums2))
