"""
Solution of the hard problem - "Substring with Concatenation of All Words",
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
"""
from collections import defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """Find Substring.

        >>> Solution().findSubstring(
        ...     'barfoothefoobarman',
        ...     ['foo', 'bar'],
        ... )
        [0, 9]
        >>> Solution().findSubstring(
        ...     'wordgoodgoodgoodbestword',
        ...     ['word', 'good', 'best', 'word'],
        ... )
        []
        >>> Solution().findSubstring(
        ...     'barfoofoobarthefoobarman',
        ...     ['bar', 'foo', 'the'],
        ... )
        [6, 9, 12]

        """
        n = len(s)
        k = len(words[0])

        wordsdict = defaultdict(int)
        for word in words:
            wordsdict[word] += 1

        answer = []

        for i in range(n):
            j = i
            wd = dict(wordsdict)

            while sum(wd.values()) and j < n:
                if wd.get(s[j:j + k]):
                    wd[s[j:j + k]] -= 1
                    j += k
                else:
                    break

            if sum(wd.values()) == 0:
                answer.append(i)

        return answer

