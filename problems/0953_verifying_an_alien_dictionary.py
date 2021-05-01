"""
Solution of the easy problem - "Verifying an Alien Dictionary",
https://leetcode.com/problems/verifying-an-alien-dictionary/
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """Is Alien Sorted.

        >>> Solution().isAlienSorted(
        ...     ['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz'
        ... )
        True
        >>> Solution().isAlienSorted(
        ...     ['word', 'world', 'row'], 'worldabcefghijkmnpqstuvxyz'
        ... )
        False
        >>> Solution().isAlienSorted(
        ...     ['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz'
        ... )
        False

        """
        def cmp(a: str, b: str):
            if a == b: return 0
            for i in range(max(len(a), len(b))):
                if len(a) <= i: return -1
                if len(b) <= i: return 1
                if order.index(a[i]) < order.index(b[i]):
                    return -1
                elif order.index(a[i]) > order.index(b[i]):
                    return 1
                else:
                    continue
            return 0

        return words == sorted(words, key=cmp_to_key(cmp))

