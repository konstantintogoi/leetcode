"""
Solution of the medium problem - "Container With Most Water",
https://leetcode.com/problems/container-with-most-water/
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Container With Most Water.

        >>> Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
        >>> Solution().maxArea([1, 1])
        1
        >>> Solution().maxArea([4, 3, 2, 1, 4])
        16
        >>> Solution().maxArea([1, 2, 1])
        2
        >>> Solution().maxArea([2, 3, 4, 5, 18, 17, 6])
        17

        """
        memo = {}
        def dp(i, j):
            if i == j - 1:
                return (j - i) * min(height[i], height[j])

            if (i, j) not in memo:
                ans = (j - i) * min(height[i], height[j])

                if height[i] <= height[j]:
                    ans1 = dp(i + 1, j)
                    if ans1 > ans:
                        ans = ans1
                else:
                    ans2 = dp(i, j - 1)
                    if ans2 > ans:
                        ans = ans2

                memo[i, j] = ans

            return memo[i, j]

        return dp(0, len(height) - 1)

