"""
Solution of the medium probelm
https://leetcode.com/problems/maximum-sum-circular-subarray/
"Maximum Sum Circular Subarray"
"""
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """Return the maximum possible sum of a subarray of `nums`.

        >>> Solution().maxSubarraySumCircular([1, -2, 3, -2])
        3
        >>> Solution().maxSubarraySumCircular([5, -3, 5])
        10
        >>> Solution().maxSubarraySumCircular([-3, -2, -3])
        -2

        """
        sumnums = sum(nums)
        maxsum = nums[0]
        minsum = 0

        res = nums[0]
        for i in range(1, len(nums)):
            maxsum = max(maxsum + nums[i], nums[i])
            minsum = min(minsum + nums[i], nums[i])
            res = max(res, maxsum, sumnums - minsum)

        return res

