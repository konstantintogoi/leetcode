"""
Solution of the medium problem
https://leetcode.com/problems/count-number-of-trapezoids-i/
"Count Number of Trapezoids I"
"""
from collections import defaultdict
from itertools import combinations
from typing import List


class Solution:
    mod = (10 ** 9) + 7

    def countTrapezoids(self, points: List[List[int]]) -> int:
        """Return the number of unique horizontal trapezoids.

        >>> Solution().countTrapezoids([[1,0], [2,0], [3,0], [2,2], [3,2]])
        3
        >>> Solution().countTrapezoids([[0,0], [1,0], [0,1], [2,1]])
        1
        >>> Solution().countTrapezoids([[54,91], [-37,91], [-6,91], [-33,91]])
        0
        >>> Solution().countTrapezoids([
        ...     [62, -25], [-81, -25], [19, -25], [39, -25],
        ...     [1, -25], [-19, -100], [69, -100], [-84, -100],
        ... ])
        30
        >>> Solution().countTrapezoids([
        ...     [77, 37], [-60, 74], [-9, 74], [34, -55], [-54, -23],
        ...     [34, -13], [85, 74], [85, 45], [-18, -13], [18, 37],
        ...     [18, -5], [29, -5], [31, -8], [53, 37],
        ... ])
        22

        """
        counter = defaultdict(int)
        for x, y in points:
            counter[y] += 1

        if len(counter) < 2:
            return 0

        cnt = 0
        nsides = 0
        for n in filter(lambda c: c > 1, counter.values()):
            ncombinations = self.factorial(n) // self.factorial(n - 2) // 2
            cnt += ncombinations * nsides
            nsides += ncombinations

        return cnt % self.mod

    def factorial(self, n: int) -> int:
        nfactorial = 1
        for i in range(2, n + 1):
            nfactorial *= i
        return nfactorial

