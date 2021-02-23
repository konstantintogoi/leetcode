"""
Solution of "Divide Two Integers" problem at
https://leetcode.com/problems/divide-two-integers/
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """Divide Two Integers.

        >>> Solution().divide(1, 1)
        1
        >>> Solution().divide(0, 1)
        0
        >>> Solution().divide(10, 3)
        3
        >>> Solution().divide(7, -3)
        -2
        >>> Solution().divide(-2147483648, -1)
        2147483647
        >>> Solution().divide(2147483648, 1)
        2147483647
        >>> Solution().divide(2147483648, 2)
        1073741824

        """
        MAX = (1 << 31) - 1
        signed = dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0
        dividend = -dividend if dividend < 0 else dividend
        divisor = -divisor if divisor < 0 else divisor
        if divisor == 1:
            return (-dividend if signed else dividend) if dividend <= MAX + signed else MAX

        quotient = 0
        while dividend >= divisor:
            q = divisor
            i = 1
            while dividend >= q:
                dividend -= q
                q += q
                quotient += i
                i += i

        return -quotient if signed else quotient

