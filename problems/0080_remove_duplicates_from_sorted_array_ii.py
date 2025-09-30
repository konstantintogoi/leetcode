"""
Solution of the medium problem
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"Remove Duplicates from Sorted Array II"
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Return `k` after placing the final result in the first `k` slots.

        >>> solution = Solution()
        >>> nums = [1, 1, 1, 2, 2, 3]
        >>> solution.removeDuplicates(nums)
        5
        >>> nums
        [1, 1, 2, 2, 3, 3]
        >>> nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        >>> solution.removeDuplicates(nums)
        7
        >>> nums
        [0, 0, 1, 1, 2, 3, 3, 3, 3]
        >>> nums = [1, 1]
        >>> solution.removeDuplicates(nums)
        2
        >>> nums
        [1, 1]
        >>> nums = [1, 1, 1, 2, 2, 2, 3, 3]
        >>> solution.removeDuplicates(nums)
        6
        >>> nums
        [1, 1, 2, 2, 3, 3, 3, 3]

        """
        i, n = 0, len(nums)
        ndeleted = 0

        while i < n - ndeleted:
            i, num = i + 1, nums[i]

            if i >= n: break
            if nums[i] == num: i += 1
            if i >= n: break

            j = i
            ndel = 0
            while i < n - ndeleted and nums[i] == num:
                ndel += 1
                i += 1

            if ndel:
                for k in range(i, n):
                    nums[j] = nums[k]
                    j += 1

            ndeleted += ndel
            i -= ndel

        return n - ndeleted

