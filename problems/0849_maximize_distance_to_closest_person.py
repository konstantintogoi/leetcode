"""
Solution of the medium problem
https://leetcode.com/problems/maximize-distance-to-closest-person/
"Maximize Distance to Closest Person"
"""
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """Return the maximum distance to the closest person.

        >>> Solution().maxDistToClosest([1, 0, 0, 0, 1, 0, 1])
        2
        >>> Solution().maxDistToClosest([1, 0, 0, 0])
        3
        >>> Solution().maxDistToClosest([0, 1])
        1

        """
        nseats = len(seats)
        prevseat = -1

        ans = 0
        for i, seat in enumerate(seats):
            if seat == 1:
                ans = i if prevseat < 0 else max(ans, (i - prevseat) // 2)
                prevseat = i

        ans = max(ans, nseats - prevseat - 1)
        return ans

