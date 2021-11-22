"""
Solution of the medium problem
https://leetcode.com/problems/coin-change/
"Coin Change"
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Coin Change.

        >>> Solution().coinChange([1, 2, 5], 11)
        3
        >>> Solution().coinChange([2], 3)
        -1
        >>> Solution().coinChange([1], 0)
        0
        >>> Solution().coinChange([1], 1)
        1
        >>> Solution().coinChange([1], 2)
        2
        >>> Solution().coinChange([2, 5, 10, 1], 27)
        4
        >>> Solution().coinChange([186, 419, 83, 408], 6249)
        20

        """
        memo = {}

        def dp(mnt):
            if mnt < 0:
                return float('inf')
            if mnt in memo:
                return memo[mnt]
            if mnt in coins:
                return 1

            memo[mnt] = min(dp(mnt - m) + 1 for m in coins)
            return memo[mnt]

        ncoins = dp(amount) if amount else 0
        return -1 if ncoins == float('inf') else ncoins
