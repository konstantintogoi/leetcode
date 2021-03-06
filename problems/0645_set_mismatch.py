"""
Solution of "Set Mismatch" problem at
https://leetcode.com/problems/set-mismatch/
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """Set Mismatch.

        >>> Solution().findErrorNums([1, 2, 2, 4])
        [2, 3]
        >>> Solution().findErrorNums([1, 1])
        [1, 2]
        >>> Solution().findErrorNums([3, 2, 2])
        [2, 1]

        """
        distinctnums = set()
        duplicate = None
        sumnums = 0
        n = len(nums)
        for num in nums:
            if num in distinctnums:
                duplicate = num
            else:
                distinctnums.add(num)
                sumnums += num
        return [duplicate, n * (n + 1) // 2 - sumnums]

