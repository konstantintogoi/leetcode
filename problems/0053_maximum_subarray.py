"""
Solution of the easy problem - "Maximum Subarray",
https://leetcode.com/problems/maximum-subarray/
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Maximum Subarray.

        >>> Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        >>> Solution().maxSubArray([1])
        1
        >>> Solution().maxSubArray([0])
        0
        >>> Solution().maxSubArray([-1])
        -1
        >>> Solution().maxSubArray([-100000])
        -100000
        >>> Solution().maxSubArray([-2, -1])
        -1

        """
        maxsum, cumsums = float('-inf'), [0]

        for num in nums:
            cumsum = cumsums[-1] + num
            if cumsum > maxsum:
                maxsum = cumsum
            cumsums.append(0 if cumsum < 0 else cumsum)

        return maxsum

