"""
Solution of the medium problem
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
"Minimum Score Triangulation of Polygon"
"""
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """Return the minumum possible score that you can achieve.

        >>> Solution().minScoreTriangulation([1, 2, 3])
        6
        >>> Solution().minScoreTriangulation([3, 7, 4, 5])
        144
        >>> Solution().minScoreTriangulation([1, 3, 1, 4, 1, 5])
        13
        >>> Solution().minScoreTriangulation([
        ... 69, 22, 21, 27, 26, 62, 69, 81, 55, 85, 95, 40, 91, 33, 72, 88, 86
        ... ])
        1334781

        """
        n = len(values)
        dp = [[
            0 if abs(i - j) <= 1 else float('inf')
        for j in range(n)] for i in range(n)]

        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    lscore, rscore = dp[i][k], dp[k][j]
                    trianglescore = values[i] * values[k] * values[j]
                    dp[i][j] = min(dp[i][j], lscore + trianglescore + rscore)

        return dp[0][n - 1]

