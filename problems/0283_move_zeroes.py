"""
Solution of the easy problem
https://leetcode.com/problems/move-zeroes/
"Move Zeroes"
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead.

        >>> nums = [0, 1, 0, 3, 12]
        >>> Solution().moveZeroes(nums)
        >>> nums
        [1, 3, 12, 0, 0]
        >>> nums = [0]
        >>> Solution().moveZeroes(nums)
        >>> nums
        [0]

        """
        i = j = 0
        while True:
            while nums[i] != 0:
                i += 1
                if i == len(nums):
                    return

            if i == len(nums) - 1:
                return

            j = i + 1
            while nums[j] == 0:
                j += 1
                if j == len(nums):
                    return

            nums[i], nums[j] = nums[j], nums[i]

