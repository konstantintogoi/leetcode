"""
Solution of the hard problem
https://leetcode.com/problems/maximal-rectangle/
"Maximal Rectangle"
"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """Find the largest rectangle containing `1`'s and return its area.

        >>> Solution().maximalRectangle([
        ...     ['1', '0', '1', '0', '0'],
        ...     ['1', '0', '1', '1', '1'],
        ...     ['1', '1', '1', '1', '1'],
        ...     ['1', '0', '0', '1', '0'],
        ... ])
        6
        >>> Solution().maximalRectangle([['0']])
        0
        >>> Solution().maximalRectangle([['1']])
        1

        """
        m, n = len(matrix), len(matrix[0])

        maxarea = 0
        for i in range(m):
            heights = []

            for j in range(n):
                height = 0

                k = i
                while k < m and matrix[k][j] == '1':
                    height += 1
                    k += 1

                heights.append(height)

            maxrecarea = self.largestRectangleArea(heights)
            maxarea = max(maxrecarea, maxarea)

        return maxarea

    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        n = len(heights)

        mstack = []
        maxarea = 0
        for i in range(n):
            while mstack and heights[i] <= heights[mstack[-1]]:
                h = heights[mstack.pop()]
                left = mstack[-1] if mstack else -1
                w = i - left - 1

                maxarea = max(h * w, maxarea)

            mstack.append(i)

        return maxarea

