"""
Solution of "Remove Palindromic Subsequences" problem at
https://leetcode.com/problems/remove-palindromic-subsequences/
"""
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        """Remove Subsequences.

        >>> Solution().removePalindromeSub('ababa')
        1
        >>> Solution().removePalindromeSub('abb')
        2
        >>> Solution().removePalindromeSub('baabb')
        2
        >>> Solution().removePalindromeSub('')
        0

        """
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return 2
        return 1 if n else 0

