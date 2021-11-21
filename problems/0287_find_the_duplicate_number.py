"""
Solution of the medium problem
https://leetcode.com/problems/find-the-duplicate-number/
"Find the Duplicate Number"
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Find Duplicate.

        >>> Solution().findDuplicate([1, 3, 4, 2, 2])
        2
        >>> Solution().findDuplicate([3, 1, 3, 4, 2])
        3
        >>> Solution().findDuplicate([1, 1])
        1
        >>> Solution().findDuplicate([1, 1, 2])
        1
        >>> Solution().findDuplicate([2, 2, 2, 2, 2])
        2

        """
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
