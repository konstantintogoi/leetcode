"""
Solution of the easy problem
https://leetcode.com/problems/ransom-note/
"Ransom Note"
"""
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """Return `True` if `ransomNote` can be constructed.

        >>> Solution().canConstruct('a', 'b')
        False
        >>> Solution().canConstruct('aa', 'ab')
        False
        >>> Solution().canConstruct('aa', 'aab')
        True

        """
        mletters = defaultdict(int)
        for letter in magazine:
            mletters[letter] += 1

        rletters = defaultdict(int)
        for letter in ransomNote:
            rletters[letter] += 1

        for letter, cnt in rletters.items():
            if cnt > mletters[letter]:
                return False

        return True

