"""
Solution of the medium problem
https://leetcode.com/problems/maximum-ice-cream-bars/
"Maximum Ice Cream Bars"
"""
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """Return the maximum number of ice cream bars the boy can buy.

        >>> Solution().maxIceCream([1, 3, 2, 4, 1], 7)
        4
        >>> Solution().maxIceCream([10, 6, 8, 7, 7, 8], 5)
        0
        >>> Solution().maxIceCream([1, 6, 3, 1, 2, 5], 20)
        6
        >>> Solution().maxIceCream([4, 7, 6, 4, 4, 2, 2, 4, 8, 8], 41)
        9

        """
        costs.sort()

        bars = 0
        for price in costs:
            if price <= coins:
                coins -= price
                bars += 1
            else:
                break

        return bars

