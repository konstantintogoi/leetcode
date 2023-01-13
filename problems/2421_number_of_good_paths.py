"""
Solution of the hard problem
https://leetcode.com/problems/number-of-good-paths/
"Number of Good Paths"
"""
from collections import Counter
from typing import List


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        """Return the number of distinct good paths.

        >>> Solution().numberOfGoodPaths(
        ...     [1, 3, 2, 1, 3],
        ...     [[0, 1], [0, 2], [2, 3], [2, 3]],
        ... )
        6
        >>> Solution().numberOfGoodPaths(
        ...     [1, 1, 2, 2, 3],
        ...     [[0, 1], [1, 2], [2, 3], [2, 4]],
        ... )
        7
        >>> Solution().numberOfGoodPaths([1], [])
        1

        """
        n = len(vals)
        djs = list(range(n))  # disjoint-set
        counters = [Counter({vals[i]: 1}) for i in range(n)]
        edges = sorted((max(vals[u], vals[v]), u, v) for u, v in edges)

        def find(u):
            if djs[u] != u:
                djs[u] = find(djs[u])
            return djs[u]

        res = n
        for val, u, v in edges:
            up, vp = find(u), find(v)
            res += counters[up][val] * counters[vp][val]
            counters[vp][val] += counters[up][val]
            djs[up] = vp

        return res

