"""
Solution of the medium problem
https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/
"Minimum Operations to Make the Integer Zero"
"""
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        """Return the number of operations to make `num1` equal to 0.

        >>> Solution().makeTheIntegerZero(3, -2)
        3
        >>> Solution().makeTheIntegerZero(5, 7)
        -1
        >>> Solution().makeTheIntegerZero(5, -21)
        3
        >>> Solution().makeTheIntegerZero(59, 70)
        -1

        """
        for k in range(1, 61):
            x = num1 - k * num2
            if x < k:
                return -1
            if x.bit_count() <= k:
                return k
        return -1

