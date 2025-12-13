"""
Solution of the medium problem
https://leetcode.com/problems/smallest-integer-divisible-by-k/
"Smallest Integer Divisible by K"
"""
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """Return the length of `n` s.t. `n` is divisible by `k`.

        >>> Solution().smallestRepunitDivByK(1)
        1
        >>> Solution().smallestRepunitDivByK(2)
        -1
        >>> Solution().smallestRepunitDivByK(3)
        3
        >>> Solution().smallestRepunitDivByK(9)
        9
        >>> Solution().smallestRepunitDivByK(17)
        16

        """
        if k % 10 in {0, 2, 4, 5, 6, 8}:
            return -1

        n = 1
        l = 1
        while n % k != 0:
            n *= 10
            n += 1
            l += 1

        return l

