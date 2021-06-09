"""
Solution of the easy problem - "Valid Parentheses",
https://leetcode.com/problems/valid-parentheses/
"""
class Solution:
    def isValid(self, s: str) -> bool:
        """Valid Parentheses.

        >>> Solution().isValid('()')
        True
        >>> Solution().isValid('()[]{}')
        True
        >>> Solution().isValid('(]')
        False
        >>> Solution().isValid('([)]')
        False
        >>> Solution().isValid('{[]}')
        True
        >>> Solution().isValid(']')
        False

        """
        pairs = {')': '(', '}': '{', ']': '['}
        pars = []

        for c in s:
            if c in pairs and not pars:
                return False
            elif c in pairs and pairs[c] != pars.pop():
                return False
            elif c in pairs:
                continue
            else:
                pars.append(c)

        return not pars

