"""
Solution of "Palindrome Number" prolblem at
https://leetcode.com/problems/palindrome-number/
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Palindrome Number.

        >>> Solution().isPalindrome(121)
        True
        >>> Solution().isPalindrome(-121)
        False
        >>> Solution().isPalindrome(10)
        False
        >>> Solution().isPalindrome(-101)
        False
        >>> Solution().isPalindrome(11)
        True

        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        xrev = 0
        while x > xrev:
            xrev = xrev * 10 + x % 10
            x = x // 10

        return x == xrev or x == xrev // 10

