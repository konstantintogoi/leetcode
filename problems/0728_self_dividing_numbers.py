"""
Solution of the easy problem
https://leetcode.com/problems/self-dividing-numbers/
"Self Dividing Numbers"
"""
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        """Return a list of all the self-dividing numbers in the range.

        >>> Solution().selfDividingNumbers(1, 22)
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
        >>> Solution().selfDividingNumbers(47, 85)
        [48, 55, 66, 77]

        """
        ans = []

        for num in range(left, right + 1):
            haszero = False
            digits = []
            n = num
            while n > 0:
                if (digit := n % 10) == 0:
                    haszero = True
                    break

                digits.append(digit)
                n //= 10

            if not haszero and all(num % digit == 0 for digit in digits):
                ans.append(num)

        return ans

