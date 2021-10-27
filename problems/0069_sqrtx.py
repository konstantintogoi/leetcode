"""
Solution of the easy problem
https://leetcode.com/problems/sqrtx/
"Sqrt(x)"
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
        l = 0
        r = x + 1

        while l + 1 != r:
            mid = (l + r) // 2
            mid2 = mid * mid
            if mid2 < x:
                l = mid
            elif mid2 > x:
                r = mid
            else:
                return mid

        return l
