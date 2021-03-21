"""
Solution of "Wiggle Subsequence" problem at
https://leetcode.com/problems/wiggle-subsequence/
"""
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """ Wiggle Subsequence.

        >>> Solution().wiggleMaxLength([0])
        1
        >>> Solution().wiggleMaxLength([0, 0])
        1
        >>> Solution().wiggleMaxLength([0, 0, 0])
        1
        >>> Solution().wiggleMaxLength([3, 3, 3, 2, 5])
        3
        >>> Solution().wiggleMaxLength([1, 7, 4, 9, 2, 5])
        6
        >>> Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])
        7
        >>> Solution().wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9])
        2

        """
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 1 if nums[0] == nums[1] else 2

        memo = {}

        def dp(i, j):
            if i + 2 >= j:
                return 1 if nums[i] == nums[i + 1] else 2

            if (i, j) in memo:
                return memo[i, j]

            skiplen = dp(i + 1, j)

            a = nums[i + 1] - nums[i]
            takelen = 2 if a else 1
            for k in range(i + 2, j):
                b = nums[k] - nums[k - 1]
                if a * b < 0:
                    a = b
                    takelen += 1

            memo[i, j] = max(skiplen, takelen)
            return memo[i, j]

        return dp(0, len(nums))

