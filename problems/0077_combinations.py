"""
Solution of the medium problem
https://leetcode.com/problems/combinations/
"Combinations"
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """Return all possible combinations of `k` numbers from `[1, n]`.

        >>> Solution().combine(4, 2)
        [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        >>> Solution().combine(1, 1)
        [[1]]

        """
        nums = [i for i in range(1, n + 1)]

        combs = []

        def comb(c, lo, hi):
            if len(c) == k:
                combs.append(c.copy())
                return

            for i in range(lo, hi):
                c.append(nums[i])
                comb(c, i + 1, hi)
                c.pop()

        comb([], 0, len(nums))
        return combs

