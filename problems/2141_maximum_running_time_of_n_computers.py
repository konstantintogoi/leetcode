"""
Solution of the hard problem
https://leetcode.com/problems/maximum-running-time-of-n-computers/
"Maximum Running Time of N Computers"
"""
from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """Return the maximum number of minutes you can run `n` computers.

        >>> Solution().maxRunTime(2, [3, 3, 3])
        4
        >>> Solution().maxRunTime(2, [1, 1, 1, 1])
        2

        """
        batteries.sort()
        capacity = sum(batteries)

        while batteries[-1] > capacity // n:
            n -= 1
            capacity -= batteries.pop()

        return capacity // n

