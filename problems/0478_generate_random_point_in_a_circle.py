"""
Solution of the medium problem
https://leetcode.com/problems/generate-random-point-in-a-circle/
"Generate Random point in a Circle"
"""
from math import cos, pi, sin, sqrt
from random import uniform
from typing import List


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        """Generates random point.

        >>> solution = Solution(1.0, 0.0, 0.0)
        >>> solution.randPoint()  # doctest: +SKIP
        >>> solution.randPoint()  # doctest: +SKIP
        >>> solution.randPoint()  # doctest: +SKIP

        """
        a = uniform(0, 2 * pi)
        r = self.r * sqrt(uniform(0, 1))
        return self.x + r * cos(a), self.y + r * sin(a)
