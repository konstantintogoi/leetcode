"""
Solution of the medium problem - "Unique Paths II",
https://leetcode.com/problems/unique-paths-ii/
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """Unique Paths.

        >>> Solution().uniquePathsWithObstacles([
        ...     [0, 0, 0],
        ...     [0, 1, 0],
        ...     [0, 0, 0],
        ... ])
        2
        >>> Solution().uniquePathsWithObstacles([
        ...     [0, 1],
        ...     [0, 0],
        ... ])
        1
        >>> Solution().uniquePathsWithObstacles([
        ...     [0, 0],
        ...     [0, 1],
        ... ])
        0
        >>> Solution().uniquePathsWithObstacles([[1]])
        0
        >>> Solution().uniquePathsWithObstacles([
        ...     [0, 0],
        ...     [1, 1],
        ...     [0, 0],
        ... ])
        0
        >>> Solution().uniquePathsWithObstacles([[0]])
        1
        >>> Solution().uniquePathsWithObstacles([
        ...     [0, 1, 0, 0, 0],
        ...     [1, 0, 0, 0, 0],
        ...     [0, 0, 0, 0, 0],
        ...     [0, 0, 0, 0, 0],
        ... ])
        0

        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]:
            return 0

        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[0][0] = 1

        for i in range(1, m):
            if obstacleGrid[i - 1][0] == 0 and obstacleGrid[i][0] == 0:
                grid[i][0] = grid[i - 1][0]

        for j in range(1, n):
            if obstacleGrid[0][j - 1] == 0 and obstacleGrid[0][j] == 0:
                grid[0][j] = grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                ways = 0
                if obstacleGrid[i - 1][j] == 0:
                    ways += grid[i - 1][j]
                if obstacleGrid[i][j - 1] == 0:
                    ways += grid[i][j - 1]
                grid[i][j] = 0 if obstacleGrid[i][j] else ways

        return grid[m - 1][n - 1]

