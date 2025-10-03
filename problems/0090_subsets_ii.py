"""
Solution of the medium problem
https://leetcode.com/problems/subsets-ii/
"Subsets II"
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Return all possible subsets (the power set).

        >>> Solution().subsetsWithDup([1, 2, 2])
        [[1, 2], [2], [1], [1, 2, 2], [2, 2], []]
        >>> Solution().subsetsWithDup([0])
        [[0], []]
        >>> Solution().subsetsWithDup([4, 4, 4, 1, 4])
        [[4, 4], [1, 4, 4, 4, 4], [1, 4, 4], [4, 4, 4, 4], [1, 4], [4], [4, 4, 4], [1], [1, 4, 4, 4], []]

        """
        subsets = set()
        nbits = len(nums)

        for i in range(2 ** nbits):
            ibin = '{{i:0{nbits}b}}'.format(nbits=nbits).format(i=i)
            subset = tuple(sorted(
                [nums[j] for j, bit in enumerate(ibin) if bit == '1']
            ))

            subsets.add(subset)

        return [list(subset) for subset in subsets]

