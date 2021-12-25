"""
Solution of the medium problem
https://leetcode.com/problems/global-and-local-inversions/
"Global and Local Inversions"
"""
from typing import List


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        """Is Ideal Permutation.

        >>> Solution().isIdealPermutation([1, 0, 2])
        True
        >>> Solution().isIdealPermutation([1, 2, 0])
        False

        """
        for i in range(len(A)):
            if i - A[i] > 1 or i - A[i] < -1:
                return False
        return True
