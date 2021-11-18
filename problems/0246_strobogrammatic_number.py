"""
Solution of the easy problem
https://leetcode.com/problems/strobogrammatic-number/
"Strobogrammatic Number"
"""
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        """Is Strobogrammatic.

        >>> Solution().isStrobogrammatic('69')
        True
        >>> Solution().isStrobogrammatic('88')
        True
        >>> Solution().isStrobogrammatic('962')
        False
        >>> Solution().isStrobogrammatic('1')
        True
        >>> Solution().isStrobogrammatic('2')
        False
        >>> Solution().isStrobogrammatic('6')
        False
        >>> Solution().isStrobogrammatic('10')
        False

        """
        if num in {'2', '3', '4', '5', '6', '7', '9'}:
            return False
        if set(num) & {'2', '3', '4', '5', '7'}:
            return False
        n = len(num)
        for i in range(n // 2):
            d = num[n - 1 - i]
            d = '6' if d == '9' else '9' if d == '6' else d
            if d != num[i]:
                return False
        return True
