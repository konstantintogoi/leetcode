"""
Solution of the medium problem
https://leetcode.com/problems/pacific-atlantic-water-flow/
"Pacific Atlantic Water Flow"
"""
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        """Pacific Atlantic.

        >>> Solution().pacificAtlantic([
        ...     [1, 2, 2, 3, 5],
        ...     [3, 2, 3, 4, 4],
        ...     [2, 4, 5, 3, 1],
        ...     [6, 7, 1, 4, 5],
        ...     [5, 1, 1, 2, 4],
        ... ])
        [[0, 4], [1, 4], [1, 3], [2, 2], [4, 0], [3, 0], [3, 1]]
        >>> Solution().pacificAtlantic([[2, 1], [1, 2]])
        [[0, 0], [1, 1], [1, 0], [0, 1]]

        """
        m = len(matrix)
        n = len(matrix[0])

        pcac = []
        pc = [[False for _ in range(n)] for _ in range(m)]
        ac = [[False for _ in range(n)] for _ in range(m)]

        def dfs(visited, i, j):
            if visited[i][j]:
                return
            visited[i][j] = True
            if pc[i][j] and ac[i][j]:
                pcac.append([i, j])

            val = matrix[i][j]

            if i + 1 < m and val <= matrix[i + 1][j]:
                dfs(visited, i + 1, j);
            if i - 1 >= 0 and val <= matrix[i - 1][j]:
                dfs(visited, i - 1, j);
            if j + 1 < n and val <= matrix[i][j + 1]:
                dfs(visited, i, j + 1);
            if j - 1 >= 0 and val <= matrix[i][j - 1]:
                dfs(visited, i, j - 1);

        for i in range(m):
            dfs(pc, i, 0);
            dfs(ac, i, n - 1)

        for j in range(n):
            dfs(pc, 0, j);
            dfs(ac, m - 1, j)

        return pcac
