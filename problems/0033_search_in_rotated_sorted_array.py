"""
Solution of the medium problem - "Search in Rotated Sorted Array",
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Search in array.

        >>> Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
        4
        >>> Solution().search([4, 5, 6, 7, 0, 1, 2], 3)
        -1
        >>> Solution().search([1], 0)
        -1

        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

