"""
Solution of the medium problem
https://leetcode.com/problems/insert-interval/
"Insert Interval"
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Return `intervals` after the insertion.

        >>> Solution().insert([[1, 3], [6, 9]], [2, 5])
        [[1, 5], [6, 9]]
        >>> Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
        [[1, 2], [3, 10], [12, 16]]
        >>> Solution().insert([], [5, 7])
        [[5, 7]]
        >>> Solution().insert([[1, 5]], [2, 3])
        [[1, 5]]

        """
        res = []
        inserted = False
        intersection = [newInterval[0], newInterval[1]]

        for start, end in intervals:
            if end < intersection[0]:
                res.append([start, end])
            elif start > intersection[1] and inserted:
                res.append([start, end])
            elif start > intersection[1]:
                res.append(intersection)
                res.append([start, end])
                inserted = True
            else:
                intersection[0] = min(start, intersection[0])
                intersection[1] = max(end, intersection[1])

        if intervals and inserted:
            return res
        elif intervals:
            res.append(intersection)
            return res
        else:
            return [newInterval]

