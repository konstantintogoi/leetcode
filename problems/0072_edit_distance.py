"""
Solution of the medium problem
https://leetcode.com/problems/edit-distance/
"Edit Distance"
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Return the minimum number of operations to convert word 1 to word2.

        >>> Solution().minDistance('horse', 'ros')
        3
        >>> Solution().minDistance('intention', 'execution')
        5
        >>> Solution().minDistance('a', '')
        1
        >>> Solution().minDistance('', '')
        0

        """
        m, n = len(word1), len(word2)

        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1): dp[i][0] = i
        for j in range(1, n + 1): dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                iscore = dp[i][j - 1] + 1
                dscore = dp[i - 1][j] + 1
                mscore = dp[i - 1][j - 1]

                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(iscore, dscore, mscore)
                else:
                    dp[i][j] = min(iscore, dscore, mscore + 1)

        return dp[m][n]

