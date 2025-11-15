"""
Solution of the medium problem
https://leetcode.com/problems/valid-triangle-number/
"Valid Triangle Number"
"""
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """Return the number of triplets that can make triangles.

        >>> Solution().triangleNumber([2, 2, 3, 4])
        3
        >>> Solution().triangleNumber([4, 2, 3, 4])
        4

        """
        n = len(nums)
        nums.sort()

        cnt = 0
        for i in range(n - 2):
            a = nums[i]
            for j in range(i + 1, n - 1):
                b = nums[j]
                cmax = bisect_left(nums, a + b, j + 1, n)
                cnt += (cmax - j - 1)

        return cnt

