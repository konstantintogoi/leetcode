"""
Solution of the hard problem
https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
"Longest Path With Different Adjacent Characters"
"""
from collections import defaultdict
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        """Return the length of the longest path.

        >>> Solution().longestPath([-1, 0, 0, 1, 1, 2], 'abacbe')
        3
        >>> Solution().longestPath([-1, 0, 0, 0], 'aabc')
        3
        >>> Solution().longestPath([-1], 'z')
        1

        """
        adjlists = defaultdict(list)

        for u, v in enumerate(parent):
            adjlists[v].append(u)

        res = 1

        def dfs(u):
            nonlocal res
            max1 = max2 = 0

            for v in adjlists[u]:
                path = dfs(v)
                if s[v] != s[u]:
                    if path > max1:
                        max2 = max1
                        max1 = path
                    elif path > max2:
                        max2 = path

            res = max(res, max1 + max2 + 1)
            return max1 + 1

        dfs(0)
        return res

