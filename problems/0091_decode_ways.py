"""
Solution of the medium problem
https://leetcode.com/problems/decode-ways/
"Decode Ways"
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        """Return the number of ways to decode a string `s`.

        >>> Solution().numDecodings('12')
        2
        >>> Solution().numDecodings('226')
        3
        >>> Solution().numDecodings('06')
        0
        >>> Solution().numDecodings('10')
        1
        >>> Solution().numDecodings('2101')
        1
        >>> Solution().numDecodings(
        ...     '111111111111111111111111111111111111111111111'
        ... )
        1836311903

        """
        if s[0] == '0':
            return 0

        dp = [1 for i in range(len(s))]
        if s[len(s) - 1] == '0':
            dp[len(s) - 1] = 0

        for i in range(len(s) - 2, -1, -1):
            dp[i] = dp[i + 1] if s[i] != '0' else 0
            if s[i] != '0' and  int(s[i] + s[i + 1]) <= 26:
                if i < len(s) - 2:
                    dp[i] += dp[i + 2]
                else:
                    dp[i] += 1

        return dp[0]

