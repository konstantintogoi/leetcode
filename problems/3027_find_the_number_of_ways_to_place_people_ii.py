"""
Solution of the hard problem
https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/
"Find the Number of Ways to Place People II"
"""
from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        """Return the number of ways to place people.

        >>> Solution().numberOfPairs([[1, 1], [2, 2], [3, 3]])
        0
        >>> Solution().numberOfPairs([[6, 2], [4, 4], [2, 6]])
        2
        >>> Solution().numberOfPairs([[3, 1], [1, 3], [1, 1]])
        2
        >>> Solution().numberOfPairs([[0, 1], [1, 3], [6, 1]])
        2
        >>> Solution().numberOfPairs([[1, 5], [2, 0], [5, 5]])
        2
        >>> Solution().numberOfPairs([[0, 3], [5, 4], [6, 2]])
        2

        """
        points = sorted(points, key=lambda p: (p[0], -p[1]))

        cnt = 0
        for i in range(len(points) - 1):
            maxlr = None
            if points[i][1] >= points[i + 1][1]:
                maxlr = points[i + 1][1]
                cnt += 1

            for j in range(i + 2, len(points)):
                if points[j][1] > points[i][1]:
                    continue
                if maxlr is None or points[j][1] > maxlr:
                    maxlr = points[j][1]
                    cnt += 1

        return cnt

