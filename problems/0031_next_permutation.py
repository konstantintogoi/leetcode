"""
Solution of the medium problem
https://leetcode.com/problems/next-permutation/
"Next Permutation"
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """Next Permutation.

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
        l = 0
        r = len(nums) - 1
        reverse = True
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                reverse = False
                l = j = i
                for k in range(i, len(nums)):
                    if nums[k] > nums[i - 1]:
                        j = k
                    else:
                        break
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                break

        if reverse: l = 0
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
