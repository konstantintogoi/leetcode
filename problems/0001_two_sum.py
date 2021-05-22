"""
Solution of the easy problem - "Two Sum",
https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def naive_twoSum(self, nums, target):
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if i == j:
                    continue
                elif a + b == target:
                    return i, j

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Two sum.

        >>> Solution().twoSum([2, 7, 11, 15], 9)
        (0, 1)
        >>> Solution().twoSum([3, 2, 4], 6)
        (1, 2)
        >>> Solution().twoSum([3, 2, 3], 6)
        (0, 2)
        >>> Solution().twoSum([3, 3], 6)
        (0, 1)

        """
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return seen[target - num], i
            seen[num] = i
 
