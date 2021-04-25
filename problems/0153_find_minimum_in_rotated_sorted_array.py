"""
Solution of the medium problem - "Find Minimum in Rotated Sorted Array",
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Find Minimum.

        >>> Solution().findMin([3, 4, 5, 1, 2])
        1
        >>> Solution().findMin([4, 5, 6, 7, 0, 1, 2])
        0
        >>> Solution().findMin([11, 13, 15, 17])
        11

        """
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]
        return nums[0]

