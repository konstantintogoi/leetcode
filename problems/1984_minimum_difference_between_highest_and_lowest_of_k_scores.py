"""
Solution of the easy problem
https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
"Minimum Difference Between Highest and Lowest of K Scores"
"""
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """Return the minimum possible difference.

        >>> Solution().minimumDifference([90], 1)
        0
        >>> Solution().minimumDifference([9, 4, 1, 7], 2)
        2

        """
        nums.sort()

        if len(nums) < k:
            return nums[-1] - nums[0]

        ans = float('inf')
        for i in range(len(nums) - k + 1):
            ans = min(ans, nums[i + k - 1] - nums[i])

        return ans

