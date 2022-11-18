"""
Solution of the easy problem
https://leetcode.com/problems/ugly-number/
"Ugly Number"
"""
import math


class Solution:
    def isUgly(self, n: int) -> bool:
        """Is Ugly?

        >>> Solution().isUgly(-1)
        False
        >>> Solution().isUgly(0)
        False
        >>> Solution().isUgly(1)
        True
        >>> Solution().isUgly(2)
        True
        >>> Solution().isUgly(3)
        True
        >>> Solution().isUgly(5)
        True
        >>> Solution().isUgly(6)
        True
        >>> Solution().isUgly(14)
        False

        """
        if n <= 0:
            return False

        if n == 1:
            return True

        while (n % 5 == 0):
            n /= 5

        while (n % 3 == 0):
            n /= 3

        while (n % 2 == 0):
            n /= 2

        return n == 1

