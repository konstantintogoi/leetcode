"""
Solution of the hard problem - "Median of Two Sorted Arrays",
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
from typing import List


class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int],
    ) -> float:
        """Median of Two Sorted Arrays.

        >>> Solution().findMedianSortedArrays([1, 3], [2])
        2
        >>> Solution().findMedianSortedArrays([1, 2], [3, 4])
        2.5
        >>> Solution().findMedianSortedArrays([0, 0], [0, 0])
        0.0
        >>> Solution().findMedianSortedArrays([], [1])
        1
        >>> Solution().findMedianSortedArrays([2], [])
        2
        >>> Solution().findMedianSortedArrays([1, 2], [1, 2])
        1.5
        >>> Solution().findMedianSortedArrays([1], [1])
        1.0
        >>> Solution().findMedianSortedArrays([1, 2], [1, 2, 3])
        2
        >>> Solution().findMedianSortedArrays([1], [2, 3, 4])
        2.5
        >>> Solution().findMedianSortedArrays([1, 1, 3, 3], [1, 1, 3, 3])
        2.0

        """
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        half = (n1 + n2) // 2
        l, r = 0, n1 - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            lo1 = nums1[i] if i >= 0 else float('-inf')
            lo2 = nums2[j] if j >= 0 else float('-inf')

            hi1 = nums1[i + 1] if (i + 1) < len(nums1) else float('inf')
            hi2 = nums2[j + 1] if (j + 1) < len(nums2) else float('inf')

            if lo1 <= hi2 and lo2 <= hi1:
                lo, hi = max(lo1, lo2), min(hi1, hi2)
                return hi if (n1 + n2) % 2 else (lo + hi) / 2
            elif lo1 > hi2:
                r = i - 1
            else:
                l = i + 1

