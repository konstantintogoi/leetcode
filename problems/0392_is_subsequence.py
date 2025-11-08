"""
Solution of the easy problem
https://leetcode.com/problems/is-subsequence/
"Is Subsequence"
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Return `True` if `s` is a subsequence of `t`, or `False` otherwise.

        >>> Solution().isSubsequence('abc', 'ahbgdc')
        True
        >>> Solution().isSubsequence('axc', 'ahbgdc')
        False

        """
        i = j = 0

        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                i += 1
            j += 1

        return i == len(s)

