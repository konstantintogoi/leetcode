"""
Solution of the medium problem
https://leetcode.com/problems/jump-game-ii/
"Jump Game II"
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """Jump.

        >>> Solution().jump([2, 3, 1, 1, 4])
        2
        >>> Solution().jump([2, 3, 0, 1, 4])
        2
        >>> Solution().jump([2, 1])
        1

        """
        memo = {}
        maxpos = len(nums) - 1

        def dp(pos):
            if pos in memo:
                return memo[pos]
            if pos == maxpos:
                return 0

            maxsteps = nums[pos]
            minjumps = float('inf')

            for stepsize in range(1, maxsteps + 1):
                if pos + stepsize <= maxpos:
                    njumps = dp(pos + stepsize)
                    minjumps = min(njumps, minjumps)

            memo[pos] = minjumps + 1
            return memo[pos]

        return dp(0)
