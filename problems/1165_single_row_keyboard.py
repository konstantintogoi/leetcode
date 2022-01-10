"""
Solution of the easy problem
https://leetcode.com/problems/single-row-keyboard/
"Single-Row Keyboard"
"""
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        """Calculate Time.

        >>> Solution().calculateTime('abcdefghijklmnopqrstuvwxyz', 'cba')
        4
        >>> Solution().calculateTime('pqrstuvwxyzabcdefghijklmno', 'leetcode')
        73

        """
        abc = {c: i for i, c in enumerate(keyboard)}
        time = abc[word[0]]
        for i in range(1, len(word)):
            time += abs(abc[word[i]] - abc[word[i - 1]])
        return time
