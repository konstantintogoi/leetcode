"""
Solution of the easy problem - "Fibonacci Number",
https://leetcode.com/problems/fibonacci-number/
"""
class Solution:
    def fib(self, n: int) -> int:
        """Fibonacci Number.

        >>> Solution().fib(0)
        0
        >>> Solution().fib(1)
        1
        >>> Solution().fib(2)
        1
        >>> Solution().fib(3)
        2
        >>> Solution().fib(4)
        3
        >>> Solution().fib(5)
        5
        >>> Solution().fib(6)
        8
        >>> Solution().fib(7)
        13
        >>> Solution().fib(8)
        21
        >>> Solution().fib(9)
        34
        >>> Solution().fib(10)
        55

        """
        if n < 2: return n
        prev = 0
        curr = 1
        fsum = 0

        for i in range(2, n + 1):
            fsum = prev + curr
            prev = curr
            curr = fsum

        return fsum

