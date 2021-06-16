"""
Solution of the easy problem - "Remove Element",
https://leetcode.com/problems/remove-element/
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """Remove Element.

        >>> nums = [3, 2, 2, 3]
        >>> Solution().removeElement(nums, 3)
        2
        >>> nums
        [2, 2]
        >>> nums = [0, 1, 2, 2, 3, 0, 4, 2]
        >>> Solution().removeElement(nums, 2)
        5
        >>> nums
        [0, 1, 3, 0, 4]

        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1

        return len(nums)

