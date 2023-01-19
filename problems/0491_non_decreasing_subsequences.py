"""
Solution of the medium problem
https://leetcode.com/problems/non-decreasing-subsequences/
"Non-decreasing Subsequences"
"""
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """Return non-decreasing subsequences of the given array.

        >>> Solution().findSubsequences([4, 6, 7, 7])
        {(4, 7), (6, 7), (4, 6), (4, 6, 7, 7), (7, 7), (4, 7, 7), (4, 6, 7), (6, 7, 7)}
        >>> Solution().findSubsequences([4, 4, 3, 2, 1])
        {(4, 4)}

        """
        res = set()
        sequence = []

        def backtrack(i):
            if i == len(nums):
                if len(sequence) >= 2:
                    res.add(tuple(sequence))
                return

            if not sequence or sequence[-1] <= nums[i]:
                sequence.append(nums[i])
                backtrack(i + 1)
                sequence.pop()
            backtrack(i + 1)

        backtrack(0)
        return res

