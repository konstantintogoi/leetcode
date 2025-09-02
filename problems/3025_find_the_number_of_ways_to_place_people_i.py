"""
Solution of the medium problem
https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/
"Find the Number of Ways to Place People I"
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

        """
        points = sorted(points, key=lambda p: (p[0], -p[1]))

        cnt = 0
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                if points[i][1] < points[j][1]:
                    continue

                innerflag = False
                for k in range(i + 1, j):
                    if points[i][1] >= points[k][1] >= points[j][1]:
                        innerflag = True
                        break

                if innerflag is False:
                    cnt += 1

        return cnt

