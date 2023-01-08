"""
Solution of the hard problem
https://leetcode.com/problems/max-points-on-a-line/
"Max Points on a Line"
"""
from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """Return the maximum number of points that lie on the same line.

        >>> Solution().maxPoints([[1, 1], [2, 2], [3, 3]])
        3
        >>> Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]])
        4
        >>> Solution().maxPoints([[0, 0]])
        1
        >>> Solution().maxPoints([[0, 0], [1, -1], [1, 1]])
        2
        >>> Solution().maxPoints([[3, 3], [1, 4], [1, 1], [2, 1], [2, 2]])
        3
        >>> Solution().maxPoints([[0, 0], [4, 5], [7, 8], [8, 9], [5, 6], [3, 4], [1, 1]])
        5

        """
        n = len(points)
        lines = defaultdict(set)
        maxlines = 1

        for i in range(n - 1):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2:
                    k = float('inf'), x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    k = k, y1 - k * x1

                lines[k].add((x1, y1))
                lines[k].add((x2, y2))
                maxlines = max(len(lines[k]), maxlines)

        return maxlines

