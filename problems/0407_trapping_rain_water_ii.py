"""
Solution of the hard problem
https://leetcode.com/problems/trapping-rain-water-ii/
"Trapping Rain Water II"
"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """Return the volume of water elevation map can trap after raining.

        >>> Solution().trapRainWater([
        ...     [1, 4, 3, 1, 3, 2],
        ...     [3, 2, 1, 3, 2, 4],
        ...     [2, 3, 3, 2, 3, 1],
        ... ])
        4
        >>> Solution().trapRainWater([
        ...     [3, 3, 3, 3, 3],
        ...     [3, 2, 2, 2, 3],
        ...     [3, 2, 1, 2, 3],
        ...     [3, 2, 2, 2, 3],
        ...     [3, 3, 3, 3, 3],
        ... ])
        10
        >>> Solution().trapRainWater([
        ...     [5, 5, 5, 1],
        ...     [5, 1, 1, 5],
        ...     [5, 1, 5, 5],
        ...     [5, 2, 5, 8],
        ... ])
        3
        >>> Solution().trapRainWater([
        ...     [5, 8, 7, 7],
        ...     [5, 2, 1, 5],
        ...     [7, 1, 7, 1],
        ...     [8, 9, 6, 9],
        ...     [9, 8, 9, 9],
        ... ])
        12

        """
        m, n = len(heightMap), len(heightMap[0])

        inboundary = [[
            i == 0 or i == m - 1 or j == 0 or j == n - 1 for j in range(n)
        ] for i in range(m)]

        boundary = []
        for i in range(1, m - 1):
            heappush(boundary, (heightMap[i][0], i, 0))
            heappush(boundary, (heightMap[i][n - 1], i, n - 1))
        for j in range(1, n - 1):
            heappush(boundary, (heightMap[0][j], 0, j))
            heappush(boundary, (heightMap[m - 1][j], m - 1, j))

        heappush(boundary, (heightMap[0][0], 0, 0))
        heappush(boundary, (heightMap[0][n - 1], 0, n - 1))
        heappush(boundary, (heightMap[m - 1][0], m - 1, 0))
        heappush(boundary, (heightMap[m - 1][n - 1], m - 1, n - 1))

        visited = [[False for j in range(n)] for i in range(m)]

        trapped = 0
        while boundary:
            h, r, c = heappop(boundary)
            if visited[r][c]: continue
            visited[r][c] = True

            neighbours = set()
            if r > 0: neighbours.add((heightMap[r - 1][c], r - 1, c))
            if r < m - 1: neighbours.add((heightMap[r + 1][c], r + 1, c))
            if c > 0: neighbours.add((heightMap[r][c - 1], r, c - 1))
            if c < n - 1: neighbours.add((heightMap[r][c + 1], r, c + 1))

            for nh, nr, nc in neighbours:
                if inboundary[nr][nc]:
                    continue

                if nh < h:
                    trapped += (h - nh)
                    heightMap[nr][nc] = h

                inboundary[nr][nc] = True
                heappush(boundary, (max(h, nh), nr, nc))

        return trapped

