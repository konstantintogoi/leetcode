"""
Solution of the medium problem
https://leetcode.com/problems/find-triangular-sum-of-an-array/
"Find Triangular Sum of an Array"
"""
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        """Return the triangular sum of `nums`.

        >>> Solution().triangularSum([1, 2, 3, 4, 5])
        8
        >>> Solution().triangularSum([5])
        5


        """
        n = len(nums)
        nums = [nums]

        for i in range(n - 1):
            newnums = []
            for j in range(len(nums[-1]) - 1):
                newnums.append((nums[-1][j] + nums[-1][j + 1]) % 10)
            nums.append(newnums)

        return nums[-1][-1]

