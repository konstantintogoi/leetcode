"""
Solution of the medium problem
https://leetcode.com/problems/spiral-matrix/
"Spiral Matrix"
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Return all elements of the `matrix` in spiral order.

        >>> Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
        >>> Solution().spiralOrder([
        ...     [1,  2,  3,  4],
        ...     [5,  6,  7,  8],
        ...     [9, 10, 11, 12],
        ... ])
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

        """
        t, r = len(matrix), len(matrix[0])
        b, l = -1, -1

        ans = []
        i, j = 0, 0
        istep, jstep = 0, 1
        while l < r - 1 and b < t - 1:
            ans.append(matrix[i][j])
            i += istep
            j += jstep

            if j == r:
                i, j = i + 1, j - 1
                istep, jstep = 1, 0
                b += 1
            elif i == t:
                i, j = i - 1, j - 1
                istep, jstep = 0, -1
                r -= 1
            elif j == l:
                i, j = i - 1, j + 1
                istep, jstep = -1, 0
                t -= 1
            elif i == b:
                i, j = i + 1, j + 1
                istep, jstep = 0, 1
                l += 1

        return ans

