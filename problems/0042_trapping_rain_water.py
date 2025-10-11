"""
Solution of the hard problem
https://leetcode.com/problems/trapping-rain-water/
"Trapping Rain Water"
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """Trap.

        >>> Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
        6
        >>> Solution().trap([4, 2, 0, 3, 2, 5])
        9
        >>> Solution().trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6])
        23
        >>> Solution().trap([0])
        0
        >>> Solution().trap([
        ...     6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2,
        ...     7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3,
        ... ])
        83

        """
        n = len(height)
        decrstack = []
        trapped = 0

        for i in range(n):
            while decrstack and height[decrstack[-1]] < height[i]:
                iright = decrstack.pop()
                bottomheight = height[iright]

                ileft = decrstack[-1] if decrstack else iright
                topheight = min(height[ileft], height[i])

                trapped += (i - ileft - 1) * (topheight - bottomheight)

            while decrstack and height[decrstack[-1]] == height[i]:
                decrstack.pop()

            decrstack.append(i)

        return trapped

