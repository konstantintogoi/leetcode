"""
Solution of the easy problem
https://leetcode.com/problems/largest-triangle-area/
"Largest Triangle Area"
"""
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """Return the area of the largest triangle the can be formed.

        >>> round(Solution().largestTriangleArea([
        ...     [0, 0], [0, 1], [1, 0], [0, 2], [2, 0]
        ... ]), 5)
        2.0
        >>> round(Solution().largestTriangleArea([[1, 0], [0, 0], [0, 1]]), 5)
        0.5

        """
        maxsquare = 0
        for i in range(len(points) - 2):
            for j in range(1, len(points) - 1):
                for k in range(2, len(points)):
                    Ax, Ay = points[i]
                    Bx, By = points[j]
                    Cx, Cy = points[k]

                    a = ((Bx - Cx) ** 2 + (By - Cy) ** 2) ** 0.5
                    b = ((Ax - Cx) ** 2 + (Ay - Cy) ** 2) ** 0.5
                    c = ((Ax - Bx) ** 2 + (Ay - By) ** 2) ** 0.5

                    if a + b > c and a + c > b and b + c > a:
                        p = (a + b + c) / 2
                        square = (p * (p - a) * (p - b) * (p - c)) ** 0.5
                        maxsquare = max(square, maxsquare)

        return maxsquare

