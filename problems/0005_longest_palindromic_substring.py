"""
Solution of the medium problem
https://leetcode.com/problems/longest-palindromic-substring/
"Longest Palindromic Substring"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Longest Palindromic Substring.

        >>> Solution().longestPalindrome('babad')
        'bab'
        >>> Solution().longestPalindrome('cbbd')
        'bb'
        >>> Solution().longestPalindrome('a')
        'a'
        >>> Solution().longestPalindrome('ac')
        'a'
        >>> Solution().longestPalindrome('bb')
        'bb'
        >>> Solution().longestPalindrome('ccc')
        'ccc'
        >>> Solution().longestPalindrome('abb')
        'bb'

        """

        table = dict()
        if self.isPalindrome(s, 0, len(s), table):
            return s

        n = len(s)
        maxlen = 0
        imax, jmax = 0, 0

        for i in range(n - 1):
            for j in range(i + 1 + maxlen, n + 1):
                if s[i] == s[j - 1] and self.isPalindrome(s, i, j, table):
                    maxlen = j - i
                    imax, jmax = i, j

        return s[imax:jmax]

    def isPalindrome(self, s: str, i, j, table: dict) -> bool:
        """

        >>> Solution().isPalindrome('babad', 0, 5, {})
        False
        >>> Solution().isPalindrome('baba', 0, 4, {})
        False
        >>> Solution().isPalindrome('abad', 0, 4, {})
        False
        >>> Solution().isPalindrome('aba', 0, 3, {})
        True
        >>> Solution().isPalindrome('bb', 0, 2, {})
        True
        >>> Solution().isPalindrome('ac', 0, 2, {})
        False
        >>> Solution().isPalindrome('a', 0, 1, {})
        True

        """
        if i == j - 1:
            return True

        if i == j - 2:
            return s[i] == s[j - 1]

        if (i, j) not in table:
            if s[i] == s[j - 1]:
                table[i, j] = self.isPalindrome(s, i + 1, j - 1, table)
            else:
                table[i, j] = False

        return table[i, j]
