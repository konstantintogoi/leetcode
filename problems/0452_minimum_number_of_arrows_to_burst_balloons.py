"""
Solution of the medium problem
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
"Minimum Number of Arrows to Burst Balloons"
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """Return the minimum number of arrows that must be shot.

        >>> Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])
        2
        >>> Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]])
        4
        >>> Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]])
        2

        """
        points.sort(key=lambda p: p[1])
        x, cnt = points[0][1], 1

        for point in points:
            if point[0] > x:
                x = point[1]
                cnt += 1

        return cnt

