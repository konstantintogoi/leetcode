"""
Solution of the medium problem
https://leetcode.com/problems/ones-and-zeroes/
"Ones and Zeroes"
"""
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """Ones and Zeroes.

        >>> Solution().findMaxForm(['10', '0001', '111001', '1', '0'], 5, 3)
        4
        >>> Solution().findMaxForm(['10', '0', '1'], 1, 1)
        2

        """
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i - zeros][j - ones] + 1,
                    )

        return dp[m][n]
