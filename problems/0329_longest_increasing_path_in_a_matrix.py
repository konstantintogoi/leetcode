"""
Solution of the hard problem - "Longest Increasing Path in a Matrix",
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
"""
from collections import defaultdict
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """Longest Increasing Path.

        >>> Solution().longestIncreasingPath([
        ...     [9, 9, 4],
        ...     [6, 6, 8],
        ...     [2, 1, 1],
        ... ])
        4
        >>> Solution().longestIncreasingPath([
        ...     [3, 4, 5],
        ...     [3, 2, 6],
        ...     [2, 2, 1],
        ... ])
        4
        >>> Solution().longestIncreasingPath([[1]])
        1

        """
        m = len(matrix)
        n = len(matrix[0])

        if m == 1 and n == 1:
            return 1

        memo = defaultdict(int)

        def dfs(i, j, prev):
            if i < 0 or j < 0:
                return 0
            elif i >= m or j >= n:
                return 0
            elif matrix[i][j] <= prev:
                return 0
            elif (i, j) in memo:
                return memo[i, j]
            else:
                curr = matrix[i][j]

            top = dfs(i - 1, j, curr)
            bottom = dfs(i + 1, j, curr)
            left = dfs(i, j - 1, curr)
            right = dfs(i, j + 1, curr)

            memo[i, j] = 1 + max(left, top, right, bottom)

            return memo[i, j]

        maxdist = 0

        for i in range(m):
            for j in range(n):
                maxdist = max(maxdist, dfs(i, j, -1))

        return maxdist

