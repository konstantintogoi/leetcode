"""
Solution of the medium problem - "Integer to Roman",
https://leetcode.com/problems/integer-to-roman/
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        """Integer to Roman.

        >>> Solution().intToRoman(3)
        'III'
        >>> Solution().intToRoman(4)
        'IV'
        >>> Solution().intToRoman(9)
        'IX'
        >>> Solution().intToRoman(58)
        'LVIII'
        >>> Solution().intToRoman(1994)
        'MCMXCIV'

        """
        rnum = ''
        rdigits = (
            ('M', 1000), ('CM', 900),
            ('D', 500), ('CD', 400),
            ('C', 100), ('XC', 90),
            ('L', 50), ('XL', 40),
            ('X', 10), ('IX', 9),
            ('V', 5), ('IV', 4),
            ('I', 1),
        )

        for d, n in rdigits:
            rnum += d * (num // n)
            num %= n

        return rnum

