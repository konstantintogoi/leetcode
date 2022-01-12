"""
Solution of the medium problem
https://leetcode.com/problems/find-smallest-common-element-in-all-rows/
"Find Smallest Common Element in All Rows"
"""
from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        """Smallest Common Element.

        >>> Solution().smallestCommonElement([
        ...     [1, 2, 3, 4, 5],
        ...     [2, 4, 5, 8,10],
        ...     [3, 5, 7, 9,11],
        ...     [1, 3, 5, 7, 9],
        ... ])
        5

        """
        isn = mat[0]
        for k in range(1, len(mat)):
            i = j = 0
            tmp = []
            while i < len(isn) or j < len(mat[k]):
                a = isn[i] if i < len(isn) else float('inf')
                b = mat[k][j] if j < len(mat[k]) else float('inf')
                if a < b:
                    i += 1
                elif a > b:
                    j += 1
                else:
                    tmp.append(isn[i])
                    i += 1
                    j += 1
            isn = tmp

        return isn[0] if isn else -1
