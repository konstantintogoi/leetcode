"""
Solution of the easy problem
https://leetcode.com/problems/detect-capital/
"Detect Capital"
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """Return `True` if the usage of capitals in a `word` is right.

        >>> Solution().detectCapitalUse('USA')
        True
        >>> Solution().detectCapitalUse('leetcode')
        True
        >>> Solution().detectCapitalUse('Google')
        True
        >>> Solution().detectCapitalUse('FlaG')
        False

        """
        fstcap = 'A' <= word[0] <= 'Z'
        allcaps = all('A' <= c <= 'Z' for c in word[1:])
        notcaps = all('a' <= c <= 'z' for c in word[1:])
        return (
            (fstcap and allcaps) or
            (not fstcap and notcaps) or
            (fstcap and notcaps)
        )

