"""
Solution of "Sqrt(x)" problem at
https://leetcode.com/problems/sqrtx/
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        """Sqrt(x).

        >>> Solution().mySqrt(0)
        0
        >>> Solution().mySqrt(1)
        1
        >>> Solution().mySqrt(2)
        1
        >>> Solution().mySqrt(3)
        1
        >>> Solution().mySqrt(4)
        2
        >>> Solution().mySqrt(8)
        2
        >>> Solution().mySqrt(9)
        3

        """
        root = 0

        while (root + 1) * (root + 1) <= x:
            root += 1
            shift = 2
            while (root + shift) * (root + shift) <= x:
                root += shift
                shift *= 2

        return root

