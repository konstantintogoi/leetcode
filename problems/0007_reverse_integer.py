"""Solution of "Reverse Integer" problem at https://leetcode.com/problems/reverse-integer/"""

MAX = int((2**31 - 1)/10)  # 2147483647 / 10
MIN = int(-2 ** 31 / 10)  # -2147483648 / 10


class Solution:
    def reverse(self, x: int) -> int:
        """Reverse integer.

        >>> Solution().reverse(123)
        321
        >>> Solution().reverse(-123)
        -321
        >>> Solution().reverse(120)
        21
        >>> Solution().reverse(-1563847412)
        0
        >>> Solution().reverse(8463847412)
        0

        """
        rev = 0
        while x != 0:
            div = int(x / 10)
            pop = x - div * 10
            x = div

            if rev > MAX or rev == MAX and pop > 7:
                return 0

            if rev < MIN or rev == MIN and pop <-8:
                return 0

            rev = rev * 10 + pop

        return rev

