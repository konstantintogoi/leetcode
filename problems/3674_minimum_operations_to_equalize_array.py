"""
Solution of the easy problem
https://leetcode.com/problems/minimum-operations-to-equalize-array/
"Minimum Operations to Equalize Array"
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """Return the minimum number of operations
        required to make all elements of `nums` equal.

        >>> Solution().minOperations([1, 2])
        1
        >>> Solution().minOperations([5, 5, 5])
        0

        """
        if all(num == nums[0] for num in nums):
            return 0
        else:
            return 1

