"""
Solution of the medium problem
https://leetcode.com/problems/max-consecutive-ones-iii/
"Max Consecutive Ones III"
"""
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """Return the maximum number of consecutive `1'`s in the array.

        >>> Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
        6
        >>> Solution().longestOnes(
        ...     [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
        ... )
        10
        >>> Solution().longestOnes([0, 0, 1, 1, 1, 0, 0], 0)
        3
        >>> Solution().longestOnes([0, 0, 0, 0], 0)
        0

        """
        ans = 0
        i, j = 0, 0
        counter = {0: 0, 1: 0}

        while j < len(nums):
            counter[nums[j]] += 1
            while i <= j and counter[0] > k:
                counter[nums[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)
            j += 1

        return ans

