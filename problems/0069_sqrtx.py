"""
Solution of "Sqrt(x)" problem at
https://leetcode.com/problems/sqrtx/
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        """Sqrt(x).

        >>> Solution().mySqrt(4)
        2
        >>> Solution().mySqrt(8)
        2

        """
        root = 0
        while root * root < x:
            root += 1
        return root - (root * root != x)

