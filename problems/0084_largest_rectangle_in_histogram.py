"""
Solution of the hard problem
https://leetcode.com/problems/largest-rectangle-in-histogram/
"Largest Rectangle in Histogram"
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Return the area of the largest rectangle in the histogram.

        >>> Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
        10
        >>> Solution().largestRectangleArea([2, 4])
        4
        >>> Solution().largestRectangleArea([0, 9])
        9

        """
        heights.append(-1)
        n = len(heights)

        maxs = 0
        mstack = []
        for i in range(n):
            while mstack and heights[i] <= heights[mstack[-1]]:
                h = heights[mstack.pop()]
                left = mstack[-1] if mstack else -1
                w = i - left - 1

                maxs = max(h * w, maxs)

            mstack.append(i)

        return maxs

