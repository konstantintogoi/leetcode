"""
Solution of the easy problem
https://leetcode.com/problems/running-sum-of-1d-array/
"Running Sum of 1d Array"
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Return the running sum of `nums`.

        >>> Solution().runningSum([1, 2, 3, 4])
        [1, 3, 6, 10]
        >>> Solution().runningSum([1, 1, 1, 1, 1])
        [1, 2, 3, 4, 5]
        >>> Solution().runningSum([3, 1, 2, 10, 1])
        [3, 4, 6, 16, 17]

        """
        sums = []
        rsum = 0
        for num in nums:
            rsum += num
            sums.append(rsum)
        return sums

