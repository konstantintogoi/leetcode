"""
Solution of the medium problem
https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
"Number of Nodes in the Sub-Tree With the Same Label"
"""
from collections import Counter, defaultdict
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        """Return numbers of nodes in the subtree with the same label.

        >>> Solution().countSubTrees(
        ...     7,
        ...     [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
        ...     'abaedcd',
        ... )
        [2, 1, 1, 1, 1, 1, 1]
        >>> Solution().countSubTrees(
        ...     4,
        ...     [[0, 1], [1, 2], [0, 3]],
        ...     'bbbb',
        ... )
        [4, 2, 1, 1]
        >>> Solution().countSubTrees(
        ...     5,
        ...     [[0, 1], [0, 2], [1, 3], [0, 4]],
        ...     'aabab',
        ... )
        [3, 2, 1, 1, 1]
        >>> Solution().countSubTrees(
        ...     7,
        ...     [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],
        ...     'aaabaaa',
        ... )
        [6, 5, 4, 1, 3, 2, 1]
        >>> Solution().countSubTrees(
        ...     6,
        ...     [[0, 1], [0, 2], [1, 3], [3, 4], [4, 5]],
        ...     'cbabaa',
        ... )
        [1, 2, 1, 1, 2, 1]
        >>> Solution().countSubTrees(
        ...     6,
        ...     [[0, 1], [1, 2], [2, 3], [3, 4], [1, 5]],
        ...     'abbacc',
        ... )
        [2, 2, 1, 1, 1, 1]

        """
        lists = defaultdict(list)

        for u, v in edges:
            lists[u].append(v)
            lists[v].append(u)

        counts = [0] * n

        def dfs(u, p):
            counter = Counter()
            for v in lists[u]:
                if v != p:
                    counter += dfs(v, u)
            counter[labels[u]] += 1
            counts[u] = counter[labels[u]]
            return counter

        dfs(0, -1)
        return counts

