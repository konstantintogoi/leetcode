"""
Solution of the hard problem
https://leetcode.com/problems/critical-connections-in-a-network/
"Critical Connections in a Network"
"""
from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(
        self,
        n: int,
        connections: List[List[int]],
    ) -> List[List[int]]:
        """Critical Connections.

        >>> Solution().criticalConnections(
        ...     4, [[0, 1], [1, 2], [2, 0], [1, 3]]
        ... )
        [[1, 3]]
        >>> Solution().criticalConnections(
        ...     6, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
        ... )
        [[1, 3]]

        """
        edges = defaultdict(list)
        for a, b in connections:
            edges[a].append(b)
            edges[b].append(a)

        ans = []
        disc, low = [0] * n, [0] * n

        def dfs(curr, prev, time):
            disc[curr] = low[curr] = time

            for nxt in edges[curr]:
                if not disc[nxt]:
                    dfs(nxt, curr, time + 1)
                    low[curr] = min(low[curr], low[nxt])
                elif nxt != prev:
                    low[curr] = min(low[curr], disc[nxt])
                if low[nxt] > disc[curr]:
                    ans.append([curr, nxt])

        dfs(0, -1, 1)
        return ans
