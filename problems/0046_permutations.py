"""
Solution of the medium problem
https://leetcode.com/problems/permutations/
"Permutations"
"""
from typing import List


class Solution:
    def permute(self, nums: List[int], memo = None) -> List[List[int]]:
        """Given an array `nums`, return all the possible permutations.

        >>> Solution().permute([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        >>> Solution().permute([0, 1])
        [[0, 1], [1, 0]]
        >>> Solution().permute([1])
        [[1]]

        """
        perms = []

        def perm(p):
            if len(p) == len(nums):
                perms.append(p.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in p:
                    p.append(nums[i])
                    perm(p)
                    p.pop()

        perm([])
        return perms

