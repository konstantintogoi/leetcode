"""
Solution of "Merge Sorted Array" problem at
https://leetcode.com/problems/merge-sorted-array/
"""
from typing import List


class Solution:
    def merge(
        self,
        nums1: List[int], m: int,
        nums2: List[int], n: int,
    ) -> None:
        """Merge Sorted Array.

        >>> Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
        [1, 2, 2, 3, 5, 6]
        >>> Solution().merge([1], 1, [], 0)
        [1]

        """
        i, j, k = m - 1, n - 1, len(nums1) - 1

        while 0 <= k:
            a = nums1[i] if 0 <= i < m else float('-inf')
            b = nums2[j] if 0 <= j < n else float('-inf')

            if a < b:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

        return nums1

