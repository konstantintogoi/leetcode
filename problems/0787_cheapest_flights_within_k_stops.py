"""
Solution of the medium problem
https://leetcode.com/problems/cheapest-flights-within-k-stops/
"Cheapest Flights Within K Stops"
"""
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """The cheapest price from `src` to `dst` with at most `k` stops.

        >>> Solution().findCheapestPrice(
        ...     4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1,
        ... )
        700
        >>> Solution().findCheapestPrice(
        ...     3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1,
        ... )
        200

        """
        adj = [[] for _ in range(n)]
        for u, v, price in flights:
            adj[u].append((v, price))

        stops = 0
        queue = [(src, 0)]
        mincost = [float('inf') for _ in range(n)]

        while queue and stops <= k:
            for i in range(len(queue)):
                u, cost = queue.pop(0)

                for v, price in adj[u]:
                    if cost + price < mincost[v]:
                        mincost[v] = cost + price
                        queue.append((v, mincost[v]))

            stops += 1

        return -1 if mincost[dst] == float('inf') else mincost[dst]

