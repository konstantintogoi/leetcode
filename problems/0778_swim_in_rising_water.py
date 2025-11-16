"""
Solution of the hard problem
https://leetcode.com/problems/swim-in-rising-water/
"Swim in Rising Water"
"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """Return the minimum time until you can reach the bottom right cell.

        >>> Solution().swimInWater([[0, 2], [1, 3]])
        3
        >>> Solution().swimInWater([
        ...     [0,   1,  2,  3,  4],
        ...     [24, 23, 22, 21,  5],
        ...     [12, 13, 14, 15, 16],
        ...     [11, 17, 18, 19, 20],
        ...     [10,  9,  8,  7,  6],
        ... ])
        16

        """
        queue = [(grid[0][0], 0, 0)]
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]

        while queue:
            elevation, i, j = heappop(queue)
            if visited[i][j]:
                continue
            visited[i][j] = True

            if i == m - 1 and j == n - 1:
                return grid[i][j]

            if i > 0 and not visited[i - 1][j]:
                grid[i - 1][j] = max(grid[i - 1][j], elevation)
                heappush(queue, (grid[i - 1][j], i - 1, j))
            if i + 1 <= m - 1 and not visited[i + 1][j]:
                grid[i + 1][j] = max(grid[i + 1][j], elevation)
                heappush(queue, (grid[i + 1][j], i + 1, j))
            if j > 0 and not visited[i][j - 1]:
                grid[i][j - 1] = max(grid[i][j - 1], elevation)
                heappush(queue, (grid[i][j - 1], i, j - 1))
            if j + 1 <= n - 1 and not visited[i][j + 1]:
                grid[i][j + 1] = max(grid[i][j + 1], elevation)
                heappush(queue, (grid[i][j + 1], i, j + 1))

        return grid[m - 1][n - 1]

