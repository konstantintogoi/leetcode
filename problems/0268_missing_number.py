"""
Solution of the easy problem
https://leetcode.com/problems/missing-number/
"Missing Number"
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Missing Number.

        >>> Solution().missingNumber([3, 0, 1])
        2
        >>> Solution().missingNumber([0, 1])
        2
        >>> Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
        8
        >>> Solution().missingNumber([0])
        1

        """
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)
