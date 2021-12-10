"""
Solution of the medium problem
https://leetcode.com/problems/brick-wall/
"Brick Wall"
"""
from collections import defaultdict
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """Least Bricks.

        >>> Solution().leastBricks([
        ...     [1, 2, 2, 1],
        ...     [3, 1, 2],
        ...     [1, 3, 2],
        ...     [2, 4],
        ...     [3, 1, 2],
        ...     [1, 3, 1, 1],
        ... ])
        2
        >>> Solution().leastBricks([
        ...     [100000000],
        ...     [100000000],
        ...     [100000000],
        ... ])
        3

        """
        m = len(wall)
        n = sum(wall[0])
        bricks = defaultdict(lambda: m, {0: m})

        for i in range(m):
            length = 0
            for j in range(len(wall[i])):
                length += wall[i][j]
                bricks[length] -= 1

        bricks.pop(n)
        return min(bricks.values())
