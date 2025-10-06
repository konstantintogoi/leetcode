"""
Solution of the medium problem
https://leetcode.com/problems/interleaving-string/
"Interleaving String"
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """Return `True` if `s3` is formed by an interleaving of `s1` and `s2`.

        >>> Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
        True
        >>> Solution().isInterleave('aabcc', 'dbbca', 'aadbbbaccc')
        False
        >>> Solution().isInterleave('', '', '')
        True
        >>> Solution().isInterleave('', '', 'a')
        False
        >>> Solution().isInterleave('a', '', 'c')
        False
        >>> Solution().isInterleave('ab', 'bc', 'bbac')
        False

        """
        m, n, o = len(s1), len(s2), len(s3)

        if m + n != o:
            return False
        if n == 0:
            return s1 == s3
        if m == 0:
            return s2 == s3

        dp = [[False for j in range(n + 1)] for i in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = (s3[:i] == s1[:i])

        for j in range(1, n + 1):
            dp[0][j] = (s3[:j] == s2[:j])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                c = s3[i + j - 1]
                if c == s1[i - 1] and c == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif c == s1[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                elif c == s2[j - 1]:
                    dp[i][j] = dp[i][j - 1]

        return dp[m][n]

