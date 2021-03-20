"""
Solution of "Guess Number Higher or Lower" problem at
https://leetcode.com/problems/guess-number-higher-or-lower/
"""
class Solution:
    def guessNumber(self, n: int) -> int:
        """Guess Number.

        >>> from functools import partial
        >>> 
        >>> def cmp(num, pick):
        ...     if pick < num: return -1
        ...     if pick > num: return 1
        ...     return 0
        >>> 
        >>> solution = Solution()
        >>> 
        >>> solution.guess = partial(cmp, pick=6)
        >>> solution.guessNumber(10)
        6
        >>> solution.guess = partial(cmp, pick=1)
        >>> solution.guessNumber(1)
        1
        >>> solution.guess = partial(cmp, pick=1)
        >>> solution.guessNumber(2)
        1
        >>> solution.guess = partial(cmp, pick=2)
        >>> solution.guessNumber(2)
        2

        """
        l, r = -1, n + 1
        while l + 1 != r:
            m = (l + r) // 2
            g = self.guess(m)
            if g > 0:
                l = m
            elif g < 0:
                r = m
            else:
                return m
        return -1

