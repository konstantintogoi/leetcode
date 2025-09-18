"""
Solution of the hard problem
https://leetcode.com/problems/text-justification/
"Text Justification"
"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """Return the justified text.

        >>> Solution().fullJustify([
        ...     "This", "is", "an",
        ...     "example", "of", "text",
        ...     "justification."
        ... ], 16)
        ['This    is    an', 'example  of text', 'justification.  ']
        >>> Solution().fullJustify([
        ...     "What","must","be",
        ...     "acknowledgment",
        ...     "shall","be"
        ... ], 16)
        ['What   must   be', 'acknowledgment  ', 'shall be        ']
        >>> Solution().fullJustify([
        ...     "Science","is","what","we",
        ...     "understand","well",
        ...     "enough","to","explain","to",
        ...     "a","computer.","Art","is",
        ...     "everything","else","we","do"
        ... ], 20)
        ['Science  is  what we', 'understand      well', 'enough to explain to', 'a  computer.  Art is', 'everything  else  we', 'do                  ']

        """
        result = []
        currwords = []

        for i, word in enumerate(words):
            needspace = 1 if currwords else 0
            currlen = sum(len(w) for w in currwords)
            currnspaces = len(currwords) - 1 if currwords else 0

            if currlen + currnspaces + needspace + len(word) <= maxWidth:
                currwords.append(word)
            elif len(currwords) == 1:
                result.append(currwords[0] + ' ' * (maxWidth - len(currwords[0])))
                currwords = [word]
            else:
                gaplen = (maxWidth - currlen) // currnspaces 
                gaplens = [gaplen for _ in range(currnspaces)]
                for i in range((maxWidth - currlen) % currnspaces):
                    gaplens[i] += 1

                res = [currwords[0]]
                for j in range(len(gaplens)):
                    res.append(' ' * gaplens[j])
                    res.append(currwords[j + 1])
                result.append(''.join(res))
                currwords = [word]

        if len(currwords) == 1:
            result.append(currwords[0] + ' ' * (maxWidth - len(currwords[0])))
        elif currwords:
            currlen = sum(len(w) for w in currwords)
            currnspaces = len(currwords) - 1 if currwords else 0
            result.append(
                ' '.join(currwords) + ' ' * (maxWidth - currlen - currnspaces)
            )

        return result

