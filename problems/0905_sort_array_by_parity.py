"""
Solution of the easy problem
https://leetcode.com/problems/sort-array-by-parity/
"Sort Array By Parity"
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """Return any array that satisfies this condition.

        >>> Solution().sortArrayByParity([3, 1, 2, 4])
        [2, 4, 3, 1]
        >>> Solution().sortArrayByParity([0])
        [0]

        """
        i = j = 0
        while True:
            while i < len(nums) and nums[i] % 2 == 0:
                i += 1

            j = i + 1
            while j < len(nums) and nums[j] % 2:
                j += 1

            if i >= len(nums) or j >= len(nums):
                break

            nums[i], nums[j] = nums[j], nums[i]

        return nums

