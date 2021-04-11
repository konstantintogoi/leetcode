"""
Solution of the easy problem - "Determine if String Halves Are Alike",
https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """Halves are alike.

        >>> Solution().halvesAreAlike('book')
        True
        >>> Solution().halvesAreAlike('textbook')
        False
        >>> Solution().halvesAreAlike('MerryChristmas')
        False
        >>> Solution().halvesAreAlike('AbCdEfGh')
        True
        >>> Solution().halvesAreAlike('tkPAdxpMfJiltOerItiv')
        False

        """
        cnt, half = 0, len(s) / 2
        for i, c in enumerate(s):
            if c in "aeiouAEIOU":
                cnt += 1 if i < half else -1 
        return cnt == 0

