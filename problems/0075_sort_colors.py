"""
Solution of the medium problem
https://leetcode.com/problems/sort-colors/
"Sort Colors"
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Sort `nums` in-place so that objects of the same color are adjacent.

        >>> nums = [2, 0, 2, 1, 1, 0]
        >>> Solution().sortColors(nums)
        >>> nums
        [0, 0, 1, 1, 2, 2]
        >>> nums = [2, 0, 1]
        >>> Solution().sortColors(nums)
        >>> nums
        [0, 1, 2]

        """
        colorscnt = {0: 0, 1: 0, 2: 0}
        for num in nums:
            colorscnt[num] += 1

        for i in range(len(nums)):
            if i < colorscnt[0]:
                nums[i] = 0
            elif i < colorscnt[0] + colorscnt[1]:
                nums[i] = 1
            else:
                nums[i] = 2

