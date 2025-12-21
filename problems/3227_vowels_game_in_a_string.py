"""
Solution of the medium problem
https://leetcode.com/problems/vowels-game-in-a-string/
"Vowels Game in a String"
"""
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        """Return `True` if Alice wins the game, and `False` otherwise.

        >>> Solution().doesAliceWin('leetcoder')
        True
        >>> Solution().doesAliceWin('bbcd')
        False

        """
        return any(c in {'a', 'e', 'i', 'o', 'u'} for c in s)

