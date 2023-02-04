"""
Solution of the easy problem
https://leetcode.com/problems/fizz-buzz/
"Fiz Buzz"
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """Fizz Buzz.

        >>> Solution().fizzBuzz(3)
        ['1', '2', 'Fizz']
        >>> Solution().fizzBuzz(5)
        ['1', '2', 'Fizz', '4', 'Buzz']
        >>> Solution().fizzBuzz(15)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

        """
        res = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))

        return res

