"""
Solution of the hard problem
https://leetcode.com/problems/scramble-string/
"Scramble String"
"""
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        """Return `True` if `s2` is a scrambled string of `s1`.

        >>> Solution().isScramble('great', 'rgeat')
        True
        >>> Solution().isScramble('abcde', 'caebd')
        False
        >>> Solution().isScramble('a', 'a')
        True

        """
        memo = {}

        def dp(sa, sb, i, j, l):
            if (i, j, l) in memo:
                return memo[i, j, l]

            if l == 1:
                memo[i, j, l] = (sa[i] == sb[j])
                return memo[i, j, l]

            for k in range(1, l):
                if dp(sa, sb, i, j, k) and dp(sa, sb, i + k, j + k, l - k):
                    memo[i, j, l] = True
                    return True
                if dp(sa, sb, i, j + l - k, k) and dp(sa, sb, i + k, j, l - k):
                    memo[i, j, l] = True
                    return True

            memo[i, j, l] = False
            return False

        return dp(s1, s2, 0, 0, len(s1))

