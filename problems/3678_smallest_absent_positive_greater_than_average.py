"""
Solution of the easy problem
https://leetcode.com/problems/smallest-absent-positive-greater-than-average/
"Smallest Absent Positive Greater Than Average"
"""
from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        """Return the smallest absent positive integer in `nums`
        such that it is strictly greater than the average of all elements.

        >>> Solution().smallestAbsent([3, 5])
        6
        >>> Solution().smallestAbsent([-1, 1, 2])
        3
        >>> Solution().smallestAbsent([4, -1])
        2
        >>> Solution().smallestAbsent([3, 5])
        6
        >>> Solution().smallestAbsent([-34])
        1

        """
        s = sum(nums)
        avg = s / len(nums)
        nums = set(nums)

        num = int(avg) + 1
        while True:
            if num > 0 and num not in nums: return num
            num += 1

