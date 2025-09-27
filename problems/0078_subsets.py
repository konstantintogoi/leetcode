"""
Solution of the medium problem
https://leetcode.com/problems/subsets/
"Subsets"
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Return all possible subsets (the power set).

        >>> Solution().subsets([1, 2, 3])
        [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
        >>> Solution().subsets([0])
        [[], [0]]

        """
        res = []
        nbits = len(nums)
        for i in range(2 ** nbits):
            ibin = bin(i)[2:].rjust(nbits, '0')
            res.append([nums[j] for j, bit in enumerate(ibin) if bit == '1'])
        return res

