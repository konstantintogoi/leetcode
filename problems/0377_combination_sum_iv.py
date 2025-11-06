"""
Solution of the medium problem
https://leetcode.com/problems/combination-sum-iv/
"Combination Sum IV"
"""
from functools import lru_cache
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """Return the number of possible combinations that add up to `target`.

        >>> Solution().combinationSum4([1, 2, 3], 4)
        7
        >>> Solution().combinationSum4([9], 3)
        0

        """
        nums.sort() 

        @lru_cache(None)
        def rec(t):
            res = 0
            for n in nums:
                if n > t:
                    break
                res += 1 if t == n else rec(t - n)
            return res
    
        return rec(target)

