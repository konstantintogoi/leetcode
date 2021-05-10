"""
Solution of the easy problem - "Two Sum II - Input array is sorted",
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Two Sum.

        >>> Solution().twoSum([2, 7, 11, 15], 9)
        [1, 2]
        >>> Solution().twoSum([2, 3, 4], 6)
        [1, 3]
        >>> Solution().twoSum([-1, 0], -1)
        [1, 2]

        """
        n = len(numbers)

        for i, num in enumerate(numbers):
            trg = target - num
            if not (numbers[0] <= trg <= numbers[-1]):
                continue

            l, r = -1, n
            while l + 1 != r:
                mid = (l + r) // 2
                if numbers[mid] < trg:
                    l = mid
                else:
                    r = mid

            if i != r and numbers[r] == trg:
                return [min(i + 1, r + 1), max(i + 1, r + 1)]

