"""
Solution of the medium problem
https://leetcode.com/problems/powerful-integers/
"Powerful Integers"
"""
from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        """Powerful Integers.

        >>> Solution().powerfulIntegers(2, 3, 10)
        [2, 3, 4, 5, 7, 9, 10]
        >>> Solution().powerfulIntegers(3, 5, 15)
        [2, 4, 6, 8, 10, 14]
        >>> Solution().powerfulIntegers(2, 1, 10)
        [9, 2, 3, 5]
        >>> Solution().powerfulIntegers(1, 2, 100)
        [33, 2, 3, 65, 5, 9, 17]

        """
        imax = -1 if x > 1 else 0
        power = 1
        while x > 1:
            if power > bound:
                break
            else:
                power *= x
                imax += 1

        jmax = -1 if y > 1 else 0
        power = 1
        while y > 1:
            if power > bound:
                break
            else:
                power *= y
                jmax += 1

        ans = set()
        for i in range(imax + 1):
            for j in range(jmax + 1):
                integer = x ** i + y ** j
                if integer <= bound:
                    ans.add(integer)
        return list(ans)
