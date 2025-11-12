"""
Solution of the easy problem
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"Find All Numbers Disappeared in an Array"
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """Return an array of all the integers that do not appear in `nums`.

        >>> Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
        [5, 6]
        >>> Solution().findDisappearedNumbers([1, 1])
        [2]

        """
        res = []
        nums.sort()

        i, j = 0, 1
        while i < len(nums):
            if i == len(nums) - 1 and nums[i] == j:
                j += 1
                break
            if nums[i] == j and nums[i + 1] == j + 1:
                i += 1
                j += 1
            elif nums[i] == j and nums[i + 1] == j:
                i += 1
            elif nums[i] == j and nums[i + 1] > j + 1:
                res.append(j + 1)
                j += 1
            elif nums[i] < j:
                i += 1
                j += 1
            elif nums[i] > j:
                res.append(j)
                j += 1

        while j <= len(nums):
            res.append(j)
            j += 1

        return res

