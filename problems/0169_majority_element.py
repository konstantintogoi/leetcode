"""
Solution of the easy problem
https://leetcode.com/problems/majority-element/
"Majority Element"
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Majority Element.

        >>> Solution().majorityElement([3, 2, 3])
        3
        >>> Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
        2
        >>> Solution().majorityElement([8, 9, 8, 9, 8])
        8
        >>> Solution().majorityElement([10, 9, 9, 9, 10])
        9
        >>> Solution().majorityElement([2, 2])
        2
        >>> Solution().majorityElement([6, 5, 5])
        5

        """
        count = 0
        cand = self.candidate(nums)

        for i in range(len(nums)):
            if nums[i] == cand:
                count += 1

        if count > len(nums) / 2:
            return cand
        else:
            return -1

    def candidate(self, nums):
        index, count = 0, 0

        for i in range(len(nums)):
            if nums[index] == nums[i]:
                count += 1
            else:
                count -= 1

            if count == 0:
                index = i
                count = 1

        return nums[index]
