"""
Solution of the easy problem
https://leetcode.com/problems/max-consecutive-ones/
"Max Consecutive Ones"
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """Return the maximum number of consecutive 1's in the array.

        >>> Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
        3
        >>> Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])
        2

        """
        i = 0
        maxw = 0
        w = 0

        while i < len(nums):
            while i < len(nums) and nums[i] == 1:
                i += 1
                w += 1
            else:
                maxw = max(w, maxw)
                i += 1
                w = 0

        return maxw

