"""
Solution of the easy problem
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
"Find N Unique Integers Sum up to Zero"
"""
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        """Return array containing unique integers s.t. they add up to 0.

        >>> Solution().sumZero(5)
        [-1, -2, 1, 2, 0]
        >>> Solution().sumZero(3)
        [-1, 1, 0]
        >>> Solution().sumZero(1)
        [0]

        """
        ans = [-i for i in range(1, n//2+1)] + [i for i in range(1, n//2+1)]
        if n % 2 == 1: ans.append(0)
        return ans

