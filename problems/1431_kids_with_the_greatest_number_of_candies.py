"""
Solution of the easy problem
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"Kids With the Greatest Number of Candies"
"""
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """Kids With the Greatest Number of Candies.

        >>> Solution().kidsWithCandies([2, 3, 5, 1, 3], 3)
        [True, True, True, False, True]
        >>> Solution().kidsWithCandies([4, 2, 1, 1, 2], 1)
        [True, False, False, False, False]
        >>> Solution().kidsWithCandies([12, 1, 12], 10)
        [True, False, True]

        """
        m = max(candies)
        return [False if c + extraCandies < m else True for c in candies]
