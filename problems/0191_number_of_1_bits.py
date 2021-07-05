"""
Solution of the easy problem - "Number of 1 Bits",
https://leetcode.com/problems/number-of-1-bits/
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        """Number of 1 Bits.

        >>> Solution().hammingWeight('00000000000000000000000000001011')
        3
        >>> Solution().hammingWeight('00000000000000000000000010000000')
        1
        >>> Solution().hammingWeight('11111111111111111111111111111101')
        31

        """
        n, c = int(n, 2), 0
        while n > 0:
            c += n % 2
            n = n // 2
        return c

