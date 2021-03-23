"""
Solution of "Vowel Spellchecker" problem at
https://leetcode.com/problems/vowel-spellchecker/
"""
from typing import List


class Solution:
    def spellchecker(
        self,
        wordlist: List[str],
        queries: List[str],
    ) -> List[str]:
        """Vowel Spellchecker.

        >>> Solution().spellchecker(
        ...     ["KiTe", "kite", "hare", "Hare"],
        ...     [
        ...         "kite", "Kite", "KiTe", "Hare", "HARE",
        ...         "Hear","hear","keti","keet","keto",
        ...     ],
        ... )
        ['kite', 'KiTe', 'KiTe', 'Hare', 'hare', '', '', 'KiTe', '', 'KiTe']
        >>> Solution().spellchecker(['ae', 'aa'], ['UU'])
        ['ae']

        """
        trns = str.maketrans({'a':'.','e':'.','i':'.','o':'.','u':'.'})

        windex = {}
        lindex = {}
        tindex = {}

        n = len(wordlist)
        for i in range(n):
            windex[wordlist[i]] = i
            lindex[wordlist[n - 1 - i].lower()] = n - 1 - i
            tindex[wordlist[n - 1 - i].lower().translate(trns)] = n - 1 - i

        answers = [''] * len(queries)

        for i, query in enumerate(queries):
            j = windex.get(query)
            if j is None:
                querylower = query.lower()
                j = lindex.get(querylower)
                if j is None:
                    j = tindex.get(querylower.translate(trns))
                    if j is None:
                        continue
            answers[i] = wordlist[j]

        return answers

