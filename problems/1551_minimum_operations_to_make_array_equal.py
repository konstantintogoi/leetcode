"""
Solution of the medium problem
https://leetcode.com/problems/minimum-operations-to-make-array-equal/
"Minimum Operations to Make Array Equal"
"""
class Solution:
    def minOperations(self, n: int) -> int:
        """Minimum Operations.

        >>> Solution().minOperations(1)
        0
        >>> Solution().minOperations(3)
        2
        >>> Solution().minOperations(5)
        6
        >>> Solution().minOperations(7)
        12
        >>> Solution().minOperations(9)
        20
        >>> Solution().minOperations(2)
        1
        >>> Solution().minOperations(4)
        4
        >>> Solution().minOperations(6)
        9
        >>> Solution().minOperations(8)
        16
        >>> Solution().minOperations(10)
        25

        """
        a = n // 2
        b = a + n % 2
        return a * b
