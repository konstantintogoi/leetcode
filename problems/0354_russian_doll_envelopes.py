"""
Solution of the hard problem
https://leetcode.com/problems/russian-doll-envelopes/
"Russian Doll Envelopes"
"""
from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """Max Envelopes.

        >>> Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]])
        3
        >>> Solution().maxEnvelopes([[1, 1], [1, 1], [1, 1]])
        1

        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []

        for _, height in envelopes:
            left = bisect_left(dp, height)
            if left == len(dp): dp.append(height)
            else: dp[left] = height
        return len(dp)
