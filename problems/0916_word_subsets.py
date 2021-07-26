"""
Solution of the medium problem - "Word Subsets",
https://leetcode.com/problems/word-subsets/
"""
from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        """Word Subsets.

        >>> Solution().wordSubsets(
        ...     ['aimazon', 'apple', 'facebook', 'google', 'leetcode'],
        ...     ['e', 'o'],
        ... )
        ['facebook', 'google', 'leetcode']
        >>> Solution().wordSubsets(
        ...     ['aimazon', 'apple', 'facebook', 'google', 'leetcode'],
        ...     ['l', 'e'],
        ... )
        ['apple', 'google', 'leetcode']
        >>> Solution().wordSubsets(
        ...     ['aimazon', 'apple', 'facebook', 'google', 'leetcode'],
        ...     ['e', 'oo'],
        ... )
        ['facebook', 'google']
        >>> Solution().wordSubsets(
        ...     ['aimazon', 'apple', 'facebook', 'google', 'leetcode'],
        ...     ['lo', 'eo'],
        ... )
        ['google', 'leetcode']
        >>> Solution().wordSubsets(
        ...     ['aimazon', 'apple', 'facebook', 'google', 'leetcode'],
        ...     ['ec', 'oc', 'ceo'],
        ... )
        ['facebook', 'leetcode']

        """
        cB = {}
        for b in B:
            cb = Counter(b)
            for key in cb:
                cB[key] = max(cb[key], cB.get(key, 0))

        uwords = []
        for a in A:
            ca = Counter(a)
            if all(ca.get(key, 0) >= cB[key] for key in cB):
                uwords.append(a)

        return uwords

