"""
Solution of the hard problem
https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/
"Minimum Operations to Make Array Elements Zero"
"""
from math import ceil
from typing import List


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        """Return the minimum number of operations to reduce all elements.

        >>> Solution().minOperations([[1, 2], [3, 4]])
        3
        >>> Solution().minOperations([[2, 6]])
        4
        >>> Solution().minOperations([[1, 8]])
        7
        >>> Solution().minOperations([[3, 10]])
        8
        >>> Solution().minOperations([[4, 8]])
        5

        """
        nops = 0
        for l, r in queries:
            lnops = self.minOps(l - 1)
            rnops = self.minOps(r)
            nops += ceil((rnops - lnops) / 2)
        return nops

    def minOps(self, num: int) -> int:
        i = 1
        base = 1
        nops = 0
        while base <= num:
            nops += ((i + 1) // 2) * (min(base * 2 - 1, num) - base + 1)
            base *= 2
            i += 1
        return nops

