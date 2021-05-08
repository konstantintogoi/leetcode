"""
Solution of the hard problem - "Find Minimum in Rotated Sorted Array II",
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Find Minimum.

        >>> Solution().findMin([1, 3, 5])
        1
        >>> Solution().findMin([2, 2, 2, 0, 1])
        0
        >>> Solution().findMin([10, 1, 10, 10, 10])
        1

        """
        def dp(i, j):
            if i + 1 == j:
                return nums[i]
            mid = (i + j) // 2
            a = dp(i, mid)
            b = dp(mid, j)
            return min(a, b)

        return dp(0, len(nums))

