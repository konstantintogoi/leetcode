"""
Solution of the medium problem - "Binary Tree With Factors",
https://leetcode.com/problems/binary-trees-with-factors/
"""
from typing import List, Set


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """Num Factored Binary Trees.

        >>> Solution().numFactoredBinaryTrees([2, 4])
        3
        >>> Solution().numFactoredBinaryTrees([2, 4, 5, 10])
        7
        >>> Solution().numFactoredBinaryTrees([18, 3, 6, 2])
        12
        >>> Solution().numFactoredBinaryTrees([15, 13, 22, 7, 11])
        5
        >>> Solution().numFactoredBinaryTrees([2,82,64,18,85,86,81,4,67,95])
        11

        """
        cnt = 0
        memo = {}
        for n in arr: cnt += self.factorizations(n, arr, memo)
        return cnt % 1000000007

    def factorizations(
        self, n: int,
        divisors: List[int],
        memo: dict = None,
        divs: Set[int] = None,
    ) -> int:
        """Number of factorizations of `num` by `divisors`.

        >>> Solution().factorizations(2, [2, 4])
        1
        >>> Solution().factorizations(4, [2, 4])
        2
        >>> Solution().factorizations(5, [2, 4, 5, 10])
        1
        >>> Solution().factorizations(10, [2, 4, 5, 10])
        3
        >>> Solution().factorizations(22, [7, 11, 13, 15, 22])
        1

        """
        memo = {} if memo is None else memo
        divs = set(divisors) if divs is None else divs
        if n in memo: return memo[n]

        cnt = 0
        for divisor in divisors:
            if n == divisor:
                cnt += 1
            elif n % divisor == 0 and n // divisor in divs:
                a = self.factorizations(divisor, divisors, memo, divs)
                b = self.factorizations(n // divisor, divisors, memo, divs)
                cnt += a * b

        memo[n] = cnt
        return cnt

