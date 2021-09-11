"""
Solution of the hard problem
https://leetcode.com/problems/regular-expression-matching/
"Regular Expression Matching"
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Regular Expression Matching.

        >>> Solution().isMatch('aa', 'a')
        False
        >>> Solution().isMatch('aa', 'a*')
        True
        >>> Solution().isMatch('ab', '.*')
        True
        >>> Solution().isMatch('aab', 'c*a*b')
        True
        >>> Solution().isMatch('mississippi', 'mis*is*p*.')
        False
        >>> Solution().isMatch('aaa', 'a*a')
        True

        """
        return self.dp(s, p, 0, 0)

    def dp(self, s, p, i, j, memo=None):
        memo = memo or {}
        if (i, j) not in memo:
            if j == len(p):
                ans = i == len(s)
            else:
                match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    if self.dp(s, p, i, j + 2):
                        ans = True
                    else:
                        ans = match and self.dp(s, p, i + 1, j)
                else:
                    ans = match and self.dp(s, p, i + 1, j + 1)
            memo[i, j] = ans
        return memo[i, j]
