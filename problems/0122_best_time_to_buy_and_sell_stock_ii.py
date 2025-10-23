"""
Solution of the medium problem
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"Best Time to Buy and Sell Stock II"
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Return the maximum profit you can achieve.

        >>> Solution().maxProfit([7, 1, 5, 3, 6, 4])
        7
        >>> Solution().maxProfit([1, 2, 3, 4, 5])
        4
        >>> Solution().maxProfit([7, 6, 4, 3, 1])
        0

        """
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit

