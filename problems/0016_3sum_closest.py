"""
Solution of the medium problem
https://leetcode.com/problems/3sum-closest/
"3Sum Closest"
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """Three Sum Closest.

        >>> Solution().threeSumClosest([-1, 2, 1, -4], 1)
        2
        >>> Solution().threeSumClosest([0, 0, 0], 1)
        0
        >>> Solution().threeSumClosest([0, 2, 1, -3], 1)
        0
        >>> Solution().threeSumClosest([1, 2, 5, 10, 11], 12)
        13

        """
        nums.sort()
        n = len(nums)
        diff = float('inf')

        for i in range(n):
            lo, hi = i + 1, n - 1
            while (lo < hi):
                s = nums[i] + nums[lo] + nums[hi]
                if abs(target - s) < abs(diff):
                    diff = target - s
                if s < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break

        return target - diff
