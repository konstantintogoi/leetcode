"""
Solution of the easy problem
https://leetcode.com/problems/duplicate-zeros/
"Duplicate Zeros"
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """Do not return anything, modify arr in-place instead.

        >>> arr = [1, 0, 2, 3, 0, 4, 5, 0]
        >>> Solution().duplicateZeros(arr)
        >>> arr
        [1, 0, 0, 2, 3, 0, 0, 4]
        >>> arr = [1, 2, 3]
        >>> Solution().duplicateZeros(arr)
        >>> arr
        [1, 2, 3]
        >>> arr = [0, 4, 1, 0, 0, 8, 0, 0, 3]
        >>> Solution().duplicateZeros(arr)
        >>> arr
        [0, 0, 4, 1, 0, 0, 0, 0, 8]

        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                for j in range(len(arr) - 1, i, -1):
                    arr[j] = arr[j - 1]
                i += 1
            i += 1

