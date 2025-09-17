"""
Solution of the medium problem
https://leetcode.com/problems/minimum-path-sum/
"Minimum Path Sum"
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """Return the sum of all numbers along the path.

        >>> Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
        7
        >>> Solution().minPathSum([[1, 2, 3], [4, 5, 6]])
        12

        """
        m, n = len(grid), len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]

        for j in range(1, n): dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m): dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]

