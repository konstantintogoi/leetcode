"""
Solution of the medium problem
https://leetcode.com/problems/permutations/
"Permutations"
"""
from typing import List


class Solution:
    def permute(self, nums: List[int], memo = None) -> List[List[int]]:
        """Permute.

        >>> Solution().permute([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        >>> Solution().permute([0, 1])
        [[0, 1], [1, 0]]
        >>> Solution().permute([1])
        [[1]]

        """
        if len(nums) == 1:
            return [nums]

        if memo is None:
            memo = {}
            nums = tuple(nums)

        if nums in memo:
            return memo[nums]

        permutations = []

        for i, num in enumerate(nums):
            subnums = nums[:i] + nums[i + 1:]
            for permutation in self.permute(subnums):
                permutations.append([num, *permutation])

        memo[nums] = permutations
        return permutations
