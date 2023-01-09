"""
Solution of the medium problem
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
"Minimum Time to Collect All Apples in a Tree"
"""
from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]):
        """Return the minimum time you have to spend to collect apples.

        >>> Solution().minTime(
        ...     7,
        ...     [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
        ...     [False, False, True, False, True, True, False],
        ... )
        8
        >>> Solution().minTime(
        ...     7,
        ...     [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
        ...     [False, False, True, False, False, True, False],
        ... )
        6
        >>> Solution().minTime(
        ...     7,
        ...     [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
        ...     [False, False, False, False, False, False, False],
        ... )
        0
        >>> Solution().minTime(
        ...     5,
        ...     [[0, 1], [1, 2], [1, 3], [2, 4]],
        ...     [True, True, False, True, True],
        ... )
        8
        >>> Solution().minTime(
        ...     8,
        ...     [[0, 1], [1, 2], [2, 3], [1, 4], [2, 5], [2, 6], [4, 7]],
        ...     [True, True, False, True, False, True, True, False],
        ... )
        10
        >>> Solution().minTime(
        ...     4,
        ...     [[0, 2], [0, 3], [1, 2]],
        ...     [False, True, False, False],
        ... )
        4

        """
        lists = defaultdict(list)

        for u, v in edges:
            lists[u].append(v)
            lists[v].append(u)

        seen = {}

        def dfs(u) -> int:
            t = 0
            seen[u] = True
            for v in lists[u]:
                t += (0 if v in seen else dfs(v))
            return t + (2 if u and (hasApple[u] or t) else 0)

        return dfs(0)

