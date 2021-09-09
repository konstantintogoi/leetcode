"""
Solution of the medium problem
https://leetcode.com/problems/string-to-integer-atoi/
"String to Integer (atoi)"
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        """String to Integer.

        >>> Solution().myAtoi('42')
        42
        >>> Solution().myAtoi('   -42')
        -42
        >>> Solution().myAtoi('4193 with word')
        4193
        >>> Solution().myAtoi('words and 987')
        0
        >>> Solution().myAtoi('-91283472332')
        -2147483648
        >>> Solution().myAtoi('+-12')
        0
        >>> Solution().myAtoi('')
        0
        >>> Solution().myAtoi('+1')
        1
        >>> Solution().myAtoi('21474836460')
        2147483647

        """
        LIMIT = 214748364

        integer, i, j, n = 0, 0, 0, len(s)
        while i < n and s[i].isspace(): i += 1
        sign = s[i] if i < n and s[i] in ('-', '+') else ''
        is_negative = True if sign == '-' else False
        if sign: i += 1
        while i < n and  s[i] == '0': i += 1

        while i + j < n and s[i + j].isdigit():
            digit = int(s[i + j])

            if is_negative and integer > LIMIT:
                integer = 2147483648
                break
            elif is_negative and integer == LIMIT and digit > 8:
                integer = 2147483648
                break

            if not is_negative and integer > LIMIT:
                integer = 2147483647
                break
            elif not is_negative and integer == LIMIT and digit > 7:
                integer = 2147483647
                break

            integer = integer * 10 + digit
            j += 1

        return (-1 if is_negative else 1) * integer
