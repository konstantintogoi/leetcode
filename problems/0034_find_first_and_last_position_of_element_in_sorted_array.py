"""
Solution of the medium problem - "Find First and Last Position of Element in Sorted Array",
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Search Range.

        >>> Solution().searchRange([5, 7, 7, 8, 8, 10], 5)
        [0, 0]
        >>> Solution().searchRange([5, 7, 7, 8, 8, 10], 7)
        [1, 2]
        >>> Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
        [3, 4]
        >>> Solution().searchRange([5, 7, 7, 8, 8, 10], 10)
        [5, 5]
        >>> Solution().searchRange([5, 7, 7, 8, 8, 10], 6)
        [-1, -1]
        >>> Solution().searchRange([], 0)
        [-1, -1]

        """
        if len(nums) == 0: return [-1, -1]
        if len(nums) == 1: return [0, 0] if nums[0] == target else [-1, -1]

        lo = hi = None

        l, r = -1, len(nums)
        while l + 1 != r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        lo = r

        if r == len(nums) or nums[r] != target:
            return [-1, -1]

        l, r = -1, len(nums)
        while l + 1 != r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid
        hi = l

        return [lo, hi]

