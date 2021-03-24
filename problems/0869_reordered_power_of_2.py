"""
Solution of "Reordered Power of 2" problem at
https://leetcode.com/problems/reordered-power-of-2/
"""
from itertools import permutations


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        """Is Reorderd Power of 2.

        >>> Solution().reorderedPowerOf2(1)
        True
        >>> Solution().reorderedPowerOf2(10)
        False
        >>> Solution().reorderedPowerOf2(16)
        True
        >>> Solution().reorderedPowerOf2(24)
        False
        >>> Solution().reorderedPowerOf2(46)
        True

        """
        digits = list(str(N))
        for perm in permutations(digits):
            if perm[0] == '0':
                continue
            _, *digits = '{:b}'.format(int(''.join(perm)))
            if '1' in digits:
                continue
            return True
        return False

