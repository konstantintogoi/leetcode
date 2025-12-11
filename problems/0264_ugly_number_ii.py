"""
Solution of the medium problem
https://leetcode.com/problems/ugly-number-ii/
"Ugly Number II"
"""
from heapq import heappush, heappop, heapreplace


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """Given an integer `n`, return the `nth` ugly number.

        >>> Solution().nthUglyNumber(1)
        1
        >>> Solution().nthUglyNumber(10)
        12
        >>> Solution().nthUglyNumber(11)
        15
        >>> Solution().nthUglyNumber(25)
        54
        >>> Solution().nthUglyNumber(50)
        243
        >>> Solution().nthUglyNumber(100)
        1536
        >>> Solution().nthUglyNumber(473)
        708588

        """
        ugly = [-1]

        num = 2
        pow2 = 1
        while len(ugly) < n:
            heappush(ugly, -num)
            pow2 += 1
            num *= 2

        num = 3
        pow3 = 0
        while num < -ugly[0]:
            heapreplace(ugly, -num)
            pow3 += 1
            num *= 3

        num = 5
        pow5 = 0
        while num < -ugly[0]:
            heapreplace(ugly, -num)
            pow5 += 1
            num *= 5

        pow2 = 1
        num = 2 * 3
        while num < -ugly[0]:
            while num < -ugly[0]:
                heapreplace(ugly, -num)
                num *= 3

            pow2 += 1
            num = (2 ** pow2) * 3

        pow2 = 1
        num = 2 * 5
        while num < -ugly[0]:
            while num < -ugly[0]:
                heapreplace(ugly, -num)
                num *= 5

            pow2 += 1
            num = (2 ** pow2) * 5

        pow3 = 1
        num = 3 * 5
        while num < -ugly[0]:
            while num < -ugly[0]:
                heapreplace(ugly, -num)
                num *= 5

            pow3 += 1
            num = (3 ** pow3) * 5

        pow2 = 1
        num = 2 * 3 * 5
        while num < -ugly[0]:
            pow3 = 1
            while num < -ugly[0]:
                while num < -ugly[0]:
                    heapreplace(ugly, -num)
                    num *= 5

                pow3 += 1
                num = (2 ** pow2) * (3 ** pow3) * 5

            pow2 += 1
            num = (2 ** pow2) * 3 * 5

        return -heappop(ugly)

