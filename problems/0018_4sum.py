"""
Solution of "4Sum" problem at
https://leetcode.com/problems/4sum/
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """Four Sum.

        >>> Solution().fourSum([1, 0, -1, 0, -2, 2], target=0)
        [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
        >>> Solution().fourSum([], target=0)
        []
        >>> Solution().fourSum([0, 0, 0, 0], target=0)
        [[0, 0, 0, 0]]
        >>> Solution().fourSum([-4, -3, -2, -1, 0, 0, 1, 2, 3, 4], 0)


        """
        n = len(nums)

        if n < 4:
            return []

        if n == 4:
            if nums[0] + nums[1] + nums[2] + nums[3] == target:
                return [nums]
            else:
                return []

        hset = {}
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                s = target - nums[i] - nums[j]
                if s in hset:
                    hset[s].append((i, j))
                else:
                    hset[s] = [(i, j)]

        quadruplets = {}
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if (nums[i] + nums[j]) in hset:
                    for k, l in hset[nums[i] + nums[j]]:
                        if k not in (i, j) and l not in (i, j):
                            a, b, c, d = sorted([nums[i], nums[j], nums[k], nums[l]])
                            quadruplets[a, b, c, d] = [a, b, c, d]

        return [q for _, q in quadruplets.items()]

