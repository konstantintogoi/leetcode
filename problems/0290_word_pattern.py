"""
Solution of the easy problem
https://leetcode.com/problems/word-pattern/
"Word Pattern"
"""
from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """Return `True` if a string `s` follows a `pattern`.

        >>> Solution().wordPattern('abba', 'dog cat cat dog')
        True
        >>> Solution().wordPattern('abba', 'dog cat cat fish')
        False
        >>> Solution().wordPattern('aaaa', 'dog cat cat dog')
        False

        """
        pattern_counter = defaultdict(list)
        for i, c in enumerate(pattern):
            pattern_counter[c].append(i)

        words_counter = defaultdict(list)
        for i, word in enumerate(s.split()):
            words_counter[word].append(i)

        return list(pattern_counter.values()) == list(words_counter.values())

