"""
Solution of the medium problem - "Permutations II",
https://leetcode.com/problems/permutations-ii/
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int], memo = None) -> List[List[int]]:
        """Permute Unique.

        >>> Solution().permuteUnique([1, 1, 2])
        {(1, 2, 1), (2, 1, 1), (1, 1, 2)}
        >>> Solution().permuteUnique([1, 2 ,3])
        {(1, 3, 2), (1, 2, 3), (2, 1, 3), (3, 2, 1), (3, 1, 2), (2, 3, 1)}

        """
        if len(nums) == 1:
            return [nums]

        if memo is None:
            memo = {}
            nums = tuple(nums)

        if nums in memo:
            return memo[nums]

        permutations = set()

        for i, num in enumerate(nums):
            subnums = nums[:i] + nums[i + 1:]
            for permutation in self.permuteUnique(subnums):
                permutations.add((num, *permutation))

        memo[nums] = permutations
        return permutations

