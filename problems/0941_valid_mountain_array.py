"""
Solution of the easy problem
https://leetcode.com/problems/valid-mountain-array/
"Valid Mountain Array"
"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """Return `True` if `arr` is a valid mountain array.

        >>> Solution().validMountainArray([2, 1])
        False
        >>> Solution().validMountainArray([3, 5, 5])
        False
        >>> Solution().validMountainArray([0, 3, 2, 1])
        True

        """
        updirection = len(arr) > 2 and arr[0] < arr[1]
        downdirection = False

        for i in range(1, len(arr)):
            if updirection and downdirection and arr[i] >= arr[i - 1]:
                return False
            if updirection and downdirection:
                continue
            if updirection and arr[i] == arr[i - 1]:
                return False
            if updirection and arr[i] < arr[i - 1]:
                downdirection = True
                continue
            if updirection:
                continue
            if downdirection and arr[i] >= arr[i - 1]:
                return False

        return updirection and downdirection

