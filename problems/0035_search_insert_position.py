"""
Solution of "Search Insert Position" problem at
https://leetcode.com/problems/search-insert-position/
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Search Insert Position.

        >>> Solution().searchInsert([1, 3, 5, 6], 5)
        2
        >>> Solution().searchInsert([1, 3, 5, 6], 2)
        1
        >>> Solution().searchInsert([1, 3, 5, 6], 7)
        4
        >>> Solution().searchInsert([1, 3, 5, 6], 0)
        0
        >>> Solution().searchInsert([1], 0)
        0

        """
        l, r = -1, len(nums)

        while l + 1 != r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid

        return r

