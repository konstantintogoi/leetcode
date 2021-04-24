"""
Solution of the medium problem - "Rotate Image",
https://leetcode.com/problems/rotate-image/
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotate Image.

        >>> matrix = [[1]]
        >>> Solution().rotate(matrix)
        >>> matrix
        [[1]]
        >>> matrix = [[1, 2], [3, 4]]
        >>> Solution().rotate(matrix)
        >>> matrix
        [[3, 1], [4, 2]]
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> Solution().rotate(matrix)
        >>> matrix
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

        """
        n = len(matrix)

        for i in range(n // 2):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

