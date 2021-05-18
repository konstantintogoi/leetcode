"""
Solution of the medium problem -
"Best Time to Buy and Sell Stock with Transaction Fee",
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """Maximum profit.

        >>> Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)
        8
        >>> Solution().maxProfit([1, 3, 7, 5, 10, 3], 3)
        6

        """
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash

