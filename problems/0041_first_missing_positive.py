"""
Solution of the hard problem
https://leetcode.com/problems/first-missing-positive/
"First Missing Positive"
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """First Missing Positive.

        >>> Solution().firstMissingPositive([2147483647])
        1
        >>> Solution().firstMissingPositive([1, 2, 0])
        3
        >>> Solution().firstMissingPositive([3, 4, -1, 1])
        2
        >>> Solution().firstMissingPositive([7, 8, 9, 11, 12])
        1

        """
        maxnum = 0
        posnums = set()

        for num in nums:
            if num > 0:
                posnums.add(num)
                maxnum = max(num, maxnum)

        for i in range(1, maxnum + 2):
            if i not in posnums:
                return i
