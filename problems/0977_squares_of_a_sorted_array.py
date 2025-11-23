"""
Solution of the easy problem
https://leetcode.com/problems/squares-of-a-sorted-array/
"Squares of a Sorted Array"
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """Return an array of the squares of each number.

        >>> Solution().sortedSquares([-4, -1, 0, 3, 10])
        [0, 1, 9, 16, 100]
        >>> Solution().sortedSquares([-7, -3, 2, 3, 11])
        [4, 9, 9, 49, 121]

        """
        possquares = []
        negsquares = []

        for num in nums:
            if 0 <= num:
                possquares.append(num * num)
            else:
                negsquares.append(num * num)

        i = 0
        j = len(negsquares) - 1
        squares = []

        while i < len(possquares) and j >= 0:
            if possquares[i] < negsquares[j]:
                squares.append(possquares[i])
                i += 1
            else:
                squares.append(negsquares[j])
                j -= 1

        while i < len(possquares):
            squares.append(possquares[i])
            i+= 1

        while j >= 0:
            squares.append(negsquares[j])
            j -= 1

        return squares

