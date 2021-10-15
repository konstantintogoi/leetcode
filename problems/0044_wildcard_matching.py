"""
Solution of the hard problem
https://leetcode.com/problems/wildcard-matching/
"Wildcard Matching"
"""
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        """Is Match.

        >>> Solution().isMatch('aa', 'a')
        False
        >>> Solution().isMatch('aa', '*')
        True
        >>> Solution().isMatch('cb', '?a')
        False
        >>> Solution().isMatch(
        ...     'babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab',
        ...     '***bba**a*bbba**aab**b',
        ... )
        False
        >>> Solution().isMatch('', '******')
        True
        >>> Solution().isMatch('', '?')
        False

        """
        if not p:
            return not s
        elif not s:
            return all(c == '*' for c in p)
        elif p[0] == "*":
            return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
        elif p[0] in {s[0], '?'}:
            return self.isMatch(s[1:], p[1:])
        else:
            return False
