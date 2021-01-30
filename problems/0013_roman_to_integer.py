"""
Solution of "Roman to Integer" problem at
https://leetcode.com/problems/roman-to-integer/
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        """Roman to Integer.

        >>> Solution().romanToInt('III')
        3
        >>> Solution().romanToInt('IV')
        4
        >>> Solution().romanToInt('IX')
        9
        >>> Solution().romanToInt('LVIII')
        58
        >>> Solution().romanToInt('MCMXCIV')
        1994

        """
        num = 0
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
            while s.startswith(d):
                num += n
                s = s[len(d):]
        return num

