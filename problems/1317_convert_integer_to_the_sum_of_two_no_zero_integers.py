"""
Solution of the easy problem
https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
"Convert Integer to the Sum of Two No-Zero Integers"
"""
from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        """Return a list of two no-zero integers `[a, b]` where `a + b = n`.

        >>> Solution().getNoZeroIntegers(2)
        [1, 1]
        >>> Solution().getNoZeroIntegers(11)
        [2, 9]

        """
        for i in range(1, int(n / 2) + 1):
            if '0' not in str(i) and '0' not in str(n - i):
                return [i, n - i]

