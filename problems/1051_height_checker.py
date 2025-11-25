"""
Solution of the easy problem
https://leetcode.com/problems/height-checker/
"Height Checker"
"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """Return the number of indices where `heights[i] != expected[i]`.

        >>> Solution().heightChecker([1, 1, 4, 2, 1, 3])
        3
        >>> Solution().heightChecker([5, 1, 2, 3, 4])
        5
        >>> Solution().heightChecker([1, 2, 3, 4, 5])
        0

        """
        cnt = 0
        sortedheights = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != sortedheights[i]:
                cnt += 1
        return cnt

