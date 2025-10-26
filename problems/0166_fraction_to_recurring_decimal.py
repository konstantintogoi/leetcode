"""
Solution of the medium problem
https://leetcode.com/problems/fraction-to-recurring-decimal/
"Fraction to Recurring Decimal"
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """Return the fraction in string format.

        >>> Solution().fractionToDecimal(1, 2)
        '0.5'
        >>> Solution().fractionToDecimal(2, 1)
        '2'
        >>> Solution().fractionToDecimal(4, 333)
        '0.(012)'
        >>> Solution().fractionToDecimal(-22, -2)
        '11'

        """
        if numerator == 0:
            return '0'

        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')

        dividend = abs(numerator)
        divisor = abs(denominator)
        res.append(str(dividend // divisor))
        remainder = dividend % divisor
        if remainder == 0:
            return ''.join(res)

        res.append('.')
        fraction = {}
        while remainder != 0:
            if remainder in fraction:
                res.insert(fraction[remainder], '(')
                res.append(')')
                break

            fraction[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // divisor))
            remainder %= divisor

        return ''.join(res)

