"""
Solution of the medium problem
https://leetcode.com/problems/perfect-squares/
"Perfect Squares"
"""
class Solution:
    def numSquares(self, n: int) -> int:
        """Return the least number of perfect square numbers that sum to `n`.

        >>> Solution().numSquares(12)
        3
        >>> Solution().numSquares(13)
        2

        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]

