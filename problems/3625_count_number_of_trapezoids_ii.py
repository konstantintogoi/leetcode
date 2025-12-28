"""
Solution of the hard problem
https://leetcode.com/problems/count-number-of-trapezoids-ii/
"Count Number of Trapezoids II"
"""
from collections import defaultdict
from itertools import combinations
from math import gcd
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """Return the number of trapezoids that can be formed.

        >>> Solution().countTrapezoids(
        ...     [[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]
        ... )
        2
        >>> Solution().countTrapezoids(
        ...     [[0, 0], [1, 0], [0, 1], [2, 1]]
        ... )
        1
        >>> Solution().countTrapezoids(
        ...     [[-32, 12], [-32, 94], [-32, -15], [-30, 88]]
        ... )
        0
        >>> Solution().countTrapezoids(
        ...     [[32, -48], [35, -48], [35, 39], [99, -48]]
        ... )
        0
        >>> Solution().countTrapezoids(
        ...     [[34, 88], [-62, -38], [26, 88], [91, 88], [47, -38]]
        ... )
        3
        >>> Solution().countTrapezoids([
        ...     [71, -89], [-75, -89], [-9, 11], [-24, -89],
        ...     [-51, -89], [-77, -89], [42, 11],
        ... ])
        10
        >>> Solution().countTrapezoids([
        ...     [69, 72], [-57, -98], [69, 4], [69, -12],
        ...     [-100, -36], [22, -99], [71, -59], [69, -36],
        ...     [-57, 6], [69, -59], [71, -12],
        ... ])
        23
        >>> Solution().countTrapezoids([
        ...     [10, -75], [-36, -2], [5, -66], [-84, 1], [-36, 16],
        ...     [-10, -55], [59, 96], [79, 16], [10, -93], [-36,96],
        ...     [24, 63], [10, 63], [-36, -66],
        ... ])
        25
        >>> Solution().countTrapezoids([
        ...     [77, -11], [-40, -53], [-5, 94], [-61, -53], [-40, 78],
        ...     [28, 45], [77, 94], [79, 96], [-61, 39], [-62, -62],
        ...     [77, 23], [28, -20], [-61,38],
        ... ])
        26
        >>> Solution().countTrapezoids([
        ...     [-33, -9], [30, -37], [-10, -9], [61, -9],
        ...     [56, -67], [36, -9], [36, 100], [36, 96],
        ...     [-32, 84], [18, 34], [-10, -82],
        ... ])
        3
        >>> Solution().countTrapezoids([
        ...     [-83, 94], [88, 94], [88, -12], [60, 92], [-30, 94],
        ...     [90, 94], [77, -47], [-68, -96], [-30, -77], [-63, -87],
        ...     [-68, -77], [62, 3], [88, -30], [-30, -30], [60, -30]
        ... ])
        48

        """
        slopes = defaultdict(lambda: defaultdict(int))
        reducted_slopes = defaultdict(lambda: defaultdict(int))

        for (x1, y1), (x2, y2) in combinations(points, 2):
            dy, dx = y2 - y1, x2 - x1

            if dx < 0 or (dx == 0 and dy < 0):
                dy, dx = -dy, -dx

            slope = (dy << 12) | (dx + 2000)

            if (g := gcd(abs(dy), dx)):
                dy //= g
                dx //= g

            reducted_slope = (dy << 12) | (dx + 2000)

            b = y1 * dx - x1 * dy
            slopes[slope][b] += 1
            reducted_slopes[reducted_slope][b] += 1

        return self.count(reducted_slopes) - self.count(slopes) // 2

    def count(self, sides_counter: dict[int, dict[int, int]]) -> int:
        cnt = 0

        for sides in sides_counter.values():
            remaining_sides_cnt = sum(sides.values())

            for sides_cnt in sides.values():
                remaining_sides_cnt -= sides_cnt
                cnt += sides_cnt * remaining_sides_cnt

        return cnt

