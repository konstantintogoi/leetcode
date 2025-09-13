"""
Solution of the medium problem
https://leetcode.com/problems/spiral-matrix-ii/
"Spiral Matrix II"
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """Return an `n x n` `matrix` filled with elements from `1` to `n^2`.

        >>> Solution().generateMatrix(3)
        [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        >>> Solution().generateMatrix(1)
        [[1]]

        """
        matrix = [[0 for j in range(n)] for i in range(n)]
        t, r = len(matrix), len(matrix[0])
        b, l = -1, -1

        curr = 1
        i, j = 0, 0
        istep, jstep = 0, 1
        while l < r - 1 and b < t - 1:
            matrix[i][j] = curr
            curr += 1
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

        return matrix

