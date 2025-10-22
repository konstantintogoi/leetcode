"""
Solution of the easy problem
https://leetcode.com/problems/valid-palindrome/
"Valid Palindrome"
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Return `True` if `s` is a palindrome, or `False` otherwise.

        >>> Solution().isPalindrome('A man, a plan, a canal: Panama')
        True
        >>> Solution().isPalindrome('race a care')
        False
        >>> Solution().isPalindrome(' ')
        True

        """
        i = 0
        while i < len(s) and not (s[i].isalpha() or s[i].isdigit()):
            i += 1

        j = len(s) - 1
        while j > 0 and not (s[j].isalpha() or s[j].isdigit()):
            j -= 1

        while i < j:
            while i < j and not (s[i].isalpha() or s[i].isdigit()):
                i += 1
            while i < j and not (s[j].isalpha() or s[j].isdigit()):
                j -= 1

            if i >= j:
                return True

            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False

        return True

