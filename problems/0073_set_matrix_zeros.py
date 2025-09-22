"""
Solution of the medium problem
https://leetcode.com/problems/set-matrix-zeroes/
"Set Matrix Zeroes"
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """If an element is `0`, set its entire row and column to `0`'s.

        >>> matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        >>> Solution().setZeroes(matrix)
        >>> matrix
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        >>> matrix = [
        ...     [0, 1, 2, 0],
        ...     [3, 4, 5, 2],
        ...     [1, 3, 1, 5],
        ... ]
        >>> Solution().setZeroes(matrix)
        >>> matrix
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

        """
        zerocols = set()
        zerorows = set()

        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zerocols.add(j)
                    zerorows.add(i)

        for i in range(m):
            if i in zerorows:
                matrix[i] = [0] * n
                continue
            for j in range(n):
                if j in zerocols:
                    matrix[i][j] = 0

