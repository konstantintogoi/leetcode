"""
Solution of the medium problem
https://leetcode.com/problems/find-peak-element/
"Find Peak Element"
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """Find Peak Element.

        >>> Solution().findPeakElement([1])
        0
        >>> Solution().findPeakElement([1, 2])
        1
        >>> Solution().findPeakElement([2, 1])
        0
        >>> Solution().findPeakElement([1, 2, 3, 1])
        2
        >>> Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4])
        1

        """
        nums.insert(0, float('-inf'))
        nums.append(float('-inf'))

        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i - 1
