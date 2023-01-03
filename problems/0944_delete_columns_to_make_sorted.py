"""
Solution of the easy problem
https://leetcode.com/problems/delete-columns-to-make-sorted/
"Delete Columns to Make Sorted"
"""
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """Return the number of columns for deletion to make sorted.

        >>> Solution().minDeletionSize(['cba', 'daf', 'ghi'])
        1
        >>> Solution().minDeletionSize(['a', 'b'])
        0
        >>> Solution().minDeletionSize(['zyx', 'wvu', 'tsr'])
        3

        """
        n, m, cnt = len(strs), len(strs[0]), 0

        for j in range(m):
            for i in range(n - 1):
                if strs[i][j] > strs[i + 1][j]:
                    cnt += 1
                    break

        return cnt

