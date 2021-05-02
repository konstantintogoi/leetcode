"""
Solution of the medium problem - "Triangle",
https://leetcode.com/problems/triangle/
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """Minimum Total.

        >>> Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
        11
        >>> Solution().minimumTotal([[-10]])
        -10
        >>> Solution().minimumTotal([[-1], [2, 3], [1, -1, -3]])
        -1

        """
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                l = r = float('inf')
                if j > 0: l = triangle[i - 1][j - 1]
                if j < i: r = triangle[i - 1][j]
                triangle[i][j] += min(l, r)

        return min(triangle[-1])

