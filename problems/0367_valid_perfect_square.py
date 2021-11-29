"""
Solution of the easy problem
https://leetcode.com/problems/valid-perfect-square/
"Valid Perfect Square"
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """Is Perfect Square.

        >>> Solution().isPerfectSquare(16)
        True
        >>> Solution().isPerfectSquare(14)
        False

        """
        l, r = 0, num
        while l + 1 != r:
            mid = (l + r) // 2
            if mid * mid < num:
                l = mid
            else:
                r = mid
        return r * r == num
