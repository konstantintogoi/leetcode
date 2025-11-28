"""
Solution of the easy problem
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"Find Numbers with Even Number of Digits"
"""
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """Return how many of them contain an even number of digits.

        >>> Solution().findNumbers([12, 345, 2, 6, 7896])
        2
        >>> Solution().findNumbers([555, 901, 482, 1771])
        1
        >>> Solution().findNumbers([100000])
        1

        """
        cnt = 0

        for num in nums:
            ndigits = 0
            while num > 0:
                ndigits += 1
                num = num // 10

            cnt += (ndigits % 2 == 0)

        return cnt

