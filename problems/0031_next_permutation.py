"""
Solution of the medium problem
https://leetcode.com/problems/next-permutation/
"Next Permutation"
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """Return the next permutation of `nums`.

        >>> nums = [2, 3, 1]
        >>> Solution().nextPermutation(nums)
        >>> nums
        [3, 1, 2]
        >>> nums = [1, 3, 2]
        >>> Solution().nextPermutation(nums)
        >>> nums
        [2, 1, 3]
        >>> nums = [1, 2, 3]
        >>> Solution().nextPermutation(nums)
        >>> nums
        [1, 3, 2]
        >>> nums = [3, 2, 1]
        >>> Solution().nextPermutation(nums)
        >>> nums
        [1, 2, 3]
        >>> nums = [1, 1, 5]
        >>> Solution().nextPermutation(nums)
        >>> nums
        [1, 5, 1]
        >>> nums = [1]
        >>> Solution().nextPermutation(nums)
        >>> nums
        [1]
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            nums.reverse()
            return

        j = len(nums) - 1
        while j > 0 and nums[i] >= nums[j]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])

