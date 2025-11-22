"""
Solution of the easy problem
https://leetcode.com/problems/largest-perimeter-triangle/
"Largest Perimeter Triangle"
"""
from bisect import bisect_left
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """Return the largest perimeter of a triangle with a non-zero area.

        >>> Solution().largestPerimeter([2, 1, 2])
        5
        >>> Solution().largestPerimeter([1, 2, 1, 10])
        0

        """
        n = len(nums)
        nums.sort()

        for i in range(n - 1, 0, -1):
            a = nums[i]
            for j in range(i - 1, -1, -1):
                b = nums[j]
                aplusb = a + b
                icmin = bisect_left(nums, aplusb) - 1
                for k in range(icmin, -1, -1):
                    if k == i or k == j:
                        continue
                    c = nums[k]
                    if a + c <= b or b + c <= a:
                        break
                    if a + c > b and b + c > a:
                        return aplusb + c

        return 0

