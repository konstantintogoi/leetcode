"""
Solution of "Longest Common Prefix" problem at
https://leetcode.com/problems/longest-common-prefix/
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Longest Common Prefix.

        >>> Solution().longestCommonPrefix(['flower', 'flow', 'flight'])
        'fl'
        >>> Solution().longestCommonPrefix(['dog', 'racecar', 'car'])
        ''
        
        """
        length, prefix = 201, ''

        for s in strs:
            if len(s) < length:
                length = len(s)

        if length == 201:
            return prefix

        for i in range(length):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j - 1][i]:
                    return prefix
            prefix += strs[0][i]

        return prefix

