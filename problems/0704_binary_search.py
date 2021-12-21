"""
Solution of the easy problem
https://leetcode.com/problems/binary-search/
"Binary Search"
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Binary Search.

        >>> Solution().search([-1, 0, 3, 5, 9, 12], 9)
        4
        >>> Solution().search([-1, 0, 3, 5, 9, 12], 2)
        -1

        """
        l, r = -1, len(nums)
        while l + 1 != r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m
            elif nums[m] > target:
                r = m
            else:
                return m

        return -1
