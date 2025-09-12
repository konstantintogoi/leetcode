"""
Solution of the medium problem
https://leetcode.com/problems/merge-intervals/
"Merge Intervals"
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Return an array of the non-overlapping intervals.

        >>> Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
        [[1, 6], [8, 10], [15, 18]]
        >>> Solution().merge([[1, 4], [4, 5]])
        [[1, 5]]
        >>> Solution().merge([[4, 7], [1, 4]])
        [[1, 7]]
        >>> Solution().merge([[1, 4], [0, 4]])
        [[0, 4]]
        >>> Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]])
        [[1, 10]]

        """
        result = []
        intervals.sort()
        for interval in intervals:
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result

