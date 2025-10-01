"""
Solution of the medium problem
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"Search in Rotated Sorted Array II"
"""
from bisect import bisect_left
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """Return `True` if `target` is in `nums`, or `False` otherwise.

        >>> Solution().search([2, 5, 6, 0, 0, 1, 2], 0)
        True
        >>> Solution().search([2, 5, 6, 0, 0, 1, 2], 3)
        False

        """
        shift = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                shift = i + 1

        l = bisect_left(nums, target, 0, shift)
        r = bisect_left(nums, target, shift, n)

        return nums[l] == target or (r < n and nums[r] == target)

