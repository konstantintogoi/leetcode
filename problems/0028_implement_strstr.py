"""
Solution of "Implement strStr()" problem at
https://leetcode.com/problems/implement-strstr/
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Return the index of the first occurrence of needle in haystack.

        >>> Solution().strStr('hello', 'll')
        2
        >>> Solution().strStr('aaaaa', 'bba')
        -1
        >>> Solution().strStr('', '')
        0

        """
        if not haystack and not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            matched = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    matched = False
                    break
            if matched:
                return i

        return -1

