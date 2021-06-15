"""
Solution of the easy problem - "Remove Duplicates from Sorted Array",
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Remove Duplicates from Sorted Array.

        >>> l = [1, 1, 2]
        >>> Solution().removeDuplicates(l)
        2
        >>> l
        [1, 2]
        >>> l = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        >>> Solution().removeDuplicates(l)
        5
        >>> l
        [0, 1, 2, 3, 4]

        """
        pos, cur = 0, float('inf')

        for num in nums:
            if num != cur:
                nums[pos] = num
                cur = num
                pos += 1

        while len(nums) > pos:
            nums.pop()

        return pos

