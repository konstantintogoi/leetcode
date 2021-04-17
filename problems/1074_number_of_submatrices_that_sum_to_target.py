"""
Solution of the hard problem - "Number of Submatrices That Sum to Target",
https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
"""
from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(
        self,
        matrix: List[List[int]],
        target: int,
    ) -> int:
        """Number of Submatrices.

        >>> Solution().numSubmatrixSumTarget([
        ...     [0, 1, 0],
        ...     [1, 1, 1],
        ...     [0, 1, 0],
        ... ], 0)
        4
        >>> Solution().numSubmatrixSumTarget([
        ...     [1, -1],
        ...     [-1, 1],
        ... ], 0)
        5
        >>> Solution().numSubmatrixSumTarget([[904]], 4)
        0
        >>> Solution().numSubmatrixSumTarget([
        ...     [0, 1, 0],
        ...     [1, 1, 1],
        ...     [0, 1, 0],
        ... ], 1)
        17

        """
        m = len(matrix)
        n = len(matrix[0])
        res = defaultdict(int)
        cnt = 0

        for r in matrix:
            for j in range(1, n):
                r[j] += r[j-1]

        for j in range(n):
            for k in range(j, n):
                res.clear()
                res[0], csum = 1, 0
                for i in range(m):
                    csum += matrix[i][k] - (matrix[i][j-1] if j else 0)
                    cnt += res[csum - target]
                    res[csum] += 1

        return cnt
