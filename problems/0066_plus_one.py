"""
Solution of the easy problem - "Plus One",
https://leetcode.com/problems/plus-one/
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """Plus One.

        >>> Solution().plusOne([1, 2, 3])
        [1, 2, 4]
        >>> Solution().plusOne([4, 3, 2, 1])
        [4, 3, 2, 2]
        >>> Solution().plusOne([0])
        [1]
        >>> Solution().plusOne([9])
        [1, 0]

        """
        digit = digits[-1] + 1
        digits[-1] = digit % 10
        carry_flag = digit // 10
        i, n = 2, len(digits)

        while i < n + 1 and carry_flag:
            digit = digits[n - i] + carry_flag
            digits[n - i] = digit % 10
            carry_flag = digit // 10
            i += 1

        if carry_flag:
            digits.insert(0, 1)

        return digits

