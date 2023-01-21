"""
Solution of the medium problem
https://leetcode.com/problems/palindrome-partitioning/
"Palindrome Partitioning"
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """Return all possible palindrome partitioning of `s`.

        >>> Solution().partition('aab')
        [['a', 'a', 'b'], ['aa', 'b']]
        >>> Solution().partition('a')
        [['a']]

        """
        res = []

        def palindrome(a):
            return a == a[::-1]

        def backtrack(i, partition):
            if i == len(s):
                res.append(partition)
                return

            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if palindrome(substr):
                    backtrack(j, partition + [substr])

            return

        backtrack(0, [])
        return res

