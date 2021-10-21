"""
Solution of the medium problem
https://leetcode.com/problems/powx-n/
"Pow(x, n)"
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """Pow(x, n).

        >>> Solution().myPow(2.0, 10)
        1024.0
        >>> Solution().myPow(2.1, 3)
        9.261000000000001
        >>> Solution().myPow(2.0, -2)
        0.25

        """
        if n == 0: return 1

        sign = True if n < 0 else False
        n = abs(n)

        xpow = 1

        while n != 0:
            if n % 2 != 0:
                xpow *= x
                n -= 1
            x *= x
            n /= 2

        return 1 / xpow if sign else xpow
