"""
Solution of the medium problem
https://leetcode.com/problems/unique-binary-search-trees/
"Unique Binary Search Trees"
"""
class Solution:
    def numTrees(self, n: int) -> int:
        """Return the number of structurally unqiue BST's.

        >>> Solution().numTrees(3)
        5
        >>> Solution().numTrees(1)
        1
        >>> Solution().numTrees(10)
        16796

        """
        dp = [0 for i in range(n + 1)]
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]

