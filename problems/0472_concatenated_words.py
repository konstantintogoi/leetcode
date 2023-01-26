"""
Solution of the hard problem
https://leetcode.com/problems/concatenated-words/
"Concatenated Words"
"""
from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """Return all the concatenated words in the given list of `words`.

        >>> Solution().findAllConcatenatedWordsInADict([
        ...     'cat', 'cats', 'catsdogcats',
        ...     'dog', 'dogcatsdog',
        ...     'hippopotamuses',
        ...     'rat', 'ratcatdogcat',
        ... ])
        ['catsdogcats', 'dogcatsdog', 'ratcatdogcat']
        >>> Solution().findAllConcatenatedWordsInADict(['cat', 'dog', 'catdog'])
        ['catdog']

        """
        s = set(words)
        concatenateWords = []
        memo = {}

        for word in words:
            if self.checkConcatenate(word, s, memo) == True:
                concatenateWords.append(word)
        return concatenateWords

    def checkConcatenate(self, word: str, s: set, memo: set) -> bool:
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]

            if suffix not in memo:
                memo[suffix] = suffix in s or self.checkConcatenate(suffix, s, memo)

            if prefix in s and memo[suffix]:
                return True

        return False

