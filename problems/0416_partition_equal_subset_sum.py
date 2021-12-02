"""
Solution of the medium problem
https://leetcode.com/problems/partition-equal-subset-sum/
"Partition Equal Subset Sum"
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """Partition Equal Subset sum.

        >>> Solution().canPartition([1, 5, 11, 5])
        True
        >>> Solution().canPartition([1, 2, 3, 5])
        False

        """
        s = sum(nums)
        if s % 2:
            return False
        else:
            psum = s // 2

        W = psum + 1
        n = len(nums)
        table = [[0 for i in range(n)] for w in range(W)]

        for w in range(1, W):
            for i in range(1, n):
                table[w][i] = table[w][i - 1]
                if nums[i] <= w:
                    val = table[w - nums[i]][i - 1] + nums[i]
                    if table[w][i] < val:
                        table[w][i] = val

        return psum == table[W - 1][n - 1]
