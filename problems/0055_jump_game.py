"""
Solution of the medium problem
https://leetcode.com/problems/jump-game/
"Jump Game"
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Return `True` if you can reach the last index, or `False` otherwise.

        >>> Solution().canJump([2, 3, 1, 1, 4])
        True
        >>> Solution().canJump([3, 2, 1, 0, 4])
        False

        """
        dp = [False] * len(nums)
        dp[0] = True

        for i in range(len(nums)):
            if dp[i]:
                for j in range(i + nums[i], i, -1):
                    if j >= len(nums) - 1:
                        return True
                    dp[j] = True

        return dp[len(nums) - 1]

