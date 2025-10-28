"""
Solution of the medium problem
https://leetcode.com/problems/number-of-islands/
"Number of Islands"
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Return the number of islands.

        >>> Solution().numIslands([
        ...     ['1', '1', '1', '1', '0'],
        ...     ['1', '1', '0', '1', '0'],
        ...     ['1', '1', '0', '0', '0'],
        ...     ['0', '0', '0', '0', '0'],
        ... ])
        1
        >>> Solution().numIslands([
        ...     ['1', '1', '0', '0', '0'],
        ...     ['1', '1', '0', '0', '0'],
        ...     ['0', '0', '1', '0', '0'],
        ...     ['0', '0', '0', '1', '1'],
        ... ])
        3

        """
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]

        def bfs(i, j):
            visited[i][j] = True

            adjlist = []
            if i > 0 and grid[i - 1][j] == '1' and not visited[i - 1][j]:
                adjlist.append((i - 1, j))
            if i < m - 1 and grid[i + 1][j] == '1' and not visited[i + 1][j]:
                adjlist.append((i + 1, j))
            if j > 0 and grid[i][j - 1] == '1' and not visited[i][j - 1]:
                adjlist.append((i, j - 1))
            if j < n - 1 and grid[i][j + 1] == '1' and not visited[i][j + 1]:
                adjlist.append((i, j + 1))

            for r, c in adjlist:
                bfs(r, c)

        nislands = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] or grid[i][j] == '0':
                    continue
                nislands += 1
                bfs(i, j)

        return nislands

