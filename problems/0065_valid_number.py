"""
Solution of the hard problem
https://leetcode.com/problems/valid-number/
"Valid Number"
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        """Return whether `s` is a valid number.

        >>> Solution().isNumber('0')
        True
        >>> Solution().isNumber('e')
        False
        >>> Solution().isNumber('.')
        False
        >>> Solution().isNumber('-1E+3')
        True
        >>> Solution().isNumber('0e')
        False
        >>> Solution().isNumber('6ee69')
        False

        """
        s = s.strip()

        chars = set()
        for i, c in enumerate(s):
            if c in {'+', '-'}:
                if i > 0 and s[i - 1] not in {'E', 'e'}:
                    return False
            elif c == '.':
                if '.' in chars or 'E' in chars or 'e' in chars:
                    return False
                chars.add(c)
            elif c in {'E', 'e'}:
                if 'E' in chars or 'e' in chars or 'mantis' not in chars:
                    return False
                chars.add(c)
            elif c.isdigit():
                if 'E' in chars or 'e' in chars:
                    chars.add('exp')
                else:
                    chars.add('mantis')
            else:
                return False

        if 'mantis' not in chars:
            return False
        if 'E' in chars or 'e' in chars:
            return 'exp' in chars
        return True

