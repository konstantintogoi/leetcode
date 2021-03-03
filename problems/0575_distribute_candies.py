"""
Solution of "Distribute Candies" problem at
https://leetcode.com/problems/distribute-candies/
"""
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        """Distribute Candies.

        >>> Solution().distributeCandies([1, 1, 2, 2, 3, 3])
        3
        >>> Solution().distributeCandies([1, 1, 2, 3])
        2
        >>> Solution().distributeCandies([6, 6, 6, 6])
        1

        """
        n = len(candyType)
        halfn = n // 2
        types = set()
        while len(types) < halfn and candyType:
            types.add(candyType.pop())
        return len(types)

