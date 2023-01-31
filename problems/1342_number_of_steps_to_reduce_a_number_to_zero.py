"""
Solution of the easy problem
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
"Number of Steps to Reduce a Number to Zero"
"""
class Solution:
    def numberOfSteps(self, num: int) -> int:
        """Return the number of steps to reduce `num` to zero.

        >>> Solution().numberOfSteps(14)
        6
        >>> Solution().numberOfSteps(8)
        4
        >>> Solution().numberOfSteps(123)
        12

        """
        steps = 0

        while num:
            if num % 2:
                num -= 1
            else:
                num /= 2
            steps += 1

        return steps

