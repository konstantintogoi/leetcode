"""
Solution of the medium problem
https://leetcode.com/problems/3sum/
"3Sum"
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Thee Sum.

        >>> Solution().threeSum([-1, 0, 1, 2, -1, 4])
        [[-1, 0, 1], [-1, -1, 2]]
        >>> Solution().threeSum([])
        []
        >>> Solution().threeSum([0])
        []
        >>> Solution().threeSum([0, 0, 0])
        [[0, 0, 0]]
        >>> Solution().threeSum([-1, 1, -1, 1])
        []

        """
        n = len(nums)
        if n < 3:
            return []
        if n == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [nums]
            else:
                return []

        s = {n: i for i, n in enumerate(nums)}
        trs = {}

        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                a, b = nums[i], nums[j]
                c = -(a + b)
                if c in s and s[c] not in (i, j):
                    if a > b:
                        a, b = b, a
                    if a > c:
                        a, c = c, a
                    if b > c:
                        b, c = c, b
                    trs[a, b, c] = [a, b, c]

        return list(trs.values())
