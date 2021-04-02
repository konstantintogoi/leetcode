"""
Solution of "3Sum With Multiplicity" problem at
https://leetcode.com/problems/3sum-with-multiplicity/
"""
from functools import lru_cache
from typing import List



class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """3Sum.

        >>> Solution().threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8)
        20
        >>> Solution().threeSumMulti([1, 1, 2, 2, 2, 2], 5)
        12

        """
        @lru_cache(None)
        def dp(size, t, i):
            if i < 0:
                return 0
            elif size == 1:
                return (arr[i] == t) + dp(1, t, i - 1)
            elif arr[i] > t:
                return dp(size, t, i - 1)
            else:
                return dp(size - 1, t - arr[i], i - 1) + dp(size, t, i - 1)

        ans = dp(3, target, len(arr) - 1)
        dp.cache_clear()
        return ans % 1000000007

