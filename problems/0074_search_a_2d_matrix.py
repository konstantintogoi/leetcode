"""
Solution of the medium problem
https://leetcode.com/problems/search-a-2d-matrix/
"Search a 2D Matrix"
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Return `True` if `target` is in `matrix` or `False` otherwise.

        >>> Solution().searchMatrix([
        ...     [ 1,  3,  5,  7],
        ...     [10, 11, 16, 20],
        ...     [23, 30, 34, 60],
        ... ], 3)
        True
        >>> Solution().searchMatrix([
        ...     [ 1,  3,  5,  7],
        ...     [10, 11, 16, 20],
        ...     [23, 30, 34, 60],
        ... ], 13)
        False
        >>> Solution().searchMatrix([[1]], 1)
        True

        """
        m, n = len(matrix), len(matrix[0])
        mn = m * n

        cnt = 0
        lo, hi = 0, mn
        while lo < hi:
            mid = (lo + hi) // 2
            i, j = mid // n, mid % n

            if target < matrix[i][j]:
                hi = mid
            elif target > matrix[i][j]:
                lo = mid + 1
            else:
                return True

        return False

